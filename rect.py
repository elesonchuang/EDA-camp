class Rectangle():
    '''
    A class for construct an input rectangle.
    'self.points' contains all points inputted.
    'self.linexs' contains the x coordinates of both edges(sorted from small to large).
    'self.lineys' contains the y coordinates of both edges(sorted from small to large).
    '''
    def __init__(self,p1,p2,p3,p4):
        self.points = [p1,p2,p3,p4]
        self.points.sort()
        self.points[2:] = self.points[::-1][0:2] # sort the points list in clockwise order, start with the downleft point.
        self.linexs = []
        self.lineys = []
        for point in self.points:
            if point[0] not in self.linexs: self.linexs.append(point[0])
            if point[1] not in self.lineys: self.lineys.append(point[1])
        self.linexs.sort()
        self.lineys.sort()
            

    def touch(self,target):
        for point in self.points:
                if (point[0] in target.linexs and target.lineys[0] <= point[1] <= target.lineys[1]) or (point[1] in target.lineys and target.linexs[0] <= point[0] <= target.linexs[0]):
                    return point
        return None


