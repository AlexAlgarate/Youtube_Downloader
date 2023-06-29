import customtkinter as ctk

from config import (
    anchor_center_button,
    anchor_nw_button,
    button_bg_color,
    corner_radius,
)
from src.window.buttons_funcionalities.open_urls import open_url
from src.window.widgets.buttons import CustomButton


class CustomMenu(ctk.CTkTabview):
    def __init__(self, parent: ctk.CTk, **kwargs):
        super().__init__(
            master=parent,
            corner_radius=corner_radius,
            segmented_button_selected_hover_color=button_bg_color,
            segmented_button_selected_color=button_bg_color,
            **kwargs
        )
        self.place(anchor=anchor_nw_button, **kwargs)

    def add_menus(self, menu_label: str):
        self.menu = self.add(menu_label)
        return self.menu

    def add_submenu_buttons(
        self, parent: ctk.CTkTabview, button_text: str, url: str, **kwargs
    ) -> CustomButton:
        button: CustomButton = CustomButton(
            parent=parent,
            button_text=button_text,
            command=lambda: open_url(url=url),
        )
        button.pack(anchor=anchor_center_button, **kwargs)
        return button
