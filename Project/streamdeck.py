import tkinter as tk
import subprocess
from tkinter import messagebox

# Internal modules
from controller import brightness
from controller import volume
import deck
import icon

brightnessController = []
monitors = brightness.Brightness.getMonitors()
for index, monitor in enumerate(monitors):
    brightnessController.append(brightness.Brightness(index))
    
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

volumeSection = icon.Icon(root)\
    .addSection(volumeController.getTitle())\
    .addButton("- 볼륨 낮추기", volumeController.decreaseLevel)\
    .addLabel(volumeController.getLabel)\
    .addButton("+ 볼륨 올리기", volumeController.increaseLevel)\
    .addSlider(lambda val: volumeController.setLevel(int(val)), volumeController.getLevel)

brightnessSections = []
for controller in brightnessController:
    brightnessSection = icon.Icon(root)\
        .addSection(controller.getTitle())\
        .addButton("- 밝기 낮추기", controller.decreaseLevel)\
        .addLabel(controller.getLabel)\
        .addButton("+ 밝기 올리기", controller.increaseLevel)\
        .addSlider(lambda val: controller.setLevel(int(val)), controller.getLevel)
    brightnessSections.append(brightnessSection)

statusSection = icon.Icon(root)\
    .addSection()\
    .addButton("상태 업데이트", streamdeck.update)

streamdeck.appendSection(applicationSection)
streamdeck.appendSection(volumeSection)
for brightnessSection in brightnessSections:
    streamdeck.appendSection(brightnessSection)
streamdeck.appendSection(statusSection)

streamdeck.appendUpdater(volumeSection.updateLabel)
streamdeck.appendUpdater(volumeSection.updateSlider)
for brightnessSection in brightnessSections:
    streamdeck.appendUpdater(brightnessSection.updateLabel)
    streamdeck.appendUpdater(brightnessSection.updateSlider)

def periodic_update():
    streamdeck.update()
    root.after(1000, periodic_update)

periodic_update()

root.mainloop()
