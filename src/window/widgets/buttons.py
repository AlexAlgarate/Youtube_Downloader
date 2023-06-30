from typing import Any, Callable, List, Optional, Union

import customtkinter as ctk

from config import button_bg_color, corner_radius, font


class CustomButton(ctk.CTkButton):
    def __init__(
        self,
        parent: ctk.CTk,
        button_text: str,
        command: Optional[Callable],
        entry_list: List[Any] = None,
        **kwargs: Union[float, str],
    ) -> None:
        self.entry_list: List[Any] = entry_list
        super().__init__(
            master=parent,
            text=button_text,
            command=command,
            font=font,
            fg_color=button_bg_color,
            corner_radius=corner_radius,
            **kwargs,
        )
        self.pack()
