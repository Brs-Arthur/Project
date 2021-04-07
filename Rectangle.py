class Rectangle:
    def __init__(self,x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.lenVectorX = self.x2 - self.x1
        self.lenVectorY = self.y2 - self.y1
        self.listCoor = []

    def addCoor(self):
        for x in range(self.x1, self.lenVectorX+2):
            for y in range(self.y1, self.lenVectorY+2):
                self.listCoor.append([x,y])