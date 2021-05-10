# -*- coding: utf-8 -*-
"""
Created on Tue May 08 08:05:27 2021

@author: TANMAY HARSH
"""

import os, platform
from time import sleep


if platform.system()=='Windows':
    ROOT_PATH='/'.join(__file__.split("\\")[:-1])+'/'
else: ROOT_PATH='/'.join(__file__.split("/")[:-1])+'/'

if __name__ == '__main__':
    os.system(ROOT_PATH+"Test_AAA_TH/Tester.py")
    sleep(1)
    os.system(ROOT_PATH+"Test_AAA_TH/RepoRTs_Generator.py")
    sleep(1)
    os.system(ROOT_PATH+"Test_AAA_TH/RepoRTs_Finalizer.py")
    input()
