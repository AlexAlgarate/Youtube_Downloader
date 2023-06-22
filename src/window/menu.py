import tkinter as tk
import webbrowser
from tkinter import messagebox

from config import github_url, linkedin_url, new_browser


class MenuBar(tk.Menu):
    """Custom menu bar for the application."""

    def __init__(self, parent: tk.Tk) -> None:
        """Initialize the menu bar.

        Args:
            parent (tk.Tk): The parent Tkinter window.
        """
        super().__init__(parent)
        self._create_about_me_menu()
        self.add_command(label="Close", command=self.close_window)

    def _create_about_me_menu(self) -> None:
        """Create the 'About me' menu."""
        about_me = tk.Menu(self, tearoff=False, font=("Arial", 12))
        self.add_cascade(label="About me", menu=about_me)
        about_me.add_command(
            label="Linkedin",
            command=lambda: self.open_url(linkedin_url),
        )
        about_me.add_command(label="Github", command=lambda: self.open_url(github_url))

    def open_url(self, url: str) -> None:
        """Open the provided URL in a web browser.

        Args:
            url (str): The URL to open.
        """
        webbrowser.open(url, new=new_browser)

    def close_window(self) -> None:
        """Close the application window with user confirmation."""
        answer: bool = messagebox.askyesno(title="Close", message="Do you want to close the program?")
        if answer:
            self.quit()
