from tkinter import messagebox
from typing import Any, List, cast

import customtkinter as ctk

from config import limit
from src.window.widgets.entries import EntryGap


def add_entry(entry_list: List[Any]) -> None:
    """Add an entry gap to the list.

    This function adds a new entry gap widget to the given list of entry gaps.
    The new entry gap is positioned below the last entry in the list.

    Args:
        entry_list (List[Any]): The list of entry gaps.

    """
    if len(entry_list) <= limit:
        parent_widget: ctk.CTk = cast(ctk.CTk, entry_list[0].master)
        last_entry: Any = entry_list[-1]
        rely: Any = last_entry.winfo_y() + last_entry.winfo_height() + 40

        entry_gap = EntryGap(parent_widget)
        entry_gap.place(
            relx=0.05,
            rely=rely / parent_widget.winfo_height(),
            relheight=0.1,
            relwidth=0.60,
            anchor="w",
        )
        entry_list.append(entry_gap)
    else:
        messagebox.showinfo(
            title="Limit exceeded",
            message="Download limit reached.\nFirst, download these videos.",
        )
