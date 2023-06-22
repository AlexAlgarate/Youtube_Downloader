from typing import List

from src.window.widgets.entries import EntryGap


def clear_entries(entry_list: List[EntryGap]) -> None:
    """Clear the entries.

    This function clears the text in each entry gap widget within the given list.
    It iterates over the entry_list and calls the delete
    method on each entry to remove the text.

    Args:
        entry_list (List[EntryGap]): The list of entry gaps.

    """
    for entry in entry_list:
        entry.delete(0, "end")
