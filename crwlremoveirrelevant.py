'''
Created on Sep 11, 2017

@author: admin_home
'''
import os
import glob
f_path = raw_input('Enter  path : ')
for hgx in glob.glob("*favicon*"):
    os.remove(hgx)
for hgx in glob.glob("*full-frame*"):
    os.remove(hgx)
for hgx in glob.glob("*eyeglasses"):
    print hgx
    os.remove(hgx)
        