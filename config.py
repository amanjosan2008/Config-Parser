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
option = form.getvalue('option')

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

def convert(obj):
     if isinstance(obj, bool):
         return str(obj).lower()
     if isinstance(obj, (list, tuple)):
         return [convert(item) for item in obj]
     if isinstance(obj, dict):
         return {convert(key):convert(value) for key, value in obj.items()}
     return obj

try:
    if option == "SE":
        cfg = str(convert(config["ServiceEngine"]))
    elif option == "VS":
        cfg = str(convert(config["VirtualService"]))
    elif option == "Cloud":
        cfg = str(convert(config["Cloud"]))
    elif option == "VIP":
        cfg = str(convert(config["VsVip"]))
    elif option == "Pool":
        cfg = str(convert(config["Pool"]))
    elif option == "SEGroup":
        cfg = str(convert(config["ServiceEngineGroup"]))
    elif option == "GSLB":
        cfg = str(convert(config["Gslb"]))
    elif option == "GSLBSite":
        cfg = str(convert(config["GslbSite"]))
    elif option == "PoolGroup":
        cfg = str(convert(config["PoolGroup"]))
    elif option == "WafProfile":
        cfg = str(convert(config["WafProfile"]))
    elif option == "Tenant":
        cfg = str(convert(config["Tenant"]))
    elif option == "Meta":
        cfg = str(convert(config["META"]))
    else:
        cfg = str(["Wrong Key: Config "+ option +" not Found." ])
except KeyError:
    cfg = str(["KeyError: Key - "+ option +" not Found in Config." ])
except NameError:
    cfg = str(["NameError: Config file not Found in the above path." ])

#if cfg == "[]":
#    cfg = str(["Error: Key - "+ option +" not Found in Config." ])


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

<script src="/tech_support/json-browse/jquery-3.4.1.slim.js"></script>
<script src="/tech_support/json-browse/jquery.json-browse.js"></script>
<link href="/tech_support/json-browse/jquery.json-browse.css"rel="stylesheet">
<script type="text/javascript">
$(function() {
  $('#btn-json-browse').click(function() {
    var options = {
      collapsed: $('#collapsed').is(':checked'),
      withQuotes: $('#with-quotes').is(':checked')
    };
    $('#json-renderer').jsonBrowse("""+cfg+""", options);
  });
  // Display JSON sample on load
  $('#btn-json-browse').click();
});
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

print("Logs:&nbsp;&nbsp;&nbsp;", path,"<br/>")
print("Config:&nbsp;", option,"<br/>")

print("""<p>
          Options:&nbsp;&nbsp;
            <label><input type="checkbox" id="collapsed" checked /> Collapse&nbsp;&nbsp;</label>
            <label><input type="checkbox" id="with-quotes" /> Quotes</label><br/>
         </p>
         <button id="btn-json-browse" title="run jsonBrowse()">Update</button>""")

try:
    if config:
        #print("Avi Config found!  Processing.. ")
        if cfg == "[]":
            print("<h3>\n", option , "Config not found\n</h3>")
        else:
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
