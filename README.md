# Local-file-share-Raspberry-pi
# Raspberry Pi Local File Share Module

The Raspberry Pi Local File Share Module is a simple and efficient solution for creating a local file sharing system using a Raspberry Pi. This project leverages the Flask web framework to set up a web-based interface that allows users to upload, list, download, and delete files within a shared directory on the Raspberry Pi.

## Prerequisites

- A Raspberry Pi with Raspbian OS installed.
- Python 3 and Flask installed on your Raspberry Pi.
- A Bash script to run the Flask application and manage the shared directory.

## Installation and Setup

### Step 1: Install Flask

Ensure your Raspberry Pi is up-to-date and install Flask:

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-flask
