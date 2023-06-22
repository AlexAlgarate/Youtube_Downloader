import re


def output_filename(youtube_title: str) -> str:
    """
    Generate a valid filename based on the given title.

    Special characters are removed from the title and the filename is constructed
    by capitalizing the first letter of each word in the title and joining them with underscores.
    Only the first 10 words are considered.

    Args:
        youtube_title (str): The title from which to generate the filename.

    Returns:
        str: The generated filename.
    """
    youtube_title = re.sub(r"[^\w\s-]", " ", youtube_title)
    filename: str = "_".join([word.capitalize() for word in youtube_title.split()[:10]])
    return f"{filename}.mp4"
