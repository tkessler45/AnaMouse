__author__ = 'tkessler'

import anaclasses

a = anaclasses.wave()
a.loadbinary('/Users/tkessler/wave0.ibw')
print(a.getdata['data'])
print(a.mean)
a.setcurs(2,4)
print(a.getdata['x'])


b = anaclasses.wave()
b.loadbinary('/Users/tkessler/imemchart.ibw')
print(b.mean)
b.setcurs(5/b.xdelta,10/b.xdelta)
print(b.getdata)