# by me

import webbrowser

def open_website(url, tabs=1):
    for _ in range(tabs):
        webbrowser.open(url)
    print(f"Opened {tabs} tab(s) of {url} on the host computer.")

# Usage example
url = "https://www.example.com"  # Replace with the actual URL
tabs = 3  # Number of tabs to open (default: 1)
open_website(url, tabs)
