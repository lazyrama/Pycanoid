from settings import VIRTUAL_PIXEL
from entities import Block


class LevelLoader:
    def __init__(self):
        levels = []

        with open("levels.txt", "r") as f:
            flag = False
            level = []
            lines = f.readlines()
            for line in lines:
                if "\"\"\"" in line and not flag:
                    flag = True
                elif "\"\"\"" in line and flag:
                    levels.append(level)
                    level = []
                    flag = False
                else:
                    level.append(line.rstrip('\n'))
        self.campaign = []
        for i, level in enumerate(levels):
            level1 = []
            for j, line in enumerate(level):
                line1 = []
                for k, block in enumerate(line):
                    if block == "#":
                        line1.append(Block(k * 4 * VIRTUAL_PIXEL, 2 * VIRTUAL_PIXEL + j * VIRTUAL_PIXEL,
                                           ))
                level1.append(line1)
            self.campaign.append(level1)
