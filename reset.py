import json, os, keyboard, shutil

def reset(saves):
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

	keyboard.add_hotkey(settings['reset_hotkey'], lambda: reset(saves))
	keyboard.wait(settings['exit_hotkey'])
