# -*- coding: utf-8 -*-
"""
Created on Wed May 09 15:00:46 2021

@author: TANMAY HARSH
"""

import os, re, platform
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS


if platform.system()=='Windows':
    ROOT_PATH='/'.join(__file__.split("\\")[:-2])+'/'
else: ROOT_PATH='/'.join(__file__.split("/")[:-2])+'/'

HTML_RepoRTs_path=ROOT_PATH+"HTML_RepoRTs/"

print("\nGenerating CSV Reports...\n")

info_Dic={}

for filename in os.listdir(HTML_RepoRTs_path):
    file_ind=re.search(r"(_[\d]+_)",filename).group()
    info_Dic[file_ind]={'tests_info':{}, 'filename':filename}

    with open(HTML_RepoRTs_path+filename,encoding="utf-8") as f:
        soup=BS(f.read(),features="html.parser")
        infos=soup.find('tbody').find_all('tr',class_=['success','warning','danger'])
        for table_row in range(len(infos)):
            info_Dic[file_ind]['tests_info'][f'test{table_row+1}']=infos[table_row].find_all('td',class_="col-xs-1")[0].text.strip()


with open(ROOT_PATH+"CSV_RepoRTs/TestResultCSV.csv",'w',encoding="utf-8") as f:
    with open(ROOT_PATH+"TestDataCSV/"+os.listdir(ROOT_PATH+"TestDataCSV/")[0],encoding="utf-8") as f2:
        file_buffer=f2.read()
    f.write(file_buffer)

df=pd.read_csv(ROOT_PATH+'CSV_RepoRTs/TestResultCSV.csv',index_col='ORIGIN',)
df=df.replace(np.nan,"",regex=True)

for TotalTests in range(len(info_Dic)):
    write_filename=False
    for SubTests in range(len(info_Dic[f"_{TotalTests}_"]['tests_info'])):
        result=info_Dic[f"_{TotalTests}_"]['tests_info'][f"test{SubTests+1}"]
        df[f"test{SubTests+1}"][TotalTests]=result
        if result!="Pass" and write_filename==False: write_filename=True
    if write_filename==True:
        df["filename"][TotalTests]=info_Dic[f"_{TotalTests}_"]['filename']

df.to_csv(ROOT_PATH+'CSV_RepoRTs/TestResultCSV.csv')
