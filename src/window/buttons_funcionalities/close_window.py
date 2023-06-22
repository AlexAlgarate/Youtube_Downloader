import customtkinter as ctk


def close_window(window: ctk.CTk) -> None:
    """Close the window.
    It destroys the Tkinter window, terminating the application.

    Args:
        window (ctk.CTk): The Tkinter window to be closed.

    """
    window.destroy()
