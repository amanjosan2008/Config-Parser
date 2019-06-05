#!/usr/bin/python3
import os
import json
import re
import cgi, cgitb

print("Content-Type: text/html;charset=utf-8\r\n\r\n")
print ("""
<!DOCTYPE html>
<html lang="en">
<title>Tech Support Analyzer Tool</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
.w3-sidebar {
  z-index: 3;
  width: 250px;
  top: 43px;
  bottom: 0;
  height: inherit;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()"><i class="fa fa-bars"></i></a>
    <a href="#" class="w3-bar-item w3-button w3-theme-l1"><img src="https://avinetworks.com/client/logo.png"></a>
  </div>
</div>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- Main content: shift it to the right by 250 pixels when the sidebar is visible -->
<div class="w3-main" style="margin-left:250px">

  <div class="w3-row w3-padding-64">
    <div class="w3-twothird w3-container">
      <h1 class="w3-text-teal">Tech Support Analyzer</h1>
      <p>
""")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
path = form.getvalue('path')

dirlist = []

for root,dirc,files in os.walk(path):
    for filename in files:
       dirlist.append(os.path.join(os.path.realpath(root),filename))

def details(FILE):
    f = open(FILE,'r')
    l = f.readlines()
    print('<table style="width:100%">')
    for i in range(len(l)):
        if "ProductName" in l[i]:
            print("<tr><th>",l[i].split(':')[0],'</th><th>',l[i].split(':')[1],"</th></tr>")
    for i in range(len(l)):
        if "Product:" in l[i]:
            print("<tr><td>",l[i].split(':')[0],'</th><th>',l[i].split(':')[1],"</td></tr>")
    for i in range(len(l)):
        if "Version" in l[i]:
            print("<tr><td>",l[i].split(':')[0],'</th><th>',l[i].split(':')[1],"</td></tr>")
    for i in range(len(l)):
        if "build" in l[i]:
            print("<tr><td>",l[i].split(':')[0],'</th><th>',l[i].split(':')[1],"</td></tr>")
    for i in range(len(l)):
        if "Date" in l[i]:
            print("<tr><td>",l[i].split(':')[0],'</th><th>',l[i].split(':',1)[1],"</td></tr>")
    print('</table>')
    print("<br />")

# Versions Info
def ver():
    a = 0
    for i in dirlist:
        if "VERSION" in i:
            a += 1
    #print(a)
    if a == 0:
        print("<h3>\nVersion File not found\n</h3>")
        return
    print("<h3>\n############ VERSION INFO #############\n</h3>")
    NODES = []
    PATH_VER = []
    for DIR in dirlist:
        if "VERSION" in DIR:
            PATH_VER.append(DIR)
            for i in DIR.split('/'):
                if 'tech_node' in i:
                    #print("Node: ", i)
                    NODES.append(i)
    NODES =set(NODES)
    for j in NODES:
        print("<h4>",j,'</h4><br/>')
        for k in range(len(PATH_VER)):
            if j in PATH_VER[k]:
                #print(PATH_VER[k])
                if "root1" in PATH_VER[k] or "prev" in PATH_VER[k]:
                    print("Upgraded from:<br/>")
                    details(PATH_VER[k])
                else:
                    print("Upgraded To:<br/>")
                    details(PATH_VER[k])

try:
    ver()
except Exception as e:
    print("Exception: ",e,"<br /><br />")

print("<h3>\n############ DONE #############\n</h3>")

print ("""
      </p>
    </div>

<!-- END MAIN -->
</div>
</body>
</html>
""")
