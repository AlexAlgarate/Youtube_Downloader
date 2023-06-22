import logging
from logging import Logger
from tkinter import messagebox
from typing import Dict, List, Type

from pytube import YouTube
from pytube.exceptions import (
    AgeRestrictedError,
    RegexMatchError,
    VideoPrivate,
    VideoRegionBlocked,
    VideoUnavailable,
)

from config import best_streams
from src.youtube.create_folder import create_folder
from src.youtube.on_progress import on_progress
from src.youtube.output_filename import output_filename

logging.basicConfig(level=logging.INFO)
logger: Logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


logger.setLevel(logging.DEBUG)


def _download_audio(url: str, download_folder: str) -> bool:
    """
    Downloads a YouTube audio given its URL.

    Args:
        url (str): The URL of the YouTube video.
        directory (str): The directory to save the downloaded audios.


    Returns:
        bool: True if the audio was downloaded successfully, False otherwise.
    """
    try:
        yt: YouTube = YouTube(url, on_progress_callback=on_progress)
        for dynamic_stream in best_streams:
            _, audio_abr = dynamic_stream.split("|")

            audio_stream = yt.streams.filter(abr=audio_abr, progressive=False).first()

            if audio_stream:
                audio_stream.download(output_path=download_folder, filename=output_filename(yt.title))
                return True

        return False

    except (
        RegexMatchError,
        AgeRestrictedError,
        VideoPrivate,
        VideoRegionBlocked,
        VideoUnavailable,
    ) as e:
        error_messages: Dict[
            Type[RegexMatchError]
            | Type[AgeRestrictedError]
            | Type[VideoPrivate]
            | Type[VideoRegionBlocked]
            | Type[VideoUnavailable],
            str,
        ] = {
            RegexMatchError: "Insert a valid URL",
            AgeRestrictedError: "This video is age restricted.",
            VideoPrivate: "This video is private.",
            VideoRegionBlocked: "This video is not available in your region.",
            VideoUnavailable: "This video is unavailable.",
        }
        error_type = type(e)
        if error_type in error_messages:
            messagebox.showerror(title="Error", message=error_messages[error_type])
        else:
            messagebox.showerror(title="Error", message=f"An unknown error occurred: {e}")
        return False


def audio_downloader(audio_url_list: List[str], download_folder: str) -> None:
    """
    Downloads multiple YouTube audios from a list of URLs.

    Args:
        audio_url_list (List[str]): A list of YouTube video URLs.
        download_folder (str): The directory to save the downloaded audos.

    """
    successful_downloads = 0
    valid_urls: List[str] = []

    for url in audio_url_list:
        if not url:
            continue

        try:
            if _download_audio(url, download_folder=download_folder):
                create_folder(download_folder=download_folder)
                logger.info(f"The audio from {url} was downloaded successfully")
                successful_downloads += 1
                valid_urls.append(url)

            else:
                logger.warning(f"No valid audio found at the URL: {url}")

        except Exception as e:
            logger.error(f"Error has occurred while downloading the audio from {url}: {e}")

    if successful_downloads != 0 and (successful_downloads == len(valid_urls)):
        messagebox.showinfo(
            title="Finished download",
            message=f"Your download is complete!.\n\n\t{successful_downloads}/{len(audio_url_list[1:])}",
        )
