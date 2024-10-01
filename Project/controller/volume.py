import platform
import subprocess
from tkinter import messagebox
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

class Volume:
    def __init__(self):
        self.__title = "Volume"
        self.__maxLevel = 100
        self.__minLevel = 0

    def getLabel(self):
        return "볼륨: %s%%" % str(self.getLevel())

    def getLevel(self):
        if ('Windows'==platform.system()):
            return self.__getLevelWindows()
        else:
            return self.__get_volume_mac()

    def __getLevelWindows(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar() * 100
        return int(current_volume)

    def __setLevelWindows(self, value):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(value / 100, None)

    def setLevel(self, level):
        level = max(level, self.__minLevel)
        level = min(level, self.__maxLevel)

        if ('Windows'==platform.system()):
            self.__setLevelWindows(level)
        else:
            self.__set_volume_mac(level)

    def increaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel + 10)

    def decreaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel - 10)

    def getTitle(self):
        return self.__title

    # mac
    def __get_volume_mac():
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

    def __set_volume_mac(level):
        try:
            subprocess.run(
                ["osascript", "-e", f"set volume output volume {level}"]
            )
        except Exception as e:
            messagebox.showerror("Error", f"볼륨을 설정하는 중 오류가 발생했습니다:\n{e}")