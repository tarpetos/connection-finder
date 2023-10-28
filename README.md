# Internet Connection Finder

---

## Overview

This Python project is designed to check the availability of an internet connection on your current device. It features
a simple user interface with two buttons: "Start" and "Stop." The "Start" button allows you to search for an internet
connection. If a connection is found, it plays a sound and enables the button. If a connection is not present, it
disables the button and continuously sends connection requests until a connection is established. The "Stop" button
allows you to halt the search and stop any sound that may be playing.

## Usage

You can choose between two different user interfaces (UI) for this application: Tkinter or Flet. To use the application,
follow the steps below:

1. **Install the required dependencies:**
   ```bash
   pip install requirements.txt
   ```

2. **Import the necessary components in your Python scrip:**
   ```python
   from connection_finder import AppStarter
   from connection_finder.types import AppOptionString, AppOption
   ```

3. **Define the main function in your script, which initializes and starts the application. Choose either
   AppOption.TKINTER or AppOption.FLET to specify the UI you want to use:**
   ```python
   def main(option: AppOptionString) -> None:
       starter = AppStarter()
       starter.start(option)
   
   if __name__ == "__main__":
       main(option=AppOption.TKINTER)  # Use AppOption.FLET to use the Flet UI
   ```

4. Run your Python script, and the Internet Connection Finder application will be launched with the chosen UI.

# Examples

## Tkinter UI

<div style="text-align:center; border-radius: 5%; overflow: hidden; margin: 0 auto;">
  <img src="examples/tkinter.png" style="width: 100%; height: 100%; object-fit: cover;" alt="">
</div>

---

## Flet UI

<div style="text-align:center; border-radius: 5%; overflow: hidden; margin: 0 auto;">
  <img src="examples/flet.png" style="width: 100%; height: 100%; object-fit: cover;" alt="">
</div>

# Licensing

This project is released under the MIT License. You are free to use and modify the code as needed.