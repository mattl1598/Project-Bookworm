import winshell
import json


def root():
	docs = winshell.my_documents()
	appdata = winshell.application_data()

	doc_path = docs + "\\GitHub\\Project-Bookworm"
	app_path = appdata + "\\Project-Bookworm"

	return doc_path


def icons():
	path = root() + "\\assets\\icons\\"

	return path


def theme():
	path = root() + "\\theme.json"

	return path


def database():
	setts = settings()

	with open(setts, "r") as file:
		setting = json.load(file)

	path = setting["database_location"]

	return path


def settings():
	path = root() + "\\settings.json"

	return path
