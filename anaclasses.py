__author__ = 'tkessler'

import igor.binarywave as ibw
from numpy import *
import os

class ReadOnlyClass(type):
    def __setattr__(self, key, value):
        raise ValueError

class wave:
    __metaclass__ = ReadOnlyClass
    data = array([])
    pcsrA = 0
    pcsrB = 0
    def __init__(self, wavename="", xdelta=1, xUnits="", dataUnits=""):
        self.wavename = wavename
        self.xdelta = xdelta
        self.xUnits = xUnits
        self.dataUnits = dataUnits
    def loadbinary(self, bpath):
        thewave=ibw.load(bpath)
        if thewave['wave']['wave_header']['nDim'][1:].sum() > 0:
            print("Error: "+os.path.split(bpath)[1]+" > one dimension")
        else:
            h=thewave['wave']['wave_header']
            self.wavename = h['bname']
            self.xdelta = h['sfA'][0]
            self.data = thewave['wave']['wData']
            self.pcsrB = self.data.size
            for string in h['dimUnits'][0]:
                self.xUnits += string.decode()
            for string in h['dataUnits']:
                self.dataUnits += string.decode()
    def resetcurs(self):
        self.pcsrA=int(0)
        self.pcsrB=int(round(self.data.size))
    @property
    def getdata(self):
        """
        Returns a dictionary of 'data' and 'x' for the contained data set, confined by the current cursor values.
        :return:
        """
        thedict = dict()
        thedict['data']=self.data[self.pcsrA:self.pcsrB]
        thedict['x']=array(arange(self.pcsrA * self.xdelta, self.pcsrB * self.xdelta, self.xdelta))
        return thedict
    def setcurs(self,A,B):
        if A>=0 and A<=B and A<=self.data.size:
            self.pcsrA=int(round(A))
        if B>=A and B<=self.data.size:
            self.pcsrB=int(round(B))
    @property
    def getcurs(self):
        return (self.pcsrA, self.pcsrB)
    def setdata(self,newdata,newDeltaX):
        assert isinstance(newdata, array)
        self.data=newdata
        assert isinstance(newDeltaX, float)
        self.xdelta=newDeltaX
    @property
    def mean(self): return self.data[self.pcsrA:self.pcsrB].mean()
