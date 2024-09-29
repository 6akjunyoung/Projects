import screen_brightness_control as sbc

class Brightness:
    def __init__(self):
        self.__title = "Brightness"
        self.__maxLevel = 100
        self.__minLevel = 0

    def getLabel(self):
        return "밝기: %s%%" % str(self.getLevel())

    def setLevel(self, level):
        level = max(level, self.__minLevel)
        level = min(level, self.__maxLevel)
        sbc.set_brightness(level)

    def getLevel(self):
        level = sbc.get_brightness()
        return level[0]

    def increaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel + 10)

    def decreaseLevel(self):
        currentLevel = self.getLevel()
        self.setLevel(currentLevel - 10)

    def getTitle(self):
        return self.__title