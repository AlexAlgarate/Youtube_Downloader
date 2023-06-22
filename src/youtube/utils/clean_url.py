import urllib.parse


def clean_youtube_url(url: str) -> str:
    """
    Clean the YouTube video URL by removing unwanted parameters.

    Args:
        url (str): The YouTube video URL.

    Returns:
        str: The cleaned YouTube video URL.
    """
    parsed_url = urllib.parse.urlparse(url)
    cleaned_query = urllib.parse.parse_qs(parsed_url.query)

    # Remove unwanted parameters
    cleaned_query.pop("t", None)

    # Reconstruct the URL without unwanted parameters
    cleanes_url_parts = list(parsed_url)
    cleanes_url_parts[4] = urllib.parse.urlencode(cleaned_query, doseq=True)
    cleaned_url = urllib.parse.urlunparse(cleanes_url_parts)

    return cleaned_url
