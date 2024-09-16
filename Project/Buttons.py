import tkinter as tk
import os
import subprocess

window = tk.Tk()
window.title("SteamDeck")
window.geometry("500x500+500+150")
window.resizable(True,True)

count=0

def countUp():
    global count
    count +=1
    label.config(text=str(count))

def updateVolume():
    current_volume = getVolume()
    label_vol.config(text="current volume:"+str(current_volume))

def getVolume():
    result = subprocess.run(["osascript", "-e", "output volume of (get volume settings)"], 
                            capture_output=True, text=True)
    return int(result.stdout.strip())

def setVolume(volume):
    subprocess.run(["osascript", "-e", f"set volume output volume {volume}"])

def volumeUp(step=10):
    current_volume = getVolume()
    new_volume = min(current_volume + step, 100)
    setVolume(new_volume)
    updateVolume()

def volumeDown(step=10):
    current_volume = getVolume()
    new_volume = max(current_volume - step, 0)
    setVolume(new_volume)
    updateVolume()

label = tk.Label(window, text="0")
label.pack()

label_vol = tk.Label(window, text="0")
label_vol.pack()
updateVolume()

button = tk.Button(window, text="Count", overrelief="solid", height=5, width=15, command=countUp, repeatdelay=1000, repeatinterval=100)
button.pack()

button = tk.Button(window, text="Volume up", overrelief="solid", height=5, width=15, command=volumeUp, repeatdelay=1000, repeatinterval=100)
button.pack()

button = tk.Button(window, text="Volume down", overrelief="solid", height=5, width=15, command=volumeDown, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()