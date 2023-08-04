import os
import time
import subprocess

while True:
    os.system('python Main_Upbit.py')
    os.system('git add .')
    os.system('git commit -m "Update data"')
    os.system('git push')
    time.sleep(200)
    
    os.system('python Main_BinanceFuture.py')
    os.system('git add .')
    os.system('git commit -m "Update data"')
    os.system('git push')
    time.sleep(200)

    os.system('python Main_Bithumb.py')
    os.system('git add .')
    os.system('git commit -m "Update data"')
    os.system('git push')
    time.sleep(200)