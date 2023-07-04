# Youtube_Downloader

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![example workflow](https://github.com/AlexAlgarate/Youtube_Downloader/actions/workflows/actions.yml/badge.svg)](https://github.com/AlexAlgarate/Youtube_Downloader/actions/workflows/actions.yml)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/AlexAlgarate/Youtube_Downloader?color=green&style=flat-square)
![GitHub release (with filter)](https://img.shields.io/github/v/release/AlexAlgarate/Youtube_Downloader)

This is a simple YouTube video downloader application built using Python and the tkinter library. It allows you to download YouTube videos and audio by providing their URLs.

## Requirements

- Python 3.10
- pytube
- tkinter library

## Installation

1. Clone the repository or download the code files.
2. Install the required libraries by running the following command:

    ```text
    pip install -r requirements.txt
    ```

## Usage

1. Launch the application by running the `main.py` file.

    ```python
    python main.py
    ```

2. Enter the URL of the YouTube video you want to download into the provided input field.
3. Select the only audio option if you desired this option.
4. Click the "Download" button to initiate the download.
5. The video or audio will be saved to the specified directory on your local machine.
6. Repeat the process for any additional videos or audio you want to download.

## Features

- Provides options to choose between video and audio downloads in sequence.
- Provides error handling for various exceptions that may occur during the download process.
- Displays informative messages and error dialogs to the user.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).