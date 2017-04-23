#!/usr/bin/env python
from matplotlib.pyplot import show
#
import lowtran
from lowtran.plots import plottrans

if __name__=='__main__':

    from argparse import ArgumentParser
    p = ArgumentParser(description='Lowtran 7 interface')
    p.add_argument('-z','--obsalt',help='altitude of observer [km]',type=float,default=0.)
    p.add_argument('-a','--zenang',help='zenith angle [deg]  can be single value or list of values',type=float,default=0)
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

    TR = lowtran.golowtran(c1)


    plottrans(TR,p.zenang,False)

    show()
