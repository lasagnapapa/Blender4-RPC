## Discord Rich Presence for Blender 4.0

### Get Started

This is a simple script to add a Discord RPC to Blender using Blender's Python API (.bpy). This python script is not to be executed through python seperately, I simply used the .py filetype to edit the code in Visual Studio confidently. To use this code, you must go in to Blender's "Scripting" tab, open a NEW text data-block, and enter the script there before running it.

- Here is a link to the raw code where you can just copy the script:
- ~ https://github.com/lasagnapapa/Blender4-RPC/raw/main/blender4-rpc.py

### NOTICE:

Before executing the script within Blender, you must edit line (7) and replace 'YOUR_CLIENT_ID' with the Client ID for your Discord applet.

If you do not have a Discord applet, you can make one by following these steps:
- Go to https://discord.com/developers/
- Click on "New Application"
- Name your new application "Blender 4.0", or simply "Blender"
- After making your new application navigate to "General Information"
- Copy the "Application ID" (client ID), and paste it where "'YOUR_CLIENT_ID'" was

### Note:
You must have pypresence installed prior to executing this command:
- **pip** install pypresence

### Customization
To customize the Discord Rich Presence (RPC) with things like custom images you can add them to your application on Discord:
- Navigate to https://discord.com/developers/applications/
- Open your application and navigate to the "Rich Presence" tab
- Add "blender_logo" and "asset_icon" to the "Rich Presence Assets" tab
- ~ You can find both images I recommend here: https://github.com/lasagnapapa/Blender4-RPC/tree/main/Assets

It should look as follows:

![image](https://github.com/lasagnapapa/Blender4-RPC/assets/68775205/c522dd07-3f2b-4fb2-9ccc-6534862c67c2)

### Finishing Up
Feel free to edit the code however you want, including adding more assets and keys. But otherwise, you're all done!

Your finished presence should look like this:

![image](https://github.com/lasagnapapa/Blender4-RPC/assets/68775205/4e8b5ead-a74f-4ad6-aad5-74eb0e496b5c)

### Changelog: (1/26/2024)

Added "Time Elapse" Counter:

![Screenshot 2024-01-26 093241](https://github.com/lasagnapapa/Blender4-RPC/assets/68775205/e4603815-a048-4aa1-b1a1-bcd938161af2)
