import os
import time
import subprocess

while True:
    # os.system('ExecutionScript.py')
    subprocess.run(['python', 'ExecutionScript.py'])
    time.sleep(20)
    os.system('git add .')
    os.system('git commit -m "Update data"')
    os.system('git push')
    time.sleep(1800)