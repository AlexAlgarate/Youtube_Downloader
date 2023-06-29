from typing import Union

import customtkinter as ctk

from config import button_bg_color, corner_radius, font


class TitleLabel(ctk.CTkLabel):
    """Custom Label widget representing a title label."""

    def __init__(
        self, parent: ctk.CTk, label_text: str, **kwargs: Union[float, str]
    ) -> None:
        """Initialize the TitleLabel.

        Args:
            parent (ctk.CTk): The parent CustomTkinter window.
            label_text (str): The text to display on the label.
            **kwargs: Additional keyword arguments to configure the widget.

        """
        super().__init__(
            master=parent,
            text=label_text,
            font=font,
            justify="left",
            corner_radius=corner_radius,
            fg_color=button_bg_color,
            **kwargs
        )
