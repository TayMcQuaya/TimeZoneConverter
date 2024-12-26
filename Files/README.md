# Time Zone Converter

## Overview
The Time Zone Converter is a simple GUI program that allows users to:
- View the current time in various time zones.
- Convert a custom time into multiple time zones.

## How to Use
1. **Launch the Program**:
   - Double-click the shortcut `Time Zone Converter` to start the program.

2. **Select a Time Zone**:
   - Use the dropdown to select your desired time zone.

3. **Fetch Current Time**:
   - Click the "Fetch Current Time" button to view the current time in all predefined time zones.

4. **Convert Custom Time**:
   - Enter a custom time in the format `HH:MM` (e.g., 02:30).
   - Choose AM or PM from the dropdown.
   - Click "Calculate Custom Time" to see the converted times.

## Requirements
- Python 3.x installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
- Required Python modules: `tkinter`, `pytz`.

## Installing Required Modules
To install the required modules, run the following commands in your terminal or command prompt:
```bash
pip install pytz
```
Note: `tkinter` is typically included with Python by default. If it is missing, refer to [tkinter installation guide](https://tkdocs.com/tutorial/install.html).

## Icon
The program includes a custom icon (`icon.ico`) for the shortcut.

## Files
- `timezone.pyw`: The main program file.
- `icon.ico`: The custom icon for the program.
