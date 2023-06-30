from pytube import YouTube


def on_progress(stream: YouTube, chunk: bytes, bytes_remaining: int) -> str:
    """
    Calculate and return the progress of a download.

    Args:
        stream (YouTube): The YouTube stream being downloaded.
        chunk (bytes): The downloaded chunk of data.
        bytes_remaining (int): The number of bytes remaining to be downloaded.

    Returns:
        str: A string representing the progress of the download in percentage.
    """
    percentage_of_download = str(
        int((stream.filesize - bytes_remaining) / stream.filesize * 100)
    )
    print(f"Downloaded {percentage_of_download} %")
