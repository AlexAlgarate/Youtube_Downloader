from typing import Dict, List

import customtkinter as ctk

from config import (
    app_name,
    app_size,
    button_bg_color,
    menu_name,
    submenu_names,
    urls_submenu,
)
from src.window.buttons_funcionalities.add_entry import add_entry
from src.window.buttons_funcionalities.clear_entries import clear_entries
from src.window.buttons_funcionalities.close_window import close_window
from src.window.buttons_funcionalities.download_videos import download_videos
from src.window.widgets.buttons import CustomButton
from src.window.widgets.entries import EntryGap
from src.window.widgets.labels import TitleLabel
from src.window.widgets.menu import AboutMeMenu
from src.window.widgets.OnlyAudioButton import OnlyAudioButton


class CreateWindow(ctk.CTk):
    """Class responsible for creating the main window of the application."""

    def __init__(self) -> None:
        super().__init__()
        """Initialize the CreateWindow instance."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title(app_name)
        self.geometry(app_size)
        self.resizable(width=False, height=False)

        self.entry_list: List[EntryGap] = []

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create the widgets in the window."""

        self._create_labels()
        self._create_entry_gaps()
        self._create_only_audio_button()
        self._create_frame_buttons()
        self._create_menu()

    def _create_menu(self):
        """Create the menu in the window."""
        about_me_urls: Dict[str, str] = {
            option: url for option, url in zip(submenu_names, urls_submenu)
        }

        self.menu = AboutMeMenu(
            self,
            menu_name=menu_name,
            submenu=submenu_names,
            button_bg_color=button_bg_color,
            urls=about_me_urls,
        )
        self.menu.place(relx=0.70, rely=0.10, relheight=0.10, relwidth=0.25, anchor="w")

    def _create_labels(self) -> None:
        """Create labels in the window."""

        self.label = TitleLabel(
            self,
            label_text="Insert the URL from Youtube",
            fg_color="#3b8ed0",
            corner_radius=8,
        )
        self.label.place(
            relx=0.05,
            rely=0.10,
            relwidth=0.40,
            relheight=0.10,
            anchor="w",
        )

    def _create_entry_gaps(self) -> None:
        self.entry_gap = EntryGap(self, width=300)
        self.entry_gap.place(
            relx=0.05, rely=0.25, relheight=0.1, relwidth=0.60, anchor="w"
        )

        self.entry_list.append(self.entry_gap)

    def _create_only_audio_button(self) -> None:
        """Create the buttons in the window."""
        self.only_audio_button = OnlyAudioButton(self, button_text="Only audio")
        self.only_audio_button.place(
            relx=0.75,
            rely=0.25,
            relwidth=0.2,
            relheight=0.10,
            anchor="w",
        )

    def _create_frame_buttons(self):
        button_configurations = [
            {
                "button_text": "Clear",
                "entry_list": self.entry_list,
                "command": lambda: clear_entries(self.entry_list),
                "relx": 0.05,
                "rely": 0.85,
                "relheight": 0.10,
                "relwidth": 0.18,
                "anchor": "nw",
            },
            {
                "button_text": "Add URL",
                "entry_list": self.entry_list,
                "command": lambda: add_entry(self.entry_list),
                "relx": 0.28,
                "rely": 0.85,
                "relheight": 0.10,
                "relwidth": 0.18,
                "anchor": "nw",
                "fg_color": "#3b8ed0",
            },
            {
                "button_text": "Download",
                "entry_list": self.entry_list,
                "command": lambda: download_videos(self.entry_list),
                "relx": 0.51,
                "rely": 0.85,
                "relheight": 0.10,
                "relwidth": 0.18,
                "anchor": "nw",
                "fg_color": "#3b8ed0",
            },
            {
                "button_text": "Close",
                "entry_list": self.entry_list,
                "command": lambda: close_window(self),
                "relx": 0.74,
                "rely": 0.85,
                "relheight": 0.10,
                "relwidth": 0.18,
                "anchor": "nw",
            },
        ]

        for config in button_configurations:
            button = CustomButton(self, **config)
            button.place(
                relx=config["relx"],
                rely=config["rely"],
                relheight=config["relheight"],
                relwidth=config["relwidth"],
                anchor=config["anchor"],
            )
