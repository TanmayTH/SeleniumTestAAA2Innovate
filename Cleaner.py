# -*- coding: utf-8 -*-
"""
Created on Wed May 09 15:06:31 2021

@author: TANMAY HARSH
"""

import os, platform

def FileCleaner(dir_list):
    for directory in dir_list:
        for file in os.listdir(ROOT_PATH+directory):
            os.remove(ROOT_PATH+directory+file)

if platform.system()=='Windows': ROOT_PATH='/'.join(__file__.split("\\")[:-1])+'/'
else: ROOT_PATH='/'.join(__file__.split("/")[:-1])+'/'

Directory_to_clear=("HTML_RepoRTs/", "CSV_RepoRTs/")

print("Cleaning Previous Files...\n")
FileCleaner(Directory_to_clear)
print("All Ready to Go !\n\n")
input()
