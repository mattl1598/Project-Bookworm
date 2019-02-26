import json
import locations
import sql

def create_settings():
	blank_settings = {
		"database_location": "",
		"database_type": "file",
		"assets": "",
		"root_location": "",
		"theme": "dark",
		"last_user_id": ""
		}
	blank_settings["database_location"] = "C:\\ProgramData\\Project-Bookworm\\database\\database.db"
	blank_settings["database_type"] = "file"
	blank_settings["assets"] = "C:\\ProgramData\\Project-Bookworm\\assets\\"
	blank_settings["root_location"] = "C:\\ProgramData\\Project-Bookworm\\"

	with open(blank_settings["root_location"]+"settings.json", 'w') as outfile:
		json.dump(blank_settings, outfile)

def create_theme():
	blank_theme = {
		"theme": "dark",
		"dark": {
			"windows": {
				"background": "#474747",
				"darkbackground": "#2f2f2f",
				"highlightbackground": "#474747",
				"highlightcolor": "black",
				"text": "white"
			},
			"textbox": {
				"background": "#2f2f2f",
				"foreground": "white",
				"highlightbackground": "#d9d9d9",
				"highlightcolor": "black",
				"insertbackground": "#c4c4c4",
				"selectbackground": "#214283",
				"selectforeground": "black"
			},
			"button": {
				"background": "#474747",
				"text": "white",
				"clickedbg": "#2f2f2f"
			}
		},
		"light": {
			"windows": {
				"background": "#d9d9d9",
				"darkbackground": "#d9d9d9",
				"highlightbackground": "#d9d9d9",
				"highlightcolor": "black",
				"text": "black"
			},
			"textbox": {
				"background": "white",
				"foreground": "black",
				"highlightbackground": "#d9d9d9",
				"highlightcolor": "black",
				"insertbackground": "#c4c4c4",
				"selectbackground": "black",
				"selectforeground": "black"
			},
			"button": {
				"background": "#d9d9d9",
				"text": "black",
				"clickedbg": "#d9d9d9"
			}
		},
		"custom": {
			"windows": {
				"background": "SystemButtonFace",
				"darkbackground": "#2f2f2f",
				"highlightbackground": "#474747",
				"highlightcolor": "black",
				"text": "white"
			},
			"textbox": {
				"background": "#2f2f2f",
				"foreground": "white",
				"highlightbackground": "#d9d9d9",
				"highlightcolor": "black",
				"insertbackground": "#c4c4c4",
				"selectbackground": "#214283",
				"selectforeground": "black"
			},
			"button": {
				"background": "#474747",
				"text": "white",
				"clickedbg": "#2f2f2f"
			}
		}
	}

	with open("C:\\ProgramData\\Project-Bookworm\\theme.json", 'w') as outfile:
		json.dump(blank_theme, outfile)


if __name__ == "__main__":
	create_settings()
	create_theme()
