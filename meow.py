import time
from playsound import playsound

def play_sound():
    while True:
        playsound("meow.wav")
        time.sleep(1)
if __name__ == "__main__":
    play_sound()
