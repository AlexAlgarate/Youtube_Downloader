from src.window.widgets import CreateWindow


def start_downloader() -> CreateWindow:
    app = CreateWindow()
    app.create_widgets()
    return app


if __name__ == "__main__":
    start_downloader().mainloop()
