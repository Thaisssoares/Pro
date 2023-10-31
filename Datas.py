class Datas (object):
    def __init__(self, diaDatas, mesDatas, anoDatas):
        self.diaDatas = diaDatas
        self.mesDatas = mesDatas
        self.anoDatas = anoDatas

    def setdiaDatas(self,diaDatas):
        if diaDatas in (1, 2, 3):
            self.diaDatas = diaDatas
        else:
            self.diaDatas = 1

    def getdiaDatas(self):
        return self.diaDatas
    def setmesDatas(self, mesDatas):
        self.mesDatas = mesDatas
    def getmesDatas(self):
        return self.mesDatas
    def setanoDatas(self,anoDatas):
        self.anoDatas = anoDatas
    def getanoDatas(self):
        return self.anoDatas

    def __str__(self):
        return "\n\n diaDatas: " + str(self.diaDatas)+ "\n mesDatas: " +str(self.mesDatas)+ "\n anoDatas: " +str(self.anoDatas)+ "\n\n"