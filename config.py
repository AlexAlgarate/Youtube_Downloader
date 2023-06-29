from typing import Dict, List, Tuple, Union

# GENERAL APP CONFIG
app_name: str = "YOUTUBE DOWNLOADER"
geometry: Tuple[int, int] = (850, 550)
app_geometry: str = "{}x{}".format(*geometry)

# Directory for downloads
video_download_folder: str = "Downloads/Videos"
audio_download_folder: str = "Downloads/Audios"

# Name of temp files
video_temp = "video.mp4"
audio_temp = "audio.mp4"

# Limit of entry gaps
limit: int = 3

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


# GENERAL WIDGETS CONFIG
button_bg_color: str = "#3b8ed0"
anchor_nw_button: str = "nw"
anchor_center_button: str = "center"
font_family: str = "Helvetica"
font_size: int = 20
font: Tuple[str, Union[int, str]] = (f"{font_family}", font_size)
corner_radius: int = 8

# Config Menu
new_browser: int = 1  # 0: same window
about_me_buttons: Dict[str, str] = [
    {
        "button_text": "Github",
        "url": "https://github.com/AlexAlgarate?tab=repositories",
    },
    {
        "button_text": "Linkedin",
        "url": "https://www.linkedin.com/in/alex-algarate/"
    }
]
