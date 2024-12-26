import tkinter as tk
from tkinter import ttk
from tkinter import font  # Import the font module
from datetime import datetime, date
import pytz

# Predefined timezones
TIMEZONES = {
    "Denpasar, Bali, Indonesia": "Asia/Makassar",
    "Germany (Berlin)": "Europe/Berlin",
    "EST (Eastern Standard Time)": "America/New_York",
    "CST (Central Standard Time)": "America/Chicago",
    "PST (Pacific Standard Time)": "America/Los_Angeles",
}

def fetch_current_time():
    """
    Fetch and display the current time in the selected timezone and convert to other timezones.
    """
    try:
        # Get the current time in UTC
        now_utc = datetime.now(pytz.utc)

        # Get the selected timezone from the dropdown
        input_timezone = selected_timezone.get()
        local_tz = pytz.timezone(TIMEZONES[input_timezone])

        # Localize the current time to the selected timezone
        local_time = now_utc.astimezone(local_tz)

        # Clear the result area
        result_text.delete(1.0, tk.END)

        # Convert the time to all predefined timezones
        for location, tz_name in TIMEZONES.items():
            target_tz = pytz.timezone(tz_name)
            target_time = local_time.astimezone(target_tz)
            
            # Insert location and colon
            result_text.insert(tk.END, f"{location}: ")
            
            # Insert time with bold tag
            formatted_time = target_time.strftime('%I:%M %p')
            result_text.insert(tk.END, f"{formatted_time}", "bold_time")
            
            # Insert day of the week
            formatted_day = target_time.strftime(', %A\n')
            result_text.insert(tk.END, formatted_day)
        
        # Center-align the text
        result_text.tag_configure("center", justify="center")
        result_text.tag_add("center", "1.0", "end")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {str(e)}\nPlease try again.")

def calculate_custom_time():
    """
    Convert user-provided time to all predefined timezones.
    """
    try:
        # Get the user input time and AM/PM value
        input_time = time_entry.get().strip()
        am_pm = am_pm_var.get()
        input_timezone = selected_timezone.get()

        # Validate the input format
        if not input_time:
            raise ValueError("Time entry cannot be empty.")
        if len(input_time.replace(":", "")) < 3:
            raise ValueError("Incomplete time entry.")

        # Parse the input time
        time_format = "%I:%M %p"  # 12-hour format with AM/PM
        input_time_with_am_pm = f"{input_time} {am_pm}"
        parsed_time = datetime.strptime(input_time_with_am_pm, time_format)

        # Get today's date in the selected timezone
        local_tz = pytz.timezone(TIMEZONES[input_timezone])
        today = datetime.now(local_tz).date()

        # Combine today's date with the parsed time
        combined_datetime = datetime.combine(today, parsed_time.time())

        # Localize the combined datetime to the selected timezone
        localized_time = local_tz.localize(combined_datetime)

        # Clear the result area
        result_text.delete(1.0, tk.END)

        # Convert the time to all predefined timezones
        for location, tz_name in TIMEZONES.items():
            target_tz = pytz.timezone(tz_name)
            target_time = localized_time.astimezone(target_tz)
            
            # Insert location and colon
            result_text.insert(tk.END, f"{location}: ")
            
            # Insert time with bold tag
            formatted_time = target_time.strftime('%I:%M %p')
            result_text.insert(tk.END, f"{formatted_time}", "bold_time")
            
            # Insert day of the week
            formatted_day = target_time.strftime(', %A\n')
            result_text.insert(tk.END, formatted_day)
        
        # Center-align the text
        result_text.tag_configure("center", justify="center")
        result_text.tag_add("center", "1.0", "end")
    except ValueError as ve:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {str(ve)}\nPlease enter a valid time (e.g., 02:30).")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {str(e)}\nPlease try again.")

def on_time_entry_change(event):
    """
    Automatically insert a colon after two digits in the time entry field.
    """
    content = time_entry.get()
    # Remove any existing colons for processing
    digits = content.replace(":", "")
    if len(digits) == 2 and ":" not in content:
        time_entry.insert(2, ":")
    elif len(digits) > 4:
        # Prevent more than 4 digits (HH:MM)
        time_entry.delete(5, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Time Converter")
root.geometry("600x550")
root.configure(bg="#f0f4f7")  # Light blue background

# Define Fonts
bold_font = font.Font(family="Consolas", size=12, weight="bold")

# Title Label
title_label = tk.Label(
    root, text="Time Converter", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333"
)
title_label.pack(pady=10)

# Timezone Selection Frame
timezone_frame = tk.Frame(root, bg="#f0f4f7")
timezone_frame.pack(pady=5)

timezone_label = tk.Label(
    timezone_frame,
    text="Select Your Timezone:",
    font=("Arial", 12),
    bg="#f0f4f7",
    fg="#555",
)
timezone_label.pack(side=tk.TOP, pady=5)

# Calculate the maximum length of the timezone strings to set Combobox width
max_tz_length = max(len(tz) for tz in TIMEZONES.keys())
timezone_dropdown = ttk.Combobox(
    timezone_frame,
    textvariable=tk.StringVar(value="Denpasar, Bali, Indonesia"),
    values=list(TIMEZONES.keys()),
    font=("Arial", 11),
    state="readonly",
    width=max_tz_length
)
timezone_dropdown.pack(pady=5, padx=10)

selected_timezone = timezone_dropdown.cget("textvariable")
selected_timezone = tk.StringVar(value="Denpasar, Bali, Indonesia")
timezone_dropdown.configure(textvariable=selected_timezone)

# Custom Time Input Frame
time_input_frame = tk.Frame(root, bg="#f0f4f7")
time_input_frame.pack(pady=5)

time_label = tk.Label(
    time_input_frame,
    text="Enter Custom Time (hh:mm):",
    font=("Arial", 12),
    bg="#f0f4f7",
    fg="#555",
)
time_label.pack(side=tk.TOP, pady=5)

time_entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
time_entry.pack(pady=5)
time_entry.insert(0, "12:00")  # Default time

# Bind the key release event to auto-insert colon
time_entry.bind('<KeyRelease>', on_time_entry_change)

# AM/PM Dropdown Frame
ampm_frame = tk.Frame(root, bg="#f0f4f7")
ampm_frame.pack(pady=5)

am_pm_var = tk.StringVar(value="AM")
am_pm_label = tk.Label(
    ampm_frame,
    text="AM/PM:",
    font=("Arial", 12),
    bg="#f0f4f7",
    fg="#555",
)
am_pm_label.pack(side=tk.LEFT, padx=(0,5))

am_pm_dropdown = ttk.Combobox(
    ampm_frame, textvariable=am_pm_var, values=["AM", "PM"], font=("Arial", 11), state="readonly", width=5
)
am_pm_dropdown.pack(side=tk.LEFT)

# Center the AM/PM dropdown
ampm_frame.pack(anchor='center')

# Fetch Current Time Button
fetch_button = tk.Button(
    root,
    text="Fetch Current Time",
    font=("Arial", 12, "bold"),
    bg="#4caf50",  # Green color
    fg="white",
    activebackground="#45a049",
    relief="flat",
    command=fetch_current_time,
)
fetch_button.pack(pady=10)

# Calculate Custom Time Button
custom_time_button = tk.Button(
    root,
    text="Calculate Custom Time",
    font=("Arial", 12, "bold"),
    bg="#007BFF",  # Blue color
    fg="white",
    activebackground="#0056b3",
    relief="flat",
    command=calculate_custom_time,
)
custom_time_button.pack(pady=10)

# Results Label
results_label = tk.Label(
    root, text="Converted Times:", font=("Arial", 14, "bold"), bg="#f0f4f7", fg="#333"
)
results_label.pack(pady=10)

# Results Display (Text Area)
result_text = tk.Text(
    root,
    font=("Consolas", 12),
    height=12,
    width=60,
    bg="#ffffff",
    fg="#333",
    relief="solid",
    bd=1,
    wrap="word",
)
result_text.pack(pady=10, padx=20)

# Configure Tags
result_text.tag_configure("bold_time", font=bold_font)
result_text.tag_configure("center", justify="center")

# Run the GUI
root.mainloop()
