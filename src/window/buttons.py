from tkinter import BooleanVar, messagebox
from typing import Any, Callable, List, Optional, Union, cast

import customtkinter as ctk

from config import audio_download_folder, font, limit, video_download_folder
from src.window.entries import EntryGap
from src.youtube.audio_downloader import audio_downloader
from src.youtube.video_downloader import video_downloader


class CustomButton(ctk.CTkButton):
    def __init__(
        self,
        parent: ctk.CTk,
        button_text: str,
        command: Optional[Callable],
        entry_list: List[Any],
        **kwargs: Union[float, str]
    ) -> None:
        self.entry_list: List[Any] = entry_list
        super().__init__(
            master=parent,
            text=button_text,
            command=command,
            font=font,
        )
        self.place(**kwargs)


def add_entry(entry_list: List[Any]) -> None:
    """Add an entry gap to the list."""
    if len(entry_list) <= limit:
        parent_widget: ctk.CTk = cast(ctk.CTk, entry_list[0].master)
        last_entry: Any = entry_list[-1]
        rely: Any = last_entry.winfo_y() + last_entry.winfo_height() + 40

        entry_gap = EntryGap(parent_widget)
        entry_gap.place(
            relx=0.05,
            rely=rely / parent_widget.winfo_height(),
            relheight=0.1,
            relwidth=0.60,
            anchor="w",
        )
        entry_list.append(entry_gap)
    else:
        messagebox.showinfo(
            title="Limit exceeded",
            message="Download limit reached.\nFirst, download these videos.",
        )


def clear_entries(entry_list: List[EntryGap]) -> None:
    """Clear the entries."""
    for entry in entry_list:
        entry.delete(0, "end")


def download_videos(entry_list: List[EntryGap]) -> None:
    """Download the videos."""
    url_list: List[str] = [entry.get() for entry in entry_list]
    if OnlyAudioButton.audio_only_var and OnlyAudioButton.audio_only_var.get():
        audio_downloader(audio_url_list=url_list, download_folder=audio_download_folder)
    else:
        video_downloader(video_url_list=url_list, download_folder=video_download_folder)


class OnlyAudioButton(ctk.CTkCheckBox):
    """Checkbutton to toggle audio-only download."""

    audio_only_var: Union[BooleanVar, None] = None

    def __init__(self, parent: ctk.CTk, button_text: str, **kwargs: Union[float, str]) -> None:
        """Initialize the OnlyAudioButton.

        Args:
            parent (tk.Tk): The parent Tkinter window.
            button_text (str): The text to display on the button.
            **kwargs: Additional keyword arguments to configure the widget.

        """
        if OnlyAudioButton.audio_only_var is None:
            OnlyAudioButton.audio_only_var = ctk.BooleanVar()
        super().__init__(
            master=parent,
            text=button_text,
            variable=self.audio_only_var,
            font=font,
        )
        self.place(**kwargs)
