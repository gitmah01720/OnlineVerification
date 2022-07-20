import sys
import  datetime

class files:
    pth="";
    
    def __init__(self,pAth):
        try :
           reder = open(pAth,"r");
        except :
            print("File Does NOT exixt!\n");
            return
        self.pth = pAth;
        

    def readfile(self):
        reder = open(self.pth,"r");
        st = reder.read();
        print(st)
        reder.close()
        return st

    def writeinfile(self,tx):
        writer = open(self.pth,"w");
        writer.write(tx)
        writer.close();
    def appendinfile(self,tx):
            writer = open(self.pth,"a");
            writer.write(tx)
            writer.close();

myfile = files("msg.txt")
opt = "Hi {0} time is {1} ".format(1,datetime.datetime.now())
myfile.writeinfile(opt)

print("akjshdf")