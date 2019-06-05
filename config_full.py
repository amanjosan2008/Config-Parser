#!/usr/bin/python3
import os
import json
import re
import cgi, cgitb
#import sys

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
path = form.getvalue('path')

dirlist = []

for root,dirc,files in os.walk(path):
    for filename in files:
       dirlist.append(os.path.join(os.path.realpath(root),filename))

#Avi Config Loader
for i in dirlist:
    if i.split('/')[-1] == "avi_config":
        f = open(i,'r')
        config = json.load(f)
        f.close

a = []
for i in config.keys():
    a.append(i)

def convert(obj):
     if isinstance(obj, bool):
         return str(obj).lower()
     if isinstance(obj, (list, tuple)):
         return [convert(item) for item in obj]
     if isinstance(obj, dict):
         return {convert(key):convert(value) for key, value in obj.items()}
     return obj

print("Content-Type: text/html;charset=utf-8\r\n\r\n")

print ("""
<!DOCTYPE html>
<html lang="en">
<title>Tech Support Analyzer Tool</title>
<head>
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
</style>

<script src="/json-browse/jquery-3.4.1.slim.js"></script>
<script src="/json-browse/jquery.json-browse.js"></script>
<link href="/json-browse/jquery.json-browse.css"rel="stylesheet">

<script type="text/javascript">

  window.onload=function(){
$('#json-renderer').jsonBrowse("""+str(a)+""",{
    collapsed: true
});
}
</script>
</head>

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

try:
    if config:
            #print("Avi Config found!  Processing.. ")
            print('<pre id="json-renderer" class="json-body"></pre>')
    else:
            print("<h3>\nAvi Config not found\n</h3>")
except:
    print("<h3>\nAVI Config not found\n</h3>")
#except Exception as e:
    #print(e)

print ("""
      </p>
    </div>

<!-- END MAIN -->
</div>
</body>
</html>
""")
