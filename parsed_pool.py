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


def pool():
    print("<h3>\n############ POOL INFO #############\n</h3>")
    for m in range(len(config["Pool"])):
        print('<table style="width:100%">')
        print("<tr><th>Name: </th><th>",config["Pool"][m]["name"],"</th></tr>")
        print("<tr><td>Enabled: </td><td>",config["Pool"][m]["enabled"],"</td></tr>")
        print("<tr><td>Max concurrent conns per server: </td><td>",config["Pool"][m]["max_concurrent_connections_per_server"],"</td></tr>")
        print("<tr><td>UUID: </td><td>",config["Pool"][m]["uuid"],"</td></tr>")
        print("<tr><td>LB Algorithm: </td><td>",config["Pool"][m]["lb_algorithm"],"</td></tr>")
        print("<tr><td>Default server port: </td><td>",config["Pool"][m]["default_server_port"],"</td></tr>")
        print("<tr><td>Tenant Ref: </td><td>",config["Pool"][m]["tenant_ref"].split('name=')[-1],"</td></tr>")
        print("<tr><td>VRF Ref: </td><td>",(re.findall(r'name=\w+', config["Pool"][m]["vrf_ref"]))[0].strip('name='),"</td></tr>")
        print("<tr><td>Cloud Ref: </td><td>",config["Pool"][m]["cloud_ref"].split('name=')[-1],"</td></tr>")
        print("<tr><td>SNI enabled: </td><td>",config["Pool"][m]["sni_enabled"],"</td></tr>")
        print("<tr><td>Rewrite host header to server name: </td><td>",config["Pool"][m]["rewrite_host_header_to_server_name"],"</td></tr>")
        print("<tr><td>Rewrite host header to sni: </td><td>",config["Pool"][m]["rewrite_host_header_to_sni"],"</td></tr>")
        print("<tr><td>Health Monitor Refs: </td><td>","</td></tr>")
        try:
            for o in range(len(config["Pool"][m]["health_monitor_refs"])):
                print("<tr><td> </td><td>", config["Pool"][m]["health_monitor_refs"][o].split('name=')[-1],"</td></tr>")
        except KeyError:
            print("<tr><td> </td><td>No Health Monitors attached to this Pool","</td></tr>")
        print("<tr><td>Inline health monitor: </td><td>",config["Pool"][m]["inline_health_monitor"],"</td></tr>")

        try:
            print("<tr><td>Server count: </td><td>",config["Pool"][m]["server_count"],"</td></tr>")
            cnt = int(config["Pool"][m]["server_count"])
        except KeyError:
            print("<tr><td>Server count: </td><td>", len(config["Pool"][m]["servers"]),"</td></tr>")
            cnt = len(config["Pool"][m]["servers"])
        #print(cnt)
        if cnt > 0:
            print("<tr><td>Servers Info: </td><td> </td></tr>")
            for n in range(len(config["Pool"][m]["servers"])):
                print("<tr><th>Hostname:</th><th>", config["Pool"][m]["servers"][n]['hostname'],"</th></tr>")
                print("<tr><td>IP Address:</td><td>", config["Pool"][m]["servers"][n]['ip']['addr'],"</td></tr>")
                try:
                    print("<tr><td>Port:</td><td>", config["Pool"][m]["servers"][n]['port'],"</td></tr>")
                except:
                    print("<tr><td>Port: </td><td>Inherited")
                print("<tr><td>Status:</td><td>", config["Pool"][m]["servers"][n]['enabled'],"</td></tr>")
                print("<tr><td>Ratio:</td><td>", config["Pool"][m]["servers"][n]['ratio'],"</td></tr>")
                print("<tr><td>Rewrite Host Header:</td><td>", config["Pool"][m]["servers"][n]['rewrite_host_header'],"</td></tr>")
        else:
            print("<tr><td>Servers: </td><td>No Server attached to this Pool","</td></tr>")
            #pass
        #except Exception as e:
            #print("EXCEPTION OCCURED:", e,"<br />")
        print("<br />")

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
            pool()
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
