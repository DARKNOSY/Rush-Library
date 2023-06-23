# by me 

import platform
import locale
import getpass
import socket
import uuid
import re
import psutil
import ctypes
import datetime

def get_mac_address():
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac

def get_battery_info():
    battery = psutil.sensors_battery()
    percent = battery.percent if battery else "N/A"
    plugged = battery.power_plugged if battery else False
    return percent, plugged

def get_volume_percent():
    volume = ctypes.windll.winmm.waveOutGetVolume(None)
    percent = round((volume / 65535) * 100, 2)
    return percent

def get_pc_info():
    info = platform.uname()
    system = info.system
    release = info.release
    version = info.version
    machine = info.machine
    processor = info.processor
    language = locale.getlocale(locale.LC_CTYPE)[0]
    username = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    mac_address = get_mac_address()
    ram = psutil.virtual_memory().total
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    disk_usage = psutil.disk_usage("/")
    disk_percent = disk_usage.percent
    battery_percent, battery_plugged = get_battery_info()
    volume_percent = get_volume_percent()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info_message = f"System: {system}\n"
    info_message += f"Release: {release}\n"
    info_message += f"Version: {version}\n"
    info_message += f"Machine: {machine}\n"
    info_message += f"Processor: {processor}\n"
    info_message += f"Language: {language}\n"
    info_message += f"Username: {username}\n"
    info_message += f"PC Name: {hostname}\n"
    info_message += f"IP Address: {ip}\n"
    info_message += f"MAC Address: {mac_address}\n"
    info_message += f"CPU Usage: {cpu_percent}%\n"
    info_message += f"Memory Usage: {memory_percent}%\n"
    info_message += f"Disk Usage: {disk_percent}%\n"
    info_message += f"Battery Percentage: {battery_percent}% (Plugged in: {battery_plugged})\n"
    info_message += f"Volume Level: {volume_percent}%\n"
    info_message += f"RAM: {ram} bytes\n"
    info_message += f"Current Time: {current_time}"

    return info_message

pc_info = get_pc_info()
print(pc_info)
