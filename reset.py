import json, os, sys, keyboard, shutil

def reset(saves, render_distance):
	if not mc_open():
		return
	for i in range(32):
		keyboard.press_and_release('shift+f3+f')
	for i in range(render_distance - 2):
		keyboard.press_and_release('f3+f')
	keyboard.press_and_release('escape, shift+tab, enter')
	files = os.listdir(saves)
	files_filtered = list(filter(lambda file: os.path.isdir(os.path.join(saves, file)) and not file.startswith('_'), files))
	files_filtered.sort(key=lambda x: int(x[16:]))

	to_move = len(files_filtered) - 4
	if to_move < 1:
		return

	files_to_move = files_filtered[0:to_move]

	for file in files_to_move:
		folder = os.path.join(saves, file)
		try:
			shutil.move(saves + '/' + file, saves + '/_oldWorlds')
		except:
			print("Unable to move " + file)

def mc_open():
	if sys.platform == 'win32':
		import pygetwindow as gw
		return "Minecraft" in gw.getActiveWindow().title
	elif sys.platform == 'darwin':
		# can't be bothered at the moment
		return True
	elif sys.platform == 'linux':
		# don't know if this works and can't test it
		import Xlib
		disp = Xlib.display.Display()
		window = disp.get_input_focus().focus

		return "Minecraft" in window.get_wm_name()

if __name__ == "__main__":
	settings_file = open('settings.json')

	settings = json.load(settings_file)

	saves = settings['path'] + '/saves'
	if not os.path.exists(saves):
		print('Unable to locate saves directory')
		exit()
	old = saves + '/_oldWorlds'
	if not os.path.exists(old):
		os.makedirs(old)
		print('_oldWorlds folder created')

	render_distance = settings['render_distance']

	keyboard.add_hotkey(settings['reset_hotkey'], lambda: reset(saves, render_distance))
	keyboard.wait(settings['exit_hotkey'])
