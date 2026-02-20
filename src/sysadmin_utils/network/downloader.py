import urllib.request
import urllib.error
from pathlib import Path

def download_file(url: str, filename: str):
    """
    Downloads a file from a URL.
    """
    print(f"Downloading from {url}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error downloading file: {e}")


