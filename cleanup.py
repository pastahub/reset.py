import json, os, shutil, sys

if __name__ == "__main__":
	os.chdir(sys.path[0])
	settings_file = open('settings.json')

	settings = json.load(settings_file)

	saves = settings['path'] + '/saves'
	if not os.path.exists(saves):
		print('Unable to locate saves directory')
		exit()
	files = os.listdir(saves)
	files_filtered = list(filter(lambda file: os.path.isdir(os.path.join(saves, file)) and file.startswith('RandomSpeedrun #'), files))
	files_filtered.sort(key=lambda x: int(x[16:]))

	to_move = len(files_filtered) - 5
	if to_move < 1:
		exit()

	files_to_move = files_filtered[0:to_move]

	for file in files_to_move:
		try:
			shutil.rmtree(saves + '/' + file, saves + '/_oldWorlds')
		except:
			print("Unable to delete " + file)
