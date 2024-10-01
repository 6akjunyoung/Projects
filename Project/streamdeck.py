import tkinter as tk
import subprocess
from tkinter import messagebox

# Internal modules
from controller import brightness
from controller import volume
import deck
import icon

brightnessControllers = []
monitors = brightness.Brightness.getMonitors()
for index, monitor in enumerate(monitors):
    brightnessControllers.append(brightness.Brightness(index))
    
volumeController = volume.Volume()

def launch_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
    except Exception as e:
        messagebox.showerror("Error", f"{app_name}을 실행하는 중 오류가 발생했습니다:\n{e}")

streamdeck = deck.Deck("StreamDeck", 800, 500)
root = streamdeck.getGUI()

applicationSection = icon.Icon(root)\
    .addSection("Application")\
    .addButton("Safari 실행", lambda: launch_app("Safari"))\
    .addButton("계산기 실행", lambda: launch_app("Calculator"))

streamdeck.appendController(volumeController.getTitle(), lambda val: volumeController.setLevel(int(val)), volumeController.getLevel)
for controller in brightnessControllers:
    streamdeck.appendController(controller.getTitle(), controller.setLevel, controller.getLevel)
streamdeck.activateController(volumeController.getTitle())

controllerSection = icon.Icon(root)\
    .addSection("Controller")\
    .addButton(volumeController.getTitle(), lambda: streamdeck.activateController(volumeController.getTitle()))\
    .addButton(brightnessControllers[0].getTitle(), lambda: streamdeck.activateController(brightnessControllers[0].getTitle()))\
    .addButton(brightnessControllers[1].getTitle(), lambda: streamdeck.activateController(brightnessControllers[1].getTitle()))\
    .addSlider(streamdeck.setControllerLevel, streamdeck.getControllerLevel)

statusSection = icon.Icon(root)\
    .addSection()\
    .addButton("상태 업데이트", streamdeck.update)

streamdeck.appendSection(applicationSection)
streamdeck.appendSection(controllerSection)
streamdeck.appendSection(statusSection)

streamdeck.appendUpdater(controllerSection.updateSlider)

def periodic_update():
    streamdeck.update()
    root.after(500, periodic_update)

periodic_update()

root.mainloop()
