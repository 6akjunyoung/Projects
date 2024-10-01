from monitorcontrol import get_monitors

class Brightness:
    def __init__(self, index):
        self.__title = "Monitor " + str(index)
        self.__maxLevel = 100
        self.__minLevel = 0
        self.__monitor = get_monitors()[index]

    @staticmethod 
    def getMonitors():
        return get_monitors()

    def getLabel(self):
        return "밝기: %s%%" % str(self.getLevel())

    def setLevel(self, level):
        level = max(level, self.__minLevel)
        level = min(level, self.__maxLevel)
        
        with self.__monitor:
            self.__monitor.set_luminance(level)

    def getLevel(self):
        with self.__monitor:
            return self.__monitor.get_luminance()

    def increaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel + 10)

    def decreaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel - 10)

    def getTitle(self):
        return self.__title