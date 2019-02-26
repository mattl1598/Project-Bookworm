import winshell
import json


def root():
	docs = winshell.my_documents()
	appdata = winshell.application_data()
	program = programs()

	doc_path = docs + "\\GitHub\\Project-Bookworm\\"
	app_path = appdata + "\\Project-Bookworm\\"
	public = "C:\\Users\\Public\\Programs\\Project-Bookworm\\"

	return public


def programs():
	return "C:\\ProgramData\\Project-Bookworm\\"


def app_data():
	appdata = winshell.application_data()
	app_path = appdata + "\\Project-Bookworm\\"

	return app_path


def icons():
	path = assets() + "icons"

	return path


def assets():
	setts = settings()

	with open(setts, "r") as file:
		setting = json.load(file)

	path = setting["assets"]

	return path


def docs():
	doc = winshell.my_documents()

	return doc

def theme():
	path = programs() + "theme.json"

	return path


def database():
	setts = settings()

	with open(setts, "r") as file:
		setting = json.load(file)

	path = setting["database_location"]

	return path


def settings():
	path = root() + "settings.json"

	return path
