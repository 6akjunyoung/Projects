
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

    def addSection(self, title):
        section = tk.LabelFrame(self.__instance, text=title, padx=10, pady=10)
        section.pack(padx=10, pady=10, fill="x")
        self.__section[title] = section
        return section

    def addButton(self, text, func, sectiontitle):
        button = tk.Button(self.__section[sectiontitle], text=text, command=func)
        button.pack(side="left", padx=5, pady=5)

    def addLabel(self, text, sectiontitle):
        label = tk.Label(self.__section[sectiontitle], text=text)
        label.pack(side="left", padx=10)
        return label