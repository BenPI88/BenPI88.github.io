import base64
installdirectory = input("Where to install? Ex. C:/Users/Benji/Documents/dvdscreensaver/ (MAKE SURE THIS IS A VALID DIRECTORY) ")
if not installdirectory[len(installdirectory) - 1] == "/":
    installdirectory = installdirectory + "/"
print("Customizing Scripts...")
oldlogo = """       












                  
      ████████████████████       █████████████████     
      ████████████████████      ████████████████████   
     ██████     ███████████   ████████████     ██████  
     █████      ██████ ████  █████  █████      ██████  
     █████     ██████  █████████    █████     ██████   
    ███████████████     ███████    ███████████████     
    ██████████           ████      ███████████         
                         ██                            
               ██████████████████████                  
    ████████ ██ ██ ███ █ ████ ██████ █ ██████████      
  ███████████ ████ ███ ██ ███ █████ ███ ██████████     
        ████████████████████████████████████
"""
logo = """

                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
      @@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@     
      @@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@   
     @@@@@@     @@@@@@@@@@@   @@@@@@@@@@@@     @@@@@@  
     @@@@@      @@@@@@ @@@@  @@@@@  @@@@@      @@@@@@  
     @@@@@     @@@@@@  @@@@@@@@@    @@@@@     @@@@@@   
    @@@@@@@@@@@@@@@     @@@@@@@    @@@@@@@@@@@@@@@     
    @@@@@@@@@@           @@@@      @@@@@@@@@@@         
                         @@                            
               @@@@@@@@@@@@@@@@@@@@@@                  
    @@@@@@@@ @@ @@ @@@ @ @@@@ @@@@@@ @ @@@@@@@@@@      
  @@@@@@@@@@@ @@@@ @@@ @@ @@@ @@@@@ @@@ @@@@@@@@@@     
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
banana3 = f"""import os
import pyautogui
import time
from colorama import Fore
from colorama import just_fix_windows_console
import dvdscraddons
just_fix_windows_console()
m = 0
x = 50
m2 = 0
y = 0
speed = 0.1
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
currentcolor = colors[0]
colorid = 0
logo = """ + """dvdscraddons.logo
def logorefresh():
	print(f'{currentcolor}{logo}{Fore.RESET}')
logorefresh()
lr = 0
#os.system('start cmd.exe /c "curl parrot.live"')
wx, wy = pyautogui.getActiveWindow().size
imx, imy = pyautogui.position()
while True:
	mx, my = pyautogui.position()
	if not mx == imx or not my == imy:
		pyautogui.getActiveWindow().close()
	lr += 1
	if lr == 10000:
		lr = 0
		logorefresh()
	try:
		pyautogui.getActiveWindow().size = (600, 400)
	except AttributeError:
		print("oh noes")
	sx, sy = pyautogui.size()
	wxbackup = wx
	wybackup = wy
	backup = 0
	try:
		wx, wy = pyautogui.getActiveWindow().size
	except AttributeError:
		wx = wxbackup
		wy = wybackup
		backup = 1
	if m == 0:
		x += speed
	else:
		x -= speed
	if m2 == 0:
		y += speed
	else:
		y -= speed
	if backup == 0:
		try:
			pyautogui.getActiveWindow().moveTo(round(x) - 10, round(y))
		except NameError:
			print("oh noes")
		except AttributeError:
			print("oh noes")
	if (x - 10) + wx > sx or (x - 10) < 0:
		colorid += 1
		lr = 9999
		if m == 0:
			m = 1
		else:
			m = 0
	if y + wy > sy or y < 0:
		colorid += 1
		lr = 9999
		if m2 == 0:
			m2 = 1
		else:
			m2 = 0
	if colorid == len(colors):
		colorid = 0
	currentcolor = colors[colorid]"""
bananarunner = """import os
import pyautogui
import time
itime = 60
while True:
	timer = itime
	imx, imy = pyautogui.position()
	while not timer == 0:
		mx, my = pyautogui.position()
		if mx == imx and my == imy:
			timer -= 1
			print(timer)
			time.sleep(1)
		else:
			timer = itime
			mx, my = pyautogui.position()
			imx, imy = pyautogui.position()
			time.sleep(1)
""" + f"""
	os.system('start cmd.exe /c "python3 {installdirectory}bananalaunch.py"')
	mx, my = pyautogui.position()
	imx, imy = pyautogui.position()
	while imx == mx and imy == my:
		mx, my = pyautogui.position()"""
bananalaunch = f"""import os
import pyautogui
import time
os.system('start cmd.exe /c "python3 {installdirectory}bananabackground.py"')
time.sleep(1)
#pyautogui.getActiveWindow().moveTo(-20, -10)
#pyautogui.getActiveWindow().size = (50000, 50000)
pyautogui.getActiveWindow().maximize()
os.system('start cmd.exe /c "python3 {installdirectory}banana3.py"')"""
bananabackground = """import os
import pyautogui
imx, imy = pyautogui.position()
mx, my = pyautogui.position()
while mx == imx and my == imy:
	mx, my = pyautogui.position()"""
print("Installing...")
b3 = open(f"{installdirectory}banana3.py", "a")
b3.close()
b3 = open(f"{installdirectory}banana3.py", "w")
b3.write(banana3)
print("Installed banana3.py!")
bb = open(f"{installdirectory}bananabackground.py", "a")
bb.close()
bb = open(f"{installdirectory}bananabackground.py", "w")
bb.write(bananabackground)
print("Installed bananabackground.py!")
bl = open(f"{installdirectory}bananalaunch.py", "a")
bl.close()
bl = open(f"{installdirectory}bananalaunch.py", "w")
bl.write(bananalaunch)
print("Installed bananalaunch.py!")
br = open(f"{installdirectory}bananarunner.py", "a")
br.close()
br = open(f"{installdirectory}bananarunner.py", "w")
br.write(bananarunner)
print("Installed bananarunner.py!")
b3.close()
bb.close()
bl.close()
br.close()
import os
print("Installing dependencies...")
os.system("pip3 install pyautogui")
print("Pyautogui installed!")
os.system("pip3 install colorama")
print("Colorama installed!")
print("Adding Addon Support...")
addonsupport = open(f"{installdirectory}dvdscraddons.py", "a")
addonsupport.close()
addonsupport = open(f"{installdirectory}dvdscraddons.py", "w")
addonsupport.write(f'logo = """{logo}"""')
addonsupport.close()
print("DVDScreensaver installed! Would you like to launch it? (y/n)")
launchopt = input("")
if launchopt == "y":
    os.system(f"""start cmd.exe /c "python3 {installdirectory}bananarunner.py" """)