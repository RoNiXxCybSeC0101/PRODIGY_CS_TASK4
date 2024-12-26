# Keylogger Project

This is a Python-based keylogger that captures and logs keystrokes from the keyboard. The keylogger supports periodic saving of keystrokes and handles special keys such as `space`, `enter`, `tab`, `backspace`, and `esc`. It also offers a user-friendly output with color-coded logging messages using the `colorama` library.

## Features

- Logs keystrokes to a file in a specified directory.
- Periodic saving after every set number of key presses.
- Periodic saving of logs every 60 seconds in the background.
- Supports logging of special keys (e.g., `space`, `enter`, `tab`, `esc`).
- Color-coded console output for easy identification of actions:
  - Green for successful logging.
  - Red for errors.
  - Cyan for the start of logging.
  - Yellow for stopping the keylogger.

## Requirements

- Python 3.x
- `pynput` library
- `colorama` library

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/keylogger-project.git
    cd keylogger-project
    ```

2. Install the required Python libraries:

    ```bash
    pip install pynput colorama
    ```

## Usage

1. Run the keylogger script:

    ```bash
    python keylogger.py
    ```

2. The keylogger will start capturing keystrokes, and the captured keys will be saved in the specified directory.

3. Press the `ESC` key to stop the keylogger.

## Configuration

You can modify the following variables in the script to customize the keylogger:

- `file_path`: The directory where the keylogger will save the keystrokes.
- `key_information`: The name of the file where the keystrokes will be logged.
- `save_interval`: The number of keystrokes after which the keys are saved.

## Example

```python
file_path = "D:\\Python Projects\\keylogger project\\project"  # Update with your desired directory
key_information = "key_log.txt"
save_interval = 10  # Save after every 10 key presses
