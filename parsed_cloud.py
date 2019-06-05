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


# Avi Config Parser
def cloud():
    print("<h3>\n############ CLOUDS INFO #############\n</h3>")
    for l in range(len(config["Cloud"])):
        #print(config["Cloud"][l],'\n')
        print('<table style="width:100%">')
        print("<tr><th>Cloud Name:</th><th>", config["Cloud"][l]["name"],"</th></tr>")
        print("<tr><td>Cloud Type:</td><td>", config["Cloud"][l]["vtype"],"</td></tr>")
        print("<tr><td>Cloud UUID:</td><td>", config["Cloud"][l]["uuid"],"</td></tr>")
        print("<tr><td>Tenant:</td><td>", config["Cloud"][l]["tenant_ref"].split('name=')[-1],"</td></tr>")
        print("<tr><td>DHCP Enabled:</td><td>", config["Cloud"][l]["dhcp_enabled"],"</td></tr>")
        b = 1
        if config["Cloud"][l]["vtype"] == "CLOUD_LINUXSERVER":
            for k,v in config["Cloud"][l]["linuxserver_configuration"].items():
                if k == "ssh_user_ref":
                    print("<tr><td>SSH User Ref: </td><td>", config["Cloud"][l]["linuxserver_configuration"]["ssh_user_ref"].split('name=')[-1],"</td></tr>")
                elif k != "hosts":
                    print("<tr><td>",k,'</td><td>',v,"</td></tr>")
                else:
                    for m in range(len(v)):
                        print("<tr><td>LSC: </td><td>", b,"</td></tr>")
                        b += 1
                        print("<tr><td>IP Address: </td><td>", v[m]["host_ip"]["addr"],"</td></tr>")
                        for n in range(len(v[m]["host_attr"])):
                            print("<tr><td>",v[m]["host_attr"][n]['attr_key'], ": </td><td>",v[m]["host_attr"][n]['attr_val'],"</td></tr>")

        elif config["Cloud"][l]["vtype"] == "CLOUD_VCENTER":
            print("<tr><td>Vcenter Username: </td><td>", config["Cloud"][l]["vcenter_configuration"]['username'],"</td></tr>")
            print("<tr><td>DataCenter: </td><td>", config["Cloud"][l]["vcenter_configuration"]['datacenter'],"</td></tr>")
            print("<tr><td>Privilege: </td><td>", config["Cloud"][l]["vcenter_configuration"]['privilege'],"</td></tr>")
            print("<tr><td>Vcenter URL: </td><td>", config["Cloud"][l]["vcenter_configuration"]['vcenter_url'],"</td></tr>")
            print("<tr><td>No of Subnets Discovered:</td><td>", len(config["Network"]),"</td></tr>")

        elif config["Cloud"][l]["vtype"] == "CLOUD_OSHIFT_K8S":
            print("<tr><td>Function under constrution for Cloud Type:</td><td>", config["Cloud"][l]["vtype"],"</td></tr>")

        elif config["Cloud"][l]["vtype"] == "CLOUD_NONE":
            print("<tr><td>Function under constrution for Cloud Type:</td><td>", config["Cloud"][l]["vtype"],"</td></tr>")

        else:
            print("<tr><td>Function under constrution for Cloud Type:</td><td>", config["Cloud"][l]["vtype"],"</td></tr>")


        print('</table>')
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
            cloud()
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
