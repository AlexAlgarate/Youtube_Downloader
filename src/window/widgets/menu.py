import webbrowser
from typing import Dict, List

import customtkinter as ctk

from config import font, new_browser


class AboutMeMenu(ctk.CTkOptionMenu):
    """Initialize the AboutMeMenu.

    Args:
        parent (ctk.CTk): The parent CustomTkinter window.
        menu_name (str): The name of the menu.
        submenu (List[str]): The list of submenu options.
        button_bg_color (str): The background color of the button.
        urls (Dict[str, str]): A dictionary mapping submenu options
            to their corresponding URLs.
        **kwargs: Additional keyword arguments to configure the widget.

    """

    def __init__(
        self,
        parent: ctk.CTk,
        menu_name: str,
        submenu: List[str],
        button_bg_color: str,
        urls: Dict[str, str],
        **kwargs
    ):
        super().__init__(
            master=parent,
            values=submenu,
            fg_color=button_bg_color,
            font=font,
            dropdown_font=font,
            anchor="center",
            dynamic_resizing=False,
            command=self.option_menu_command,
        )
        self.urls = urls
        self.place(**kwargs)
        self.set(menu_name)

    def option_menu_command(self, value: str) -> None:
        """Open the URL associated with the selected menu option.

        Args:
            value (str): The selected menu option.

        """
        url = self.urls.get(value)
        if url:
            self.open_url(url)

    def open_url(self, url: str) -> None:
        """Open the provided URL in a web browser.

        Args:
            url (str): The URL to open.

        """
        webbrowser.open(url, new=new_browser)
