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

#Avi Config Loader
for i in dirlist:
    if i.split('/')[-1] == "avi_config":
        f = open(i,'r')
        config = json.load(f)
        f.close


def lic():
    print("<h3>\n############ LICENSE INFO #############\n</h3>")
    print("<p>Max SEs: ", config["ControllerLicense"][0]["max_ses"],'</p>\n')
    a = 1
    try:
      for j in range(len(config["ControllerLicense"][0]["extension"]["used_license_resources"])):
        if config["ControllerLicense"][0]["extension"]["used_license_resources"][j]['license_type'] == 'LIC_CORES':
            print("Used Cores: LIC",a, ":" ,config["ControllerLicense"][0]["extension"]["used_license_resources"][j]['used_count'],"<br />")
            a += 1
    except Exception as e:
         #print("Exception: ", e,"<br />")
         pass
    print('\n')

    for k in range(len(config["ControllerLicense"][0]["licenses"])):
        print('<table style="width:100%">')
        print("<tr><th>License File Name:</th><th>", config["ControllerLicense"][0]["licenses"][k]["license_name"],"</th></tr>")
        print("<tr><td>Customer Name:</td><td>", config["ControllerLicense"][0]["licenses"][k]["customer_name"],"</td></tr>")
        print("<tr><td>License ID:</td><td>", config["ControllerLicense"][0]["licenses"][k]["license_id"],"</td></tr>")
        print("<tr><td>License Type:</td><td>", config["ControllerLicense"][0]["licenses"][k]["license_type"],"</td></tr>")
        print("<tr><td>Tier Type:</td><td>", config["ControllerLicense"][0]["licenses"][k]["tier_type"],"</td></tr>")
        print("<tr><td>Valid Till:</td><td>", config["ControllerLicense"][0]["licenses"][k]["valid_until"],"</td></tr>")
        try:
            print("<tr><td>Max SEs:</td><td>", config["ControllerLicense"][0]["licenses"][k]["max_ses"],"</td></tr>")
        except Exception as e:
            #print("Exception: ", e,"<br />")
            pass
        try:
            print("<tr><td>Sockets:</td><td>", config["ControllerLicense"][0]["licenses"][k]["sockets"],"</td></tr>")
        except Exception as e:
            #print("Exception: ", e,"<br />")
            pass
        try:
            print("<tr><td>Cores:</td><td>", config["ControllerLicense"][0]["licenses"][k]["cores"],"</td></tr>")
        except Exception as e:
            #print("Exception: ", e,"<br />")
            pass
        print("</table><br/>")


try:
    if config:
        #print("Avi Config found!  Processing.. ")
        try:
            lic()
        except Exception as e:
            print("Exception: ",e,"<br /><br />")
    else:
        print("<h3>\nAvi Config not found\n</h3>")
except:
    print("<h3>\nAVI Config not found\n</h3>")


print("<h3>\n############ DONE #############\n</h3>")

print ("""
      </p>
    </div>

<!-- END MAIN -->
</div>
</body>
</html>
""")
