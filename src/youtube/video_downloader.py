import logging
import os
import subprocess
import tempfile
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

from config import audio_temp, best_streams, video_temp
from src.youtube.create_folder import create_folder
from src.youtube.on_progress import on_progress
from src.youtube.output_filename import output_filename

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


def _get_streams(url: str, temp_dir: str) -> bool:
    """
    Download the best available video and audio streams for the given URL.

    Args:
        url (str): The YouTube video URL.
        temp_dir (str): The temporary directory to store the downloaded streams.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        yt: YouTube = YouTube(url, on_progress_callback=on_progress)

        for dynamic_stream in best_streams:
            video_res, audio_abr = dynamic_stream.split("|")

            video_stream = yt.streams.filter(res=video_res, progressive=False).first()
            audio_stream = yt.streams.filter(abr=audio_abr, progressive=False).first()

            if video_stream and audio_stream:
                video_stream.download(output_path=temp_dir, filename=video_temp)
                audio_stream.download(output_path=temp_dir, filename=audio_temp)
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


def _merge_streams(temp_dir: str, url: str, download_folder: str) -> None:
    """
    Merge the downloaded video and audio streams into a single file using FFmpeg.

    Args:
        temp_dir (str): The temporary directory where the video and audio streams are stored.
        url (str): The YouTube video URL.
        download_folder (str): The folder to save the merged video file.
    """
    video_temp_path: str = os.path.join(temp_dir, video_temp)
    audio_temp_path: str = os.path.join(temp_dir, audio_temp)
    output_path: str = os.path.join(download_folder, output_filename(YouTube(url).title))
    cmd: str = f"ffmpeg -i {video_temp_path} -i {audio_temp_path} -c:v copy -c:a aac {output_path}"

    if cmd:
        subprocess.call(cmd, shell=True)


def video_downloader(video_url_list: List[str], download_folder: str) -> None:
    """
    Download videos from a list of YouTube video URLs.

    Args:
        video_urls (List[str]): The list of YouTube video URLs to download.
        download_folder (str): The folder to save the downloaded videos.
    """
    successful_downloads = 0
    valid_urls: List[str] = []

    for url in video_url_list:
        if not url:
            continue

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                if _get_streams(url=url, temp_dir=temp_dir):
                    create_folder(download_folder)
                    _merge_streams(temp_dir=temp_dir, url=url, download_folder=download_folder)
                    logger.info(f"The video from {url} was downloaded successfully")
                    successful_downloads += 1
                    valid_urls.append(url)

                else:
                    logger.warning(f"No valid video found at the URL: {url}")

        except Exception as e:
            logger.error(f"Error has occurred while downloading the video from {url}: {e}")

    if successful_downloads != 0 and (successful_downloads == len(valid_urls)):
        messagebox.showinfo(
            title="Finished download",
            message=f"Your download is complete!.\n\n\t{successful_downloads}/{len(video_url_list[1:])}",
        )
