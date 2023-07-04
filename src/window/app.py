from typing import List

import customtkinter as ctk

from config import about_me_buttons, anchor_nw_button, app_geometry, app_name
from src.window.buttons_funcionalities.add_entry import add_entry
from src.window.buttons_funcionalities.clear_entries import clear_entries
from src.window.buttons_funcionalities.close_window import close_window
from src.window.buttons_funcionalities.download_videos import download_videos
from src.window.widgets.buttons import CustomButton
from src.window.widgets.entries import EntryGap
from src.window.widgets.labels import TitleLabel
from src.window.widgets.only_audio_check import OnlyAudioButton
from src.window.widgets.options_menu import CustomMenu
# from src.window.widgets.progress_bar import CustomProgressBar


class CreateWindow(ctk.CTk):
    """Class responsible for creating the main window of the application."""

    def __init__(self) -> None:
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title(app_name)
        self.geometry(app_geometry)
        self.resizable(width=False, height=False)
        self.entry_list: List[EntryGap] = []
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create the widgets in the window."""

        self.create_labels()
        self.create_entry_gaps()
        self.create_menu()
        # self.create_progressbar()

    # TODO Run progress bar in another thread
    # def create_progressbar(self):
    #     self.progress_bar = CustomProgressBar(self)
    #     self.progress_bar.place(relx=0.05, rely=0.85, relheight=0.05, relwidth=0.50)

    def create_menu(self):
        self.menu = CustomMenu(parent=self)
        self.menu.place(relx=0.65, rely=0.05, relheight=0.85, relwidth=0.30)

        self.create_options_menu()
        self.create_about_me_menu()

    def create_about_me_menu(self):
        about_me = self.menu.add_menus(menu_label="About me")
        for config_about_me in about_me_buttons:
            about_me_button = self.menu.add_submenu_buttons(
                parent=about_me, **config_about_me
            )
            about_me_button.pack(pady=20, padx=20, ipadx=0, ipady=7, fill="y")

    def create_options_menu(self):
        options = self.menu.add_menus(menu_label="Options")
        self.only_audio_button = OnlyAudioButton(options, button_text="Only audio")
        self.only_audio_button.pack(pady=20, padx=20, ipadx=0, ipady=7, fill="y")
        config_options_buttons = [
            {"button_text": "Add URL", "command": lambda: add_entry(self.entry_list)},
            {"button_text": "Clear", "command": lambda: clear_entries(self.entry_list)},
            {
                "button_text": "Download",
                "command": lambda: download_videos(self.entry_list),
            },
            {"button_text": "Close", "command": lambda: close_window(self)},
        ]
        for config in config_options_buttons:
            options_button = CustomButton(options, entry_list=self.entry_list, **config)
            options_button.pack(pady=20, padx=20, ipadx=0, ipady=7, fill="y")

    def create_labels(self) -> None:
        self.label = TitleLabel(
            self,
            label_text="Insert the URL from Youtube",
        )
        self.label.place(
            relx=0.05,
            rely=0.03,
            relwidth=0.40,
            relheight=0.075,
            anchor=anchor_nw_button,
        )

    def create_entry_gaps(self) -> None:
        self.entry_gap = EntryGap(self, width=300)
        self.entry_gap.place(
            relx=0.05, rely=0.25, relheight=0.1, relwidth=0.50, anchor="w"
        )
        self.entry_list.append(self.entry_gap)
