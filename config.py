from typing import List, Tuple, Union

# Aplication name and size of the window
app_name: str = "YOUTUBE DOWNLOADER"
app_size: str = "600x350"

# Directory for downloads
video_download_folder: str = "Downloads/Videos"
audio_download_folder: str = "Downloads/Audios"

# Limit of entry gaps
limit: int = 3

# Font options
font_family: str = "Helvetica"
font_size: int = 16
font: Tuple[str, Union[int, str]] = (f"{font_family}", font_size)

# Background colors
window_bg = only_audio_bg = add_entry_bg = "#c2f2de"
download_button_bg: str = "#6bcfb7"
label_bg: str = "#fad79b"
entry_bg: str = "#c4fa9b"

# URLs
github_url: str = "https://github.com/AlexAlgarate?tab=repositories"
linkedin_url: str = "https://www.linkedin.com/in/alex-algarate/"

# Browser options
new_browser: int = 1  # 0: same window

video_temp = "video.mp4"
audio_temp = "audio.mp4"

best_streams: List[str] = [
    "2160p|160kbps",
    "1440p|160kbps",
    "1080p|160kbps",
    "720p|160kbps",
    "720p|128kbps",
    "480p|160kbps",
    "480p|128kbps",
]
