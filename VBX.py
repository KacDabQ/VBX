import subprocess
import os
import threading

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

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

prPurple(logo)

prYellow('We suggest you not opening this if you dont know what it is. Warned ya!')

howMuch = int(input(('<<(HOWMUCHVBS)>>: ')))

###

current_directory = os.path.dirname(os.path.realpath(__file__))

vbs_file = "vbxdestroyer.vbs"

vbs_path = os.path.join(current_directory, vbs_file)

def run_vbs():
    subprocess.call(['cscript', vbs_path])

threads = []
for _ in range(howMuch):
    thread = threading.Thread(target=run_vbs)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()