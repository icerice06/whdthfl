#pip install playsound==1.2.2
from playsound import playsound
import time

times_to_play_sound = [
    "08:40:00",
    "09:30:00",
    "09:40:00",
    "10:30:00",
    "10:40:00",
    "11:30:00",
    "11:40:00",
    "12:30:00",
    "13:40:00",
    "14:30:00",
    "14:40:00",
    "15:30:00",
    "15:40:00",
    "16:30:00",
    "16:40:00",
    "18:10:00",
    "19:10:00",
    "20:30:00"
]

print("START")

while True:
    current_time = time.strftime("%H:%M:%S")
    
    if current_time in times_to_play_sound:
        print(current_time)
        playsound("a3.mp3")
