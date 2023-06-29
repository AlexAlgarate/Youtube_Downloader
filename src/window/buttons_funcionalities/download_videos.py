from typing import List

from config import audio_download_folder, video_download_folder
from src.window.widgets.entries import EntryGap
from src.window.widgets.only_audio_check import OnlyAudioButton
from src.youtube.audio_downloader import audio_downloader
from src.youtube.video_downloader import video_downloader


def download_videos(entry_list: List[EntryGap]) -> None:
    """Download the videos."""
    url_list: List[str] = [entry.get() for entry in entry_list]
    if OnlyAudioButton.audio_only_var and OnlyAudioButton.audio_only_var.get():
        audio_downloader(audio_url_list=url_list, download_folder=audio_download_folder)
    else:
        video_downloader(video_url_list=url_list, download_folder=video_download_folder)
