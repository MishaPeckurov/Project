class string:
    strl = 'all'
    strl1 = 'ALLL'
class check(string):
    def checkstring(self):
        print(max(len(self.strl),len(self.strl1)))
a = check()
a.checkstring()