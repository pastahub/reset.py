# reset.py
A single instance reset macro that (hopefully) works for every os. (If you use Mac or Linux please tell me if this works by messaging me on discord @pasta#3635)

## Setup
For all platforms keyboard is required. It can be installed with `pip3 install keyboard`.<br/>
On windows pygetwindow is required in order to detect the title of the active window. It can be installed with `pip3 install pygetwindow`<br/>
Active window title detection has not been added for mac yet.<br/>
On linux Xlib is required. It can be installed with `pip3 install python3-xlib`<br/>
Also make sure that settings.json is in the same directory as reset.py and that each option is correct.<br/>
You also need to have atum and fast reset installed for Minecraf, both of which can be found [here](https://www.minecraftspeedrunning.com/public-resources/mods).<br/>
Then just run reset.py and start resetting.

## Settings:

### reset_hotkey
The hotkey to reset the game. Use '+' to add multiple keys, such as `ctrl+u`.

### exit_hotkey
The hotkey which stops the macro. Same formatting as reset_hotkey.

### path
The path to your .minecraft folder.
