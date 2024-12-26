# 🖥️ Keylogger Project ⌨️

Welcome to the **Python-based Keylogger Project**! This tool captures and logs keyboard keystrokes in real-time. It's a great way to learn about keylogging and how to work with input events in Python. The keylogger supports periodic saving and handles special keys such as `space`, `enter`, `tab`, `backspace`, and `esc`. Plus, it provides a colorful console output! 🌈

## 🚀 Features

- 📝 **Log keystrokes**: Captures every key pressed and saves them to a file.
- ⏰ **Periodic saving**: Automatically saves keystrokes after every set number of key presses.
- 🕐 **Background saving**: Logs are saved every 60 seconds in the background.
- 🔑 **Handles special keys**: Logs keys like `space`, `enter`, `tab`, `backspace`, and `esc`.
- 🎨 **Color-coded output**: 
  - Green for successful logging ✅
  - Red for errors ❌
  - Cyan for the start of logging 💻
  - Yellow for stopping the keylogger 🛑

## 🛠️ Requirements

To run this project, you’ll need:

- Python 3.x 🐍
- `pynput` library 🖱️
- `colorama` library 🌈

## 🧑‍💻 Installation

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/RoNiXxCybSeC0101/PRODIGY_CS_TASK4.git
    cd keylogger-project
    ```

2. **Install the required Python libraries**:

    ```bash
    pip install pynput colorama
    ```

## 🔧 Usage

1. **Run the keylogger** script:

    ```bash
    python keylogger.py
    ```

2. The keylogger will start and begin logging your keystrokes. All captured keys will be saved in the specified directory.

3. Press the `ESC` key to **stop** the keylogger. 🛑

## ⚙️ Configuration

You can easily modify these variables in the script to fit your needs:

- `file_path`: Directory where the keystrokes will be saved.
- `key_information`: The filename where the keys will be logged.
- `save_interval`: Number of key presses after which the keys are saved.

### Example Configuration:

```python
file_path = "D:\\Python Projects\\keylogger project\\project"  # Update with your desired directory
key_information = "key_log.txt"
save_interval = 10  # Save after every 10 key presses
```

## 📸 Screenshots 

![image](https://github.com/user-attachments/assets/df6821ba-653a-4db6-92cf-63cd09ce363a)

![image](https://github.com/user-attachments/assets/0fe03e05-043b-4b88-b34c-ffd72437894d)

### after running the tool i just browse facebook.com into a browser 

![image](https://github.com/user-attachments/assets/f8726ec6-3221-477f-9616-af94c54696c3)

![image](https://github.com/user-attachments/assets/568cfdeb-70f5-4d80-8279-4d4800636cd0)

### then i clicked "esc" button to stop the keylogger 

![image](https://github.com/user-attachments/assets/4e58f737-c255-467e-b299-62d482953fd3)

### and in the keylog.txt we can see the keys i logged when i enter facebook.com into the browser

![image](https://github.com/user-attachments/assets/3a0be6db-31f5-43a1-beb5-68adebe5760c)

## 🔚 Conclusion

This project demonstrates the basic functionality of a keylogger in Python. While it serves as a simple tool to show how keylogging works, it is highly efficient and can be expanded upon. With further development, this keylogger can be compiled into a standalone executable (`.exe`), making it even more versatile and easy to distribute without needing Python installed on the target machine. 🚀

This tool is intended for **educational purposes only** and serves as a great foundation for learning about keyboard events, logging, and building useful security tools. Use it responsibly and ethically. 💻



