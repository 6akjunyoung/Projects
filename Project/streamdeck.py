import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import screen_brightness_control as sbc

def set_brightness_mac(level):
    # level: 0 ~ 100 사이의 값
    sbc.set_brightness(level)
    print(f"Brightness set to {level}")

def get_brightness_mac():
    brightness = sbc.get_brightness()
    print(f"Current brightness is {brightness}")
    return brightness
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
def get_volume():
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

def set_volume(volume):
    try:
        subprocess.run(
            ["osascript", "-e", f"set volume output volume {volume}"]
        )
    except Exception as e:
        messagebox.showerror("Error", f"볼륨을 설정하는 중 오류가 발생했습니다:\n{e}")

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

# 밝기 관련 함수
def get_brightness():
    return get_brightness_mac()
    try:
        result = subprocess.run(
            ["brightness", "-l"],
            capture_output=True,
            text=True
        )
        for line in result.stdout.split('\n'):
            if "brightness" in line.lower():
                return float(line.split()[-1])
        return 1.0  # 기본값
    except Exception as e:
        messagebox.showerror("Error", f"밝기를 가져오는 중 오류가 발생했습니다:\n{e}")
        return 1.0

def set_brightness(value):
    set_brightness_mac(value)
    return
    try:
        subprocess.run(
            ["brightness", f"{value}"]
        )
    except Exception as e:
        messagebox.showerror("Error", f"밝기를 설정하는 중 오류가 발생했습니다:\n{e}")

def increase_brightness():
    current = get_brightness()
    new_brightness = min(current + 0.1, 1.0)
    set_brightness(new_brightness)
    update_brightness_label()

def decrease_brightness():
    current = get_brightness()
    new_brightness = max(current - 0.1, 0.0)
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
    brightness_percentage = int(brightness * 100)
    brightness_label.config(text=f"밝기: {brightness_percentage}%")

# GUI 설정
root = tk.Tk()
root.title("Mac 제어 도구")
root.geometry("400x300")

# 애플리케이션 실행 섹션
app_frame = tk.LabelFrame(root, text="애플리케이션 실행", padx=10, pady=10)
app_frame.pack(padx=10, pady=10, fill="x")

safari_button = tk.Button(app_frame, text="Safari 실행", command=lambda: launch_app("Safari"))
safari_button.pack(side="left", padx=5, pady=5)

calculator_button = tk.Button(app_frame, text="계산기 실행", command=lambda: launch_app("Calculator"))
calculator_button.pack(side="left", padx=5, pady=5)

# 볼륨 조절 섹션
volume_frame = tk.LabelFrame(root, text="볼륨 조절", padx=10, pady=10)
volume_frame.pack(padx=10, pady=10, fill="x")

decrease_volume_button = tk.Button(volume_frame, text="- 볼륨 낮추기", command=decrease_volume)
decrease_volume_button.pack(side="left", padx=5, pady=5)

volume_label = tk.Label(volume_frame, text="볼륨: --%")
volume_label.pack(side="left", padx=10)

increase_volume_button = tk.Button(volume_frame, text="+ 볼륨 올리기", command=increase_volume)
increase_volume_button.pack(side="left", padx=5, pady=5)

# 밝기 조절 섹션
brightness_frame = tk.LabelFrame(root, text="화면 밝기 조절", padx=10, pady=10)
brightness_frame.pack(padx=10, pady=10, fill="x")

decrease_brightness_button = tk.Button(brightness_frame, text="- 밝기 낮추기", command=decrease_brightness)
decrease_brightness_button.pack(side="left", padx=5, pady=5)

brightness_label = tk.Label(brightness_frame, text="밝기: --%")
brightness_label.pack(side="left", padx=10)

increase_brightness_button = tk.Button(brightness_frame, text="+ 밝기 올리기", command=increase_brightness)
increase_brightness_button.pack(side="left", padx=5, pady=5)

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
brightness_slider = tk.Scale(brightness_frame, from_=0, to=100, orient="horizontal", command=lambda val: set_brightness(int(val)/100))
brightness_slider.set(int(get_brightness() * 100))
brightness_slider.pack(side="left", padx=10)

# 상태 업데이트 함수 수정
def update_labels():
    current_volume = get_volume()
    volume_slider.set(current_volume)
    volume_label.config(text=f"볼륨: {current_volume}%")
    
    current_brightness = get_brightness()
    brightness_slider.set(int(current_brightness * 100))
    brightness_label.config(text=f"밝기: {int(current_brightness * 100)}%")


# 주기적으로 상태 업데이트 (예: 5초마다)
def periodic_update():
    update_labels()
    root.after(500, periodic_update)

root.after(500, periodic_update)

# 메인 루프 시작
root.mainloop()
