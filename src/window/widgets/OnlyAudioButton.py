from tkinter import BooleanVar
from typing import Union

import customtkinter as ctk

from config import font


class OnlyAudioButton(ctk.CTkCheckBox):
    """Checkbutton to toggle audio-only download."""

    audio_only_var: Union[BooleanVar, None] = None

    def __init__(
        self, parent: ctk.CTk, button_text: str, **kwargs: Union[float, str]
    ) -> None:
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
