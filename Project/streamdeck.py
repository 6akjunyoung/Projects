import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import platform
import screen_brightness_control as sbc

import deck

def set_brightness(level):
    # level: 0 ~ 100 사이의 값
    sbc.set_brightness(level)
    #print(f"Brightness set to {level}")

def get_brightness():
    brightness = sbc.get_brightness()
    #print(f"Current brightness is {brightness}")
    return brightness[0]
'''
def set_brightness_mac(level):
    # level: 0 ~ 100 사이의 값
    try:
        subprocess.run(["osascript", "-e", f"tell application \"System Events\" to set the value of slider 1 of group 1 of window 1 of application process \"Displays\" to {level}"], check=True)
        print(f"Brightness set to {level}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set brightness: {e}")

def get_brightness_mac():
    try:
        return 0
        result = subprocess.run(["osascript", "-e", "tell application \"System Events\" to get the value of slider 1 of group 1 of window 1 of application process \"Displays\""], capture_output=True, text=True, check=True)
        return float(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Failed to get brightness: {e}")
        return 0
'''

# 볼륨 관련 함수
def get_volume_mac():
    try:
        result = subprocess.run(
            ["osascript", "-e", "output volume of (get volume settings)"],
            capture_output=True,
            text=True
        )
        return int(result.stdout.strip())
    except Exception as e:
        messagebox.showerror("Error", f"볼륨을 가져오는 중 오류가 발생했습니다:\n{e}")
        return 0

def set_volume_mac(volume):
    try:
        subprocess.run(
            ["osascript", "-e", f"set volume output volume {volume}"]
        )
    except Exception as e:
        messagebox.showerror("Error", f"볼륨을 설정하는 중 오류가 발생했습니다:\n{e}")

def get_volume():
    if ('Windows'==platform.system()):
        return 0
    else:
        return get_volume_mac()

def set_volume(volume):
    if ('Windows'==platform.system()):
        return
    else:
        set_volume_mac()

def increase_volume():
    current = get_volume()
    new_volume = min(current + 10, 100)
    set_volume(new_volume)
    update_volume_label()

def decrease_volume():
    current = get_volume()
    new_volume = max(current - 10, 0)
    set_volume(new_volume)
    update_volume_label()

def increase_brightness():
    current = get_brightness()
    new_brightness = min(current + 10, 100)
    set_brightness(new_brightness)
    update_brightness_label()

def decrease_brightness():
    current = get_brightness()
    new_brightness = max(current - 10, 0)
    set_brightness(new_brightness)
    update_brightness_label()

# 애플리케이션 실행 함수
def launch_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
    except Exception as e:
        messagebox.showerror("Error", f"{app_name}을 실행하는 중 오류가 발생했습니다:\n{e}")

# 라벨 업데이트 함수
def update_labels():
    update_volume_label()
    update_brightness_label()

def update_volume_label():
    volume = get_volume()
    volume_label.config(text=f"볼륨: {volume}%")

def update_brightness_label():
    brightness = get_brightness()
    brightness_percentage = int(brightness)
    brightness_label.config(text=f"밝기: {brightness_percentage}%")

# GUI 설정
streamdeck = deck.Deck("StreamDeck", 800, 500)
root = streamdeck.getTkInstance()

# 애플리케이션 실행 섹션
streamdeck.addSection("Application")
streamdeck.addButton("Safari 실행", lambda: launch_app("Safari"), "Application")
streamdeck.addButton("계산기 실행", lambda: launch_app("Calculator"), "Application")

# 볼륨 조절 섹션
volume_frame = streamdeck.addSection("Volume")
streamdeck.addButton("- 볼륨 낮추기", decrease_volume, "Volume")
volume_label = streamdeck.addLabel("볼륨: --%", "Volume")
streamdeck.addButton("+ 볼륨 올리기", increase_volume, "Volume")

# 밝기 조절 섹션
brightness_frame = streamdeck.addSection("Brightness")
streamdeck.addButton("- 밝기 낮추기", decrease_brightness, "Brightness")
brightness_label = streamdeck.addLabel("밝기: --%", "Brightness")
streamdeck.addButton("+ 밝기 올리기", increase_brightness, "Brightness")

# 상태 업데이트 섹션

status_frame = tk.Frame(root, padx=10, pady=10)
status_frame.pack(padx=10, pady=10, fill="x")

update_button = tk.Button(status_frame, text="상태 업데이트", command=update_labels)
update_button.pack()

# 초기 상태 라벨 업데이트
update_labels()

# ... (이전 코드와 동일)

# 볼륨 슬라이더
volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient="horizontal", command=lambda val: set_volume(int(val)))
volume_slider.set(get_volume())
volume_slider.pack(side="left", padx=10)

# 밝기 슬라이더
brightness_slider = tk.Scale(brightness_frame, from_=0, to=100, orient="horizontal", command=lambda val: set_brightness(int(val)))
brightness_slider.set(int(get_brightness()))
brightness_slider.pack(side="left", padx=10)

# 상태 업데이트 함수 수정
def update_labels():
    current_volume = get_volume()
    volume_slider.set(current_volume)
    volume_label.config(text=f"볼륨: {current_volume}%")
    
    current_brightness = get_brightness()
    brightness_slider.set(int(current_brightness))
    brightness_label.config(text=f"밝기: {int(current_brightness)}%")


# 주기적으로 상태 업데이트 (예: 5초마다)
def periodic_update():
    update_labels()
    root.after(500, periodic_update)

root.after(500, periodic_update)

# 메인 루프 시작
root.mainloop()
