import os
import time
import subprocess

while True:
    subprocess.run(['python3', 'Update_InputExcel.py'])
    time.sleep(2)
    subprocess.run(['python3', 'Update_OutputExcel_and_HTML.py'])
    time.sleep(2)
    os.system('git add .')
    os.system('git commit -m "Update data"')
    os.system('git push')
    time.sleep(1800)