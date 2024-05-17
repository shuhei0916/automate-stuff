import time, subprocess

time_left = 10
while time_left > 0:
    print(time_left, end='', flush=True)
    time.sleep(1)
    time_left =  time_left - 1
    
# TODO: カウントダウン後に音声ファイルを再生する
subprocess.Popen(['start', 'C:\\Users\\Ito\\coding\\automate-stuff\\15time_and_thread\\alarm.wav'], shell=True)
# C:\Users\Ito\coding