import tkinter as tk
from tkinter import messagebox

# Function to switch frames
def show_frame(frame):
    frame.tkraise()  # Brings the desired frame to the top

# Functionality for each screen
def start_port_scanner():
    messagebox.showinfo("Port Scanner", "Starting the Port Scanner!")

def start_ip_geolocator():
    messagebox.showinfo("IP Geolocator", "Starting the IP Geolocator!")

def start_combination():
    messagebox.showinfo("Combination", "Starting both tools!")

# Create the main application window
root = tk.Tk()
root.title("Cybersecurity Tools")
root.geometry("1280x720")  # Set to 720p resolution
root.configure(bg="#2C3E50")

# Use grid to manage frames for scene switching
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create frames for each scene
main_menu = tk.Frame(root, bg="#2C3E50")
port_scanner_screen = tk.Frame(root, bg="#1B4F72")
ip_geolocator_screen = tk.Frame(root, bg="#145A32")
combination_screen = tk.Frame(root, bg="#512E5F")

for frame in (main_menu, port_scanner_screen, ip_geolocator_screen, combination_screen):
    frame.grid(row=0, column=0, sticky="nsew")

# Main Menu Frame
tk.Label(
    main_menu,
    text="Cybersecurity Tools",
    font=("Arial", 55, "bold"),
    bg="#2C3E50",
    fg="white"
).pack(pady=40)

tk.Button(
    main_menu,
    text="Port Scanner",
    command=lambda: show_frame(port_scanner_screen),
    font=("Arial", 20),
    bg="#2980B9",
    fg="white",
    relief="raised",
    bd=3
).pack(pady=10, ipadx=10, ipady=5)

tk.Button(
    main_menu,
    text="IP Geolocator",
    command=lambda: show_frame(ip_geolocator_screen),
    font=("Arial", 20),
    bg="#27AE60",
    fg="white",
    relief="raised",
    bd=3
).pack(pady=10, ipadx=10, ipady=5)

tk.Button(
    main_menu,
    text="Both",
    command=lambda: show_frame(combination_screen),
    font=("Arial", 20),
    bg="#8E44AD",
    fg="white",
    relief="raised",
    bd=3
).pack(pady=10, ipadx=10, ipady=5)

# Port Scanner Frame
# Update the title
tk.Label(
    port_scanner_screen,
    text="Port Scanner",
    font=("Arial", 40, "bold"),  # Updated font size
    bg="#1B4F72",
    fg="white"
).pack(pady=40)  # Increased padding

# Add a textbox for IP input
tk.Entry(
    port_scanner_screen,
    font=("Arial", 18),  # Adjusted font size for larger window
    width=40
).pack(pady=10)

# Add a note below the textbox
tk.Label(
    port_scanner_screen,
    text="Note: Enter a single IP or a comma-separated list of IPs.",
    font=("Arial", 14),  # Smaller font for the note
    bg="#1B4F72",
    fg="white"
).pack(pady=10)


# Update the checkbox and buttons
tk.Checkbutton(
    port_scanner_screen,
    text="Scan multiple IPs",
    font=("Arial", 18),  # Updated font size
    bg="#1B4F72",
    fg="white"
).pack(pady=10)

tk.Button(
    port_scanner_screen,
    text="Start Scan",
    command=start_port_scanner,
    font=("Arial", 20),  # Updated font size
    bg="#2980B9",
    fg="white"
).pack(pady=20, ipadx=10, ipady=10)  # Increased padding

tk.Button(
    port_scanner_screen,
    text="Back to Menu",
    command=lambda: show_frame(main_menu),
    font=("Arial", 18),  # Updated font size
    bg="#C0392B",
    fg="white"
).pack(pady=10, ipadx=10, ipady=5)
# Update the title

#IP Geolocator Frame
tk.Label(
    ip_geolocator_screen,
    text="IP Geolocator",
    font=("Arial", 40, "bold"),  # Updated font size
    bg="#145A32",
    fg="white"
).pack(pady=40)  # Increased padding

# Add a textbox for IP input
tk.Entry(
    ip_geolocator_screen,
    font=("Arial", 18),
    width=40
).pack(pady=10)

# Add a note below the textbox
tk.Label(
    ip_geolocator_screen,
    text="Note: Enter the IP address you want to geolocate.",
    font=("Arial", 14),
    bg="#145A32",
    fg="white"
).pack(pady=10)


# Update the buttons
tk.Button(
    ip_geolocator_screen,
    text="Start Geolocation",
    command=start_ip_geolocator,
    font=("Arial", 20),  # Updated font size
    bg="#27AE60",
    fg="white"
).pack(pady=20, ipadx=10, ipady=10)  # Increased padding

tk.Button(
    ip_geolocator_screen,
    text="Back to Menu",
    command=lambda: show_frame(main_menu),
    font=("Arial", 18),  # Updated font size
    bg="#C0392B",
    fg="white"
).pack(pady=10, ipadx=10, ipady=5)

# Both Frame
tk.Label(
    combination_screen,
    text="Port Scanner + IP Geolocator",
    font=("Arial", 40, "bold"),  # Updated font size
    bg="#512E5F",
    fg="white"
).pack(pady=40)  # Increased padding
# Add a textbox for IP input
tk.Entry(
    combination_screen,
    font=("Arial", 18),
    width=40
).pack(pady=10)

# Add a note below the textbox
tk.Label(
    combination_screen,
    text="Note: Enter an IP address to scan and geolocate.",
    font=("Arial", 14),
    bg="#512E5F",
    fg="white"
).pack(pady=10)


# Update the buttons
tk.Button(
    combination_screen,
    text="Start Both",
    command=start_combination,
    font=("Arial", 20),  # Updated font size
    bg="#8E44AD",
    fg="white"
).pack(pady=20, ipadx=10, ipady=10)  # Increased padding

tk.Button(
    combination_screen,
    text="Back to Menu",
    command=lambda: show_frame(main_menu),
    font=("Arial", 18),  # Updated font size
    bg="#C0392B",
    fg="white"
).pack(pady=10, ipadx=10, ipady=5)


# Show the main menu initially
show_frame(main_menu)

# Run the main loop
root.mainloop()
