import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')  # Format for hours:minutes:seconds AM/PM
    current_date = strftime('%A, %d %B %Y')  # Format for Day, Date Month Year
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  # Update every 1 second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure the clock display
time_label = tk.Label(root, font=('Helvetica', 48), fg='blue')
time_label.pack(pady=20)

date_label = tk.Label(root, font=('Helvetica', 24), fg='green')
date_label.pack(pady=10)

# Call the function to update time
update_time()

# Run the application
root.mainloop()
