# -------------------------------------------------------------------------------------------------------------

# 													COMMANDS:

	# ~ google search ~ To Do A Google Search
	# ~ weather ~ To Show A Weather Report Of A State
	# ~ wikipedia ~ To Get Information From Wikipedia
	# ~ Open Github | Open StackOverFlow | Open Youtube | Open Google ~ To open these websites on ur default browser
	# ~ Start Sublime ~ It will start sublime text
	# ~ Start Chrome ~ It will start chrome
	# ~ Quote ~ It would generate a quote for you
	# ~ Time ~ It will show you the current time and date
	# ~ Quit ~ Quit's the script

# -------------------------------------------------------------------------------------------------------------

import pyttsx3 # pip install pyttsx3
import os
import datetime
import time
import wikipedia as wk # pip install wikipedia
import webbrowser
import requests # pip install requests
from googlesearch import search # pip install google

# ---------------------------------------------------------------------------------
# Speech Engine
speechEngine = pyttsx3.init()
speaker = speechEngine.getProperty('voice')
speechEngine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

def Say(speech): 
	speechEngine.say(speech)
	speechEngine.runAndWait()
# ----------------------------------------------------------------------------------

def greet(): # To Greet User According To Time
	dt = int(datetime.datetime.now().hour)
	if dt>=0 and dt<12:
		Say(f'Good Morning {name}')
	elif dt>=12 and dt<18:
		Say(f'Good Afternoon {name}')
	else:
		Say(f'Good Evening {name}')


def weatherReports(): # Tells you the weather of your city
	# https://openweathermap.org/ checkout this link for more details on this
	try:
		api_key = '' # Put your own access key/api key
		# Get your API key from https://openweathermap.org/
		Say('Sir, Please enter your city name')
		city = input('City Name: ')
		url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
		responseWeather = requests.get(url)
		if responseWeather.status_code == 200:
			reports = responseWeather.json()
			# Filtering Result
			main = reports['main']
			weather = reports['weather']
			mintemp = main['temp_min']
			max_temp = main['temp_max']
			celmax = int(max_temp) - 273.15 # Converting Kelvin to Celcius
			celmin = int(mintemp) - 273.15 # Converting Kelvin to Celcius
			print(f"The Minimum Temperature at {city} is {int(celmin)} °C")
			print(f"The Maximum Temperature at {city} is {int(celmax)} °C")
			print(f"The Weather Report Is: {weather[0]['description']}")
			Say(f"The Minimum Temperature at {city} is {int(celmin)} °Celcius")
			Say(f"The Maximum Temperature at {city} is {int(celmax)} °Celcius")
			Say(f"The Weather Report Is: {weather[0]['description']}")

		else:
			print('Sorry cannot get you the weather report please try again after sometime')
			Say('Sorry cannot get you the weather report please try again after sometime')

	except Exception as e:
		print(f'Sorry {name} cannot complete your request please check your connection and try after sometime')
		Say(f'Sorry {name} cannot complete your request please check your connection and try after sometime')


def weblink(link): # Opens links on your default browser passed through this function
	try:
		webbrowser.open(link)
	except Exception as e:
		print('Cannot open the link please check your default browser')
		Say('Cannot open the link please check your default browser')


def openfile(path): # Opens Software / Files when a location address is passed through the function
	try:
		filepath = path # Path of software
		os.startfile(filepath)
	except Exception as e:
		print('Cannot Locate The File')
		Say('Cannot Locate The File')


if __name__ == '__main__':
	Say('Hello, I am Zira Version 1.0, I am your Virtual Assistant')
	Say('Enter your name')
	name = input('Enter your name: ') # Input: Name
	greet()
	Say('How May I Help You?')

	while True: # This will loop infinite times
		command = input('How May I Help You? ').lower() # Input: Command
		
		if 'python' in command: # Opens Python IDLE
			try:
				Say('Opening Python I D L E')
				interpreterPath = "C:\\Users\\priyanshu\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw" # IDLE Path
				os.startfile(interpreterPath)
			except Exception as e:
				print(f'Sorry {name} cannot complete your request please check your file location and try after sometime')
				Say(f'Sorry {name} cannot complete your request please check your file location and try after sometime')

		elif 'google search' in command: # For Searching On Web
			try:
				searchWeb = input('Search Web: ')
				for j in search(searchWeb, tld="co.in", num=10, stop=10, pause=2):
					print(j)
			except Exception as e:
				print(f'Sorry {name} cannot complete your request please check your connection and try after sometime')
				Say(f'Sorry {name} cannot complete your request please check your connection and try after sometime')

		elif 'time' in command: # Tells u the time & date
			try:
				dt = datetime.datetime.now()
				Say(f'The Date And Time Is {dt}')
				print(f'The Date And Time Is {dt}')
			except Exception as e:
				print('An Error Occured While Showing The Date And Time')
				Say('An Error Occured While Showing The Date And Time')

		elif 'weather' in command:
			Say('Getting You The Weather Reports......')
			weatherReports()

		elif 'open youtube' in command: # Opens YouTube
			Say('Opening YouTube.....')
			weblink('https://youtube.com/')

		elif 'open google' in command: # Opens Google
			Say('Opening Google.....')
			weblink('https://google.com/')

		elif 'open github' in command: # Opens GitHub
			Say('Opening GitHub.....')
			weblink('https://github.com/')

		elif 'open stackoverflow' in command: # Opens Stack Over Flow
			Say('Opening StackOverFlow.....')
			weblink('https://stackoverflow.com/')

		elif 'wikipedia' in command: # Searches on wikipedia
			try:
				searchQuery = input('Search: ').lower()
				sentences = int(input('Enter No. Of Sentences To Print: '))
				print('-'*80,'\n')
				result = wk.summary(searchQuery, sentences=sentences)
				print(f'Search: {searchQuery}')
				print(f'Wikipedia Result:- {result}')
				Say(result)
			except Exception as e:
				print(f'Sorry {name} cannot complete your request please check your connection and try after sometime')
				Say(f'Sorry {name} cannot complete your request please check your connection and try after sometime')

		elif 'start chrome' in command: # Opens/Starts Chrome | Can change it according to ur browser
			Say('Starting Chrome......')
			openfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

		elif 'start sublime' in command: # Opens/Starts Sublime | Change it according to your IDE/Source Code Editor
			Say('Starting Sublime Text......')
			openfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")

		elif 'quote' in command: # Gives you random quote from Quotables Database
			try:
				Say('Getting You A Quote')
				url = 'https://api.quotable.io/random'
				parameters = {'content' : 'famous-quotes'}
				response = requests.get(url, params=parameters)
				if response.status_code == 200:
					quotes = response.json()
					print(quotes['content'])
					Say(quotes['content'])
					print(quotes['author'])
					Say(f"By: {quotes['author']}")
				else:
					print("Sorry! Cannot get you a quote right now Please try again after sometime")
			except Exception as e:
				print(f'Sorry {name} cannot complete your request please check your connection and try after sometime')
				Say(f'Sorry {name} cannot complete your request please check your connection and try after sometime')

		elif 'code' in command: # Opens Visual Studio Code
			Say('Starting Visual Studio Code')
			openfile("C:\\Users\\priyanshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
			
		elif 'quit' in command: # Quits the script
			Say('Happy To Help You, See You Again')
			quit()

		else:
			Say('Sorry I can\'t understand you' )
