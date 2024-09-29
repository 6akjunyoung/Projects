import tkinter as tk
import subprocess
from tkinter import messagebox

# Internal modules
import brightness
import volume
import deck

brightnessController = brightness.Brightness()
volumeController = volume.Volume()

# 애플리케이션 실행 함수
def launch_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
    except Exception as e:
        messagebox.showerror("Error", f"{app_name}을 실행하는 중 오류가 발생했습니다:\n{e}")

# GUI 설정
streamdeck = deck.Deck("StreamDeck", 800, 500)
root = streamdeck.getTkInstance()

# 애플리케이션 실행 섹션
streamdeck.addSection("Application")
streamdeck.addButton("Safari 실행", lambda: launch_app("Safari"), "Application")
streamdeck.addButton("계산기 실행", lambda: launch_app("Calculator"), "Application")

# 볼륨 조절 섹션
streamdeck.addSection(volumeController.getTitle())
streamdeck.addButton("- 볼륨 낮추기", volumeController.decreaseLevel, volumeController.getTitle())
streamdeck.addLabel("볼륨: %s%%", volumeController.getLevel, volumeController.getTitle())
streamdeck.addButton("+ 볼륨 올리기", volumeController.increaseLevel, volumeController.getTitle())
streamdeck.addScale(lambda val: volumeController.setLevel(int(val)), volumeController.getLevel(), volumeController.getTitle())

# 밝기 조절 섹션
streamdeck.addSection(brightnessController.getTitle())
streamdeck.addButton("- 밝기 낮추기", brightnessController.decreaseLevel, brightnessController.getTitle())
streamdeck.addLabel("밝기: %s%%", brightnessController.getLevel, brightnessController.getTitle())
streamdeck.addButton("+ 밝기 올리기", brightnessController.increaseLevel, brightnessController.getTitle())
streamdeck.addScale(lambda val: brightnessController.setLevel(int(val)), int(brightnessController.getLevel()), brightnessController.getTitle())

# 상태 업데이트 함수 수정
def update_labels():
    streamdeck.updateLabel(volumeController.getTitle())
    streamdeck.updateLabel(brightnessController.getTitle())

# 상태 업데이트 섹션
status_frame = tk.Frame(root, padx=10, pady=10)
status_frame.pack(padx=10, pady=10, fill="x")
update_button = tk.Button(status_frame, text="상태 업데이트", command=update_labels)
update_button.pack()

# 주기적으로 상태 업데이트 (예: 5초마다)
def periodic_update():
    update_labels()
    root.after(500, periodic_update)

periodic_update()

# 메인 루프 시작
root.mainloop()
