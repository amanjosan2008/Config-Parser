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

def segroup():
    print("<h3>\n############ SE GROUP INFO #############\n</h3>")
    for i in range(len(config["ServiceEngineGroup"])):
        try:
            print('<table style="width:100%">')
            print("<tr><th>SE Group: </th><th>",config["ServiceEngineGroup"][i]["name"],"</th></tr>")
            print("<tr><td>Cloud: </td><td>",config["ServiceEngineGroup"][i]["cloud_ref"].split('name=')[-1],"</td></tr>")
            print('<tr><td>Tenant Ref: </td><td>',config["ServiceEngineGroup"][i]['tenant_ref'].split('name=')[-1],"</td></tr>")
            try:
                print('<tr><td>Accelerated Networking: </td><td>',config["ServiceEngineGroup"][i]['accelerated_networking'],"</td></tr>")
            except:
                print('<tr><td>Accelerated Networking: </td><td>N.A. ',"</td></tr>")
            print('<tr><td>Algo: </td><td>',config["ServiceEngineGroup"][i]['algo'],"</td></tr>")
            print('<tr><td>Auto Rebalance: </td><td>',config["ServiceEngineGroup"][i]['auto_rebalance'],"</td></tr>")
            if config["ServiceEngineGroup"][i]['auto_rebalance'] == "True":
                print('<tr><td>Auto Rebalance Capacity Per SE: </td><td>',config["ServiceEngineGroup"][i]['auto_rebalance_capacity_per_se'],"</td></tr>")
                print('<tr><td>Auto Rebalance Criteria: </td><td>',config["ServiceEngineGroup"][i]['auto_rebalance_criteria'],"</td></tr>")
            print('<tr><td>Buffer SE: </td><td>',config["ServiceEngineGroup"][i]['buffer_se'],"</td></tr>")
            print('<tr><td>CPU Reserve: </td><td>',config["ServiceEngineGroup"][i]['cpu_reserve'],"</td></tr>")
            print('<tr><td>CPU Socket Affinity: </td><td>',config["ServiceEngineGroup"][i]['cpu_socket_affinity'],"</td></tr>")
            print('<tr><td>Dedicated Dispatcher Core: </td><td>',config["ServiceEngineGroup"][i]['dedicated_dispatcher_core'],"</td></tr>")
            print('<tr><td>Disk per SE: </td><td>',config["ServiceEngineGroup"][i]['disk_per_se'],"</td></tr>")
            print('<tr><td>Max CPU Usage: </td><td>',config["ServiceEngineGroup"][i]['max_cpu_usage'],"</td></tr>")
            print('<tr><td>Max VS per SE: </td><td>',config["ServiceEngineGroup"][i]['max_vs_per_se'],"</td></tr>")
            print('<tr><td>Min Scaleout per VS: </td><td>',config["ServiceEngineGroup"][i]['min_scaleout_per_vs'],"</td></tr>")
            print('<tr><td>Min SE: </td><td>',config["ServiceEngineGroup"][i]['min_se'],"</td></tr>")
            print('<tr><td>Per App: </td><td>',config["ServiceEngineGroup"][i]['per_app'],"</td></tr>")
            print('<tr><td>Placement Mode: </td><td>',config["ServiceEngineGroup"][i]['placement_mode'],"</td></tr>")
            print('<tr><td>SE Bandwidth Type: </td><td>',config["ServiceEngineGroup"][i]['se_bandwidth_type'],"</td></tr>")
            print('<tr><td>SE Name Prefix: </td><td>',config["ServiceEngineGroup"][i]['se_name_prefix'],"</td></tr>")
            print('<tr><td>VCenter Folder: </td><td>',config["ServiceEngineGroup"][i]['vcenter_folder'],"</td></tr>")
            print('<tr><td>VCPUs per SE: </td><td>',config["ServiceEngineGroup"][i]['vcpus_per_se'],"</td></tr>")
        except Exception as e:
            print("<tr><td>EXCEPTION OCCURED:</td><td>", e,"</td></tr>")
            pass
        print('<br />')
#Avi Config Loader
for i in dirlist:
    if i.split('/')[-1] == "avi_config":
        f = open(i,'r')
        config = json.load(f)
        f.close
try:
    if config:
        #print("Avi Config found!  Processing.. ")
        try:
            segroup()
            print("<h3>\n############ DONE #############\n</h3>")
        except Exception as e:
            print("Exception: ",e,"<br /><br />")
    else:
        print("<h3>\nAvi Config not found\n</h3>")
except:
    print("<h3>\nAVI Config not found\n</h3>")


print ("""
      </p>
    </div>

<!-- END MAIN -->
</div>
</body>
</html>
""")
