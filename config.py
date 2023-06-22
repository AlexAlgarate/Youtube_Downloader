from typing import List, Tuple, Union

# Aplication name and size of the window
app_name: str = "YOUTUBE DOWNLOADER"
app_size: str = "600x365"

# Directory for downloads
video_download_folder: str = "Downloads/Videos"
audio_download_folder: str = "Downloads/Audios"

# Name of temp files
video_temp = "video.mp4"
audio_temp = "audio.mp4"

# Limit of entry gaps
limit: int = 3

# Font options
font_family: str = "Helvetica"
font_size: int = 14
font: Tuple[str, Union[int, str]] = (f"{font_family}", font_size)

# Background colors
button_bg_color: str = "#3b8ed0"

# List of best quality streams
best_streams: List[str] = [
    "2160p|160kbps",
    "1440p|160kbps",
    "1080p|160kbps",
    "720p|160kbps",
    "720p|128kbps",
    "480p|160kbps",
    "480p|128kbps",
]

# About Me menu config
menu_name: str = "About Me"
github_url: str = "https://github.com/AlexAlgarate?tab=repositories"
linkedin_url: str = "https://www.linkedin.com/in/alex-algarate/"
new_browser: int = 1  # 0: same window
submenu_names: List[str] = ["Github", "Linkedin"]
urls_submenu: List[str] = [github_url, linkedin_url]
