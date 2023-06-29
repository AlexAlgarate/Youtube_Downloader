import webbrowser

from config import new_browser


def open_url(url: str) -> None:
    """Open the provided URL in a web browser.

    Args:
        url (str): The URL to open.

    """
    webbrowser.open(url, new=new_browser)
