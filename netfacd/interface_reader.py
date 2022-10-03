#!/usr/bin/env python3

import netifaces

for i in netifaces.interfaces():

    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except: # THIS IS A NEW LINE
        print('Could not collect adapter information')
