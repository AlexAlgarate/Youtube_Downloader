from typing import Union

import customtkinter as ctk

from config import font


class TitleLabel(ctk.CTkLabel):
    """Custom Label widget representing a title label."""

    def __init__(self, parent: ctk.CTk, label_text: str, **kwargs: Union[float, str]) -> None:
        """Initialize the TitleLabel.

        Args:
            parent (tk.Tk): The parent Tkinter window.
            text_label (str): The text to display on the label.
            **kwargs: Additional keyword arguments to configure the widget.

        """
        super().__init__(master=parent, text=label_text, font=font, justify="left", **kwargs)
