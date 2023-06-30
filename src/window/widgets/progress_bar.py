import customtkinter as ctk


class CustomProgressBar(ctk.CTkProgressBar):
    def __init__(self, parent: ctk.CTk, *args):
        super().__init__(master=parent, *args)
        self.set(0)
        self.place(*args)
