import os


def create_folder(download_folder: str) -> None:
    """
    Create a folder at the specified path if it doesn't already exist.

    Args:
        download_folder (str): Path of the folder to be created.
    """
    try:
        os.makedirs(download_folder, exist_ok=True)
    except OSError as e:
        print(f"An error has occurred: {e}")
