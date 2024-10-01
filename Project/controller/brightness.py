import screen_brightness_control as sbc

class Brightness:
    def __init__(self, index):
        self.__title = "Monitor " + str(index)
        self.__maxLevel = 100
        self.__minLevel = 0
        self.__index = index

    @staticmethod 
    def getMonitors():
        return sbc.list_monitors()

    def getLabel(self):
        return "밝기: %s%%" % str(self.getLevel())

    def setLevel(self, level):
        level = max(level, self.__minLevel)
        level = min(level, self.__maxLevel)
        sbc.set_brightness(level, display=self.__index)

    def getLevel(self):
        level = sbc.get_brightness()
        return level[self.__index]

    def increaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel + 10)

    def decreaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel - 10)

    def getTitle(self):
        return self.__title