import bpy
import time
import os
import subprocess

# Replace 'YOUR_CLIENT_ID' with your actual Discord application's Client ID
CLIENT_ID = 'YOUR_CLIENT_ID'
RPC = None  # Placeholder for Presence object

# Function to check if pypresence is installed
def is_pypresence_installed():
    try:
        import pypresence
        return True
    except ImportError:
        return False

# Function to install pypresence
def install_pypresence():
    try:
        subprocess.run(["pip", "install", "pypresence"], check=True)
        print("pypresence installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install pypresence. Please install it manually.")

# Function to initialize Discord Rich Presence
def init_discord_rich_presence():
    global RPC
    try:
        from pypresence import Presence
        RPC = Presence(client_id=CLIENT_ID)
        RPC.connect()
    except ImportError:
        print("pypresence not found. Installing...")
        install_pypresence()
        init_discord_rich_presence()

# Function to get project information
def get_project_info():
    project_name = bpy.path.basename(bpy.context.blend_data.filepath)
    asset_count = len(bpy.data.objects)
    asset_number = bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else 'N/A'
    return project_name, asset_count, asset_number

# Function to update Discord Rich Presence
def update_presence():
    project_name, asset_count, asset_number = get_project_info()

    presence_data = {
        'details': f'Working on {project_name}',
        'state': f'Asset {asset_number} of {asset_count}',
        'large_image': 'blender_logo',
        'small_image': 'asset_icon',
        'large_text': 'Blender Project',
        'small_text': 'Asset Details',
        'instance': False
    }

    RPC.update(**presence_data)

# Main loop to continuously update presence
try:
    init_discord_rich_presence()  # Initialize Discord Rich Presence

    while True:
        update_presence()
        time.sleep(15)  # Update every 15 seconds

except KeyboardInterrupt:
    if RPC:
        RPC.close()
