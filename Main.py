import os
import time

while True:
    os.system('ExecutionScript.py')
    os.system('git add .')
    os.system('git commit -m "Update data"')
    os.system('git push')
    time.sleep(900)