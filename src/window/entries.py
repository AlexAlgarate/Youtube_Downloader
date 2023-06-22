import customtkinter as ctk
from typing import Union


class EntryGap(ctk.CTkEntry):
    """Custom Entry widget representing a gap for user input."""

    def __init__(self, parent: ctk.CTk, **kwargs: Union[float, str]) -> None:
        """Initialize the EntryGap.

        Args:
            parent (tk.Tk): The parent Tkinter window.
            **kwargs: Additional keyword arguments to configure the widget.

        """
        super().__init__(master=parent, **kwargs)
        self.audio_only_button = ctk.BooleanVar()
