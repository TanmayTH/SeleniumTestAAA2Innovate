# -*- coding: utf-8 -*-
"""
Created on Wed May 09 15:02:36 2021

@author: TANMAY HARSH
"""

import os, platform

def DeleteFile(file_path):
    with open(file_path) as f:
        file_buffer=f.read()
        if file_buffer.find("<tr class='danger'>")!=-1 or file_buffer.find("<tr class='warning'>")!=-1:
            return False
    return True

def TestReportsOrganizer(path):
    for file in os.listdir(path):
        file_path=path+file
        if DeleteFile(file_path):
            os.remove(file_path)


if platform.system()=='Windows':
    ROOT_PATH='/'.join(__file__.split("\\")[:-2])+'/'
else: ROOT_PATH='/'.join(__file__.split("/")[:-2])+'/'
HTML_RepoRTs_path=ROOT_PATH+"HTML_RepoRTs/"

print("\n\nFinalizing Reports...")
TestReportsOrganizer(HTML_RepoRTs_path)
print("\nReports Finalized !\n")
