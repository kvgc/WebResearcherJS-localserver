## Step 0 : Before you run this, run backup_annotations.sh.
## This creates 'saved_notes.csv' in the same folder
## This program parses the csv and outputs index.html

import pandas as pd
from bs4 import BeautifulSoup
df=pd.read_csv('saved_notes.csv', sep=',',header=None)

pageHTML = '''<html><body>
<link rel="stylesheet" type="text/css" href="ext_libs/bootstrap.min.css">
<script  type="text/javascript" src="ext_libs/bootstrap.min.js"></script>'''
for i in range(1,len(df.values)):
    pageHTML += '''
    <div class="card text-center" style="   width:100%;padding:2% 2% 2% 2%;">
    <div class="card-title">
    <button type="button" class="btn btn-dark btn-block">
        <a class ="text-light" href="https://''' + df.values[i][3] + '''">'''+ df.values[i][3] + '''</a></button></div>
        <div class="card-text text-left">'''
    soup = BeautifulSoup(df.values[i][4],'html.parser')
    div_tags = soup.find_all('div',class_="pell-content")
    for j in range(len(div_tags)):
        pageHTML+=str(div_tags[j])

    pageHTML+="</div></div><br><br>"

pageHTML+="</body></html>"
f= open("index.html",'w+')
f.write(pageHTML)
f.close()
