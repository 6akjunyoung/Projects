
import tkinter as tk

class Deck:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height
        self.__sections = []
        self.__updaters = []
        self.__controllers = { }
        self.__activeControllerName = ""
        self.__initGUI()

    def __initGUI(self):
        self.__gui = tk.Tk()
        self.__gui.title(self.__title)
        self.__gui.geometry(f"{ self.__width }x{ self.__height }")

    def update(self):
        for updater in self.__updaters:
            updater()

    def getGUI(self):
        return self.__gui

    def appendSection(self, section):
        self.__sections.append(section)

    def appendUpdater(self, updater):
        self.__updaters.append(updater)

    def appendController(self, name, funcSetter, funcGetter):
        self.__controllers[name] = funcSetter, funcGetter

    def activateController(self, name):
        self.__activeControllerName = name

    def setControllerLevel(self, val):
        funcSetter, _ = self.__controllers[self.__activeControllerName]
        funcSetter(int(val))

    def getControllerLevel(self):
        _, funcGetter = self.__controllers[self.__activeControllerName]
        return funcGetter()