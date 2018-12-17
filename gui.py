import homepage
import settings
import schoolDetails
import multientry
import book2
import entry
import input as input1
import login

def homescreen():
	homepage.main()


def settings_menu():
	settings.main()
	homescreen()


def school_details():
	schoolDetails.start()
	homescreen()


def multi_entry():
	multientry.class3()
	homescreen()


def book_deets():
	entry.Form("isbn here:")
	homescreen()


def logins():
	login.main()
