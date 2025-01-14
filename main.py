import tkinter as tk
from tkinter import messagebox, Toplevel, scrolledtext
import socket
import requests
import threading
import re
import webbrowser
from queue import Queue  # For thread-safe queue
from saveResults import save_geolocation_results, save_scan_results

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

# Port scanner logic using a Queue for thread-safe results
def scan_ports(ip, start_port, end_port):
    open_ports = []
    queue = Queue()

    def scan(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))  # Returns 0 if successful
                if result == 0:  # If port is open
                    queue.put(port)
        except socket.error:
            pass

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Collect results from the queue
    while not queue.empty():
        open_ports.append(queue.get())

    return open_ports

# Functionality for Port Scanner
def start_port_scanner(ip):
    start_port = 1
    end_port = 65535
    if checkIPType("4", ip) or checkIPType("6", ip):
        open_ports = scan_ports(ip, start_port, end_port)
        if open_ports:
            messagebox.showinfo("Port Scan Result", f"Open Ports: {open_ports}")
            save_prompt = messagebox.askyesno("Save Results", "Do you want to save the port scan results?")
            if save_prompt:
                save_scan_results({"open": open_ports}, "TCP", ip)  # Save to scan_results.txt

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
            if messagebox.askyesno("Geolocation Result", result + "Open Google Maps?"):
                webbrowser.open(maps_link)
            save_prompt = messagebox.askyesno("Save Results", "Do you want to save the geolocation results?")
            if save_prompt:
                save_geolocation_results(geo_data)  # Save to geolocation_results.txt
        else:
            messagebox.showerror("Geolocation Error", "Failed to retrieve geolocation data.")
    else:
        messagebox.showerror("Input Error", "Invalid IP address. Please enter a valid IP.")

# Function to run both functionalities
def start_combination(ip):
    start_ip_geolocator(ip)
    start_port_scanner(ip)

# Function to view history
def view_history():
    history_window = Toplevel(root)
    history_window.title("History Viewer")
    history_window.geometry("800x600")

    text_area = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    try:
        with open("scan_history.txt", "r") as scan_file:
            text_area.insert(tk.END, "Scan History:\n")
            text_area.insert(tk.END, scan_file.read())

        with open("geolocation_history.txt", "r") as geo_file:
            text_area.insert(tk.END, "\nGeolocation History:\n")
            text_area.insert(tk.END, geo_file.read())
    except FileNotFoundError:
        text_area.insert(tk.END, "No history files found.\n")
    except Exception as e:
        text_area.insert(tk.END, f"Error reading history: {e}\n")

    text_area.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("Cybersecurity Tools")
root.geometry("1280x720")
root.configure(bg="#2C3E50")

# Input field for user IP entry
ip_entry = tk.StringVar()

tk.Label(root, text="Enter IP Address:", font=("Arial", 18), bg="#2C3E50", fg="white").pack(pady=10)
tk.Entry(root, textvariable=ip_entry, font=("Arial", 18), width=40).pack(pady=10)

# Main Menu
tk.Label(root, text="Cybersecurity Tools", font=("Arial", 55, "bold"), bg="#2C3E50", fg="white").pack(pady=40)
tk.Button(root, text="Port Scanner", command=lambda: start_port_scanner(ip_entry.get()), font=("Arial", 20), bg="#2980B9", fg="white").pack(pady=10)
tk.Button(root, text="IP Geolocator", command=lambda: start_ip_geolocator(ip_entry.get()), font=("Arial", 20), bg="#27AE60", fg="white").pack(pady=10)
tk.Button(root, text="Both", command=lambda: start_combination(ip_entry.get()), font=("Arial", 20), bg="#8E44AD", fg="white").pack(pady=10)
tk.Button(root, text="View History", command=view_history, font=("Arial", 20), bg="#9B59B6", fg="white").pack(pady=10)
tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 20), bg="#E74C3C", fg="white").pack(pady=10)

# Run the application
root.mainloop()