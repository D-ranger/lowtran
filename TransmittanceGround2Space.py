#!/usr/bin/env python
from matplotlib.pyplot import show
#
import lowtran
from lowtran.plots import plottrans

if __name__=='__main__':

    from argparse import ArgumentParser
    p = ArgumentParser(description='Lowtran 7 interface')
    p.add_argument('-z','--obsalt',help='altitude of observer [km]',type=float,default=0.)
    p.add_argument('-a','--zenang',help='observer zenith angle [deg]',type=float,nargs='+',default=[0,60,80])
    p.add_argument('-w','--wavelen',help='wavelength range nm (start,stop)',type=float,nargs=2,default=(200,30000))
    p.add_argument('--model',help='0-6, see Card1 "model" reference. 5=subarctic winter',type=int,default=5)
    p=p.parse_args()

    c1={'model':p.model,
        'itype':3,   # 3: observer to space
        'iemsct':0,  # 0: transmittance
        'h1': p.obsalt,
        'angle': p.zenang,
        'wlnmlim': p.wavelen,
        }

    TR = lowtran.loopangle(c1)

    plottrans(TR, c1, False)

    show()
