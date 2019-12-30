# -*- coding: utf-8 -*-

import functions as f


filepath = '/home/pi/Desktop/Associations.ods'

vege_dict = f.export_vegetables(filepath)

v = input("Entre un legume wesh: ")
if v not in vege_dict:
    print("Pas dans la liste, verifie l'ortographe")
else:
    print(f.print_carac(v, vege_dict))

