# 4 :30

""" TEMPAT INPUT UTAMA """

from action import *

#introduction
intro = input('Hello ^o^\nWanna buy or sell? ')

#percabangan

if intro == 'buy': #condition 1
    print('='*50)
    Buy()

elif intro == 'sell' :   #condition 2
    print('='*50)
    Sell()

else:   #condition 3
    print('bye')