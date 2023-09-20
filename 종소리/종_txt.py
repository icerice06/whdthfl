#pip install playsound==1.2.2

from playsound import playsound
import time

times_to_play_sound = []
with open("시정표.txt", 'r') as f:
    for line in f:
        line = line.strip() 
        times_to_play_sound.extend(line.split())

print("START")

while True:
    current_time = time.strftime("%H:%M:%S")
    
    if current_time in times_to_play_sound:
        print(current_time)
        playsound("a3.mp3")