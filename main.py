import tkinter as tk
from tkinter import messagebox
import socket
import requests
import threading
import re
import webbrowser

# Function to check the type of IP
def checkIPType(ip_type, ip):
    if ip_type == "4":  # Check IPv4
        return checkIPv4Address(ip)
    elif ip_type == "6":  # Check IPv6
        return checkIPv6Address(ip)
    else:
        return False

def checkIPv4Address(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
        if part != "0" and part.startswith("0"):
            return False
    return True

def checkIPv6Address(ip):
    ipv6_pattern = re.compile(r"""
        ^                                     # Start of string
        ([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$   # Full IPv6 format
    """, re.VERBOSE)
    return bool(ipv6_pattern.match(ip))

# Function to get geolocation data for an IP
def get_geolocation_data(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        geo_data = response.json()
        loc = geo_data.get('loc', '')
        lat, lon = loc.split(',') if loc else (None, None)
        return {
            'ip': geo_data.get('ip'),
            'city': geo_data.get('city'),
            'region': geo_data.get('region'),
            'country': geo_data.get('country'),
            'lat': lat,
            'lon': lon,
            'isp': geo_data.get('org')
        }
    except Exception as e:
        print(f"Error fetching geolocation data: {e}")
        return None

# Port scanner logic
def scan_ports(ip, start_port, end_port):
    open_ports = []
    def scan(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip, port))
                open_ports.append(port)
        except:
            pass

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

# Functionality for Port Scanner
def start_port_scanner(ip):
    start_port = 1
    end_port = 1024
    if checkIPType("4", ip) or checkIPType("6", ip):
        open_ports = scan_ports(ip, start_port, end_port)
        if open_ports:
            messagebox.showinfo("Port Scan Result", f"Open Ports: {open_ports}")
        else:
            messagebox.showinfo("Port Scan Result", "No open ports found.")
    else:
        messagebox.showerror("Input Error", "Invalid IP address. Please enter a valid IP.")

# Functionality for IP Geolocator
def start_ip_geolocator(ip):
    if checkIPType("4", ip) or checkIPType("6", ip):
        geo_data = get_geolocation_data(ip)
        if geo_data:
            result = (
                f"IP: {geo_data['ip']}\n"
                f"Country: {geo_data['country']}\n"
                f"Region: {geo_data['region']}\n"
                f"City: {geo_data['city']}\n"
                f"ISP: {geo_data['isp']}\n"
                f"Latitude: {geo_data['lat']}\n"
                f"Longitude: {geo_data['lon']}\n"
                f"Google Maps Link: "
            )
            maps_link = f"https://www.google.com/maps?q={geo_data['lat']},{geo_data['lon']}"
            # Prompt user to open link
            if messagebox.askyesno("Geolocation Result", result + "Open Google Maps?"):
                webbrowser.open(maps_link)
        else:
            messagebox.showerror("Geolocation Error", "Failed to retrieve geolocation data.")
    else:
        messagebox.showerror("Input Error", "Invalid IP address. Please enter a valid IP.")

# Functionality for combination
def start_combination(ip):
    start_ip_geolocator(ip)
    start_port_scanner(ip)

# Create the main application window
root = tk.Tk()
root.title("Cybersecurity Tools")
root.geometry("1280x720")
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

# Helper function to switch frames
def show_frame(frame):
    frame.tkraise()

# Add consistent styles
def styled_button(master, text, command, bg_color):
    return tk.Button(
        master,
        text=text,
        command=command,
        font=("Arial", 20),
        bg=bg_color,
        fg="white",
        relief="raised",
        bd=3
    )

# Main Menu Frame
tk.Label(main_menu, text="Cybersecurity Tools", font=("Arial", 55, "bold"), bg="#2C3E50", fg="white").pack(pady=40)

styled_button(main_menu, "Port Scanner", lambda: show_frame(port_scanner_screen), "#2980B9").pack(pady=10, ipadx=10, ipady=5)
styled_button(main_menu, "IP Geolocator", lambda: show_frame(ip_geolocator_screen), "#27AE60").pack(pady=10, ipadx=10, ipady=5)
styled_button(main_menu, "Both", lambda: show_frame(combination_screen), "#8E44AD").pack(pady=10, ipadx=10, ipady=5)
styled_button(main_menu, "Exit", root.destroy, "#E74C3C").pack(pady=20, ipadx=10, ipady=5)

# Individual Frames
def setup_screen(frame, title, ip_var, action, color):
    tk.Label(frame, text=title, font=("Arial", 40, "bold"), bg=color, fg="white").pack(pady=40)
    tk.Entry(frame, textvariable=ip_var, font=("Arial", 18), width=40).pack(pady=10)
    styled_button(frame, "Start", lambda: action(ip_var.get()), "#27AE60").pack(pady=20, ipadx=10, ipady=10)
    styled_button(frame, "Back to Menu", lambda: show_frame(main_menu), "#C0392B").pack(pady=10, ipadx=10, ipady=5)

scanner_ip = tk.StringVar()
geolocator_ip = tk.StringVar()
combination_ip = tk.StringVar()

setup_screen(port_scanner_screen, "Port Scanner", scanner_ip, start_port_scanner, "#1B4F72")
setup_screen(ip_geolocator_screen, "IP Geolocator", geolocator_ip, start_ip_geolocator, "#145A32")
setup_screen(combination_screen, "Port Scanner + IP Geolocator", combination_ip, start_combination, "#512E5F")

# Show the main menu initially
show_frame(main_menu)

# Run the main loop
root.mainloop()
