
import tkinter as tk

class Deck:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height
        self.__section = {}
        self.__initInstance()

    def __initInstance(self):
        self.__instance = tk.Tk()
        self.__instance.title(self.__title)
        self.__instance.geometry(f"{ self.__width }x{ self.__height }")

    def getTkInstance(self):
        return self.__instance

    def addSection(self, name):
        section = tk.LabelFrame(self.__instance, text=name, padx=10, pady=10)
        section.pack(padx=10, pady=10, fill="x")
        self.__section[name] = section
        return section

    def addButton(self, text, func, sectionname):
        button = tk.Button(self.__section[sectionname], text=text, command=func)
        button.pack(side="left", padx=5, pady=5)

    def addLabel(self, text, sectionname):
        label = tk.Label(self.__section[sectionname], text=text)
        label.pack(side="left", padx=10)
        return label

    def addScale(self, func, val, sectionname):
        slider = tk.Scale(self.__section[sectionname], from_=0, to=100, orient="horizontal", command=func)
        slider.set(val)
        slider.pack(side="left", padx=10)
        return slider
