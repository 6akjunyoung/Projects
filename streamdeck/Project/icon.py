
import tkinter as tk

class Icon:
    def __init__(self, gui):
        self.__section = None
        self.__labelUpdater = None
        self.__sliderUpdater = None
        self.__slider = None
        self.__label = None
        self.__button = None
        self.__instance = gui

    def addSection(self, name=None):
        if name == None:
            self.__section = tk.Frame(self.__instance, padx=10, pady=10)
        else:
            self.__section = tk.LabelFrame(self.__instance, text=name, padx=10, pady=10)
        self.__section.pack(padx=10, pady=10, fill="x")
        return self

    def addButton(self, text, func):
        self.__button = tk.Button(self.__section, text=text, command=func)
        self.__button.pack(side="left", padx=5, pady=5)
        return self

    def addLabel(self, funcGetText):
        self.__label = tk.Label(self.__section, text=funcGetText())
        self.__label.pack(side="left", padx=10)
        self.__labelUpdater = funcGetText
        return self

    def addSlider(self, func, funcGetValue):
        self.__slider = tk.Scale(self.__section, from_=0, to=100, orient="horizontal", command=func)
        self.__slider.set(funcGetValue())
        self.__slider.pack(side="bottom")
        self.__sliderUpdater = funcGetValue
        return self

    def updateLabel(self):
        self.__label.config(text=self.__labelUpdater())

    def updateSlider(self):
        self.__slider.set(self.__sliderUpdater())
