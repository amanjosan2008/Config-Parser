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

def se():
    print("<h3>\n############ SE INFO #############\n</h3>")
    for i in range(len(config["ServiceEngine"])):
        print('<table style="width:100%">')
        try:
            print("<tr><th>Name: </th><th>",config["ServiceEngine"][i]["name"],"</th></tr> ")
            print("<tr><td>State: </td><td>",config["ServiceEngine"][i]["enable_state"],"</td></tr>")
            print("<tr><td>Cloud: </td><td>", config["ServiceEngine"][i]["cloud_ref"].split('name=')[-1],"</td></tr>")
            print("<tr><td>SE Group: </td><td>",(re.findall(r'name=\w+', config["ServiceEngine"][i]["se_group_ref"]))[0].strip('name='),"</td></tr>")
            print("<tr><td>Tenant: </td><td>",config["ServiceEngine"][i]["tenant_ref"].split('name=')[-1],"</td></tr>")
            print("<tr><td>UUID: </td><td>",config["ServiceEngine"][i]["uuid"],"</td></tr>")
            print("<tr><td>Container Mode: </td><td>",config["ServiceEngine"][i]["container_mode"],"</td></tr>")
            print("<tr><td>Container Type: </td><td>",config["ServiceEngine"][i]["container_type"],"</td></tr>")
            print("<tr><td>Controller Created: </td><td>",config["ServiceEngine"][i]["controller_created"],"</td></tr>")
            try:
                print("<tr><td>Controller IP: </td><td>",config["ServiceEngine"][i]["controller_ip"],"</td></tr>")
            except:
                pass
            try:
                print("<tr><td>HB Misses: </td><td>",config["ServiceEngine"][i]["extension"]["hb_status"]["num_hb_misses"],"</td></tr>")
            except:
                pass
            try:
                print("<tr><td>Gateway UP: </td><td>",config["ServiceEngine"][i]["extension"]["gateway_up"],"</td></tr>")
            except:
                pass
            print("<tr><td>Inband Mgmt: </td><td>",config["ServiceEngine"][i]["extension"]["inband_mgmt"],"</td></tr>")
            try:
                print("<tr><td>Oper Status: </td><td>",config["ServiceEngine"][i]["extension"]["oper_status"]["state"],"</td></tr>")
            except:
                pass
            try:
                print("<tr><td>Oper Status Reason: </td><td>",config["ServiceEngine"][i]["extension"]["oper_status"]["reason"],"</td></tr>")
            except:
                pass
            print("<tr><td>SE Connected: </td><td>",config["ServiceEngine"][i]["extension"]["se_connected"],"</td></tr>")
            try:
                print("<tr><td>Power State: </td><td>",config["ServiceEngine"][i]["extension"]["power_state"],"</td></tr>")
            except:
                pass
            print("<tr><td>Version: </td><td>",config["ServiceEngine"][i]["extension"]["version"],"</td></tr>")
            print("<tr><td>Vinfra Discovered: </td><td>",config["ServiceEngine"][i]["extension"]["vinfra_discovered"],"</td></tr>")
            print("<tr><td>VNICs: </td><td> </td></tr>")
            try:
                for k in range(len(config["ServiceEngine"][i]["extension"]["vnic"])):
                    print("<tr><td>MAC: </td><td>",config["ServiceEngine"][i]["extension"]["vnic"][k]["mac_addr"],"</td></tr>")
                    print("<tr><td>State: </td><td>",config["ServiceEngine"][i]["extension"]["vnic"][k]["state"],"</td></tr>")
            except:
                print("<tr><td></td><td>Exception: Key not found</td></tr>")
            print("<tr><th>Management VNIC: </th><th></th></tr>")
            print("<tr><td>Linux Name: </td><td>",config["ServiceEngine"][i]["mgmt_vnic"]["linux_name"],"</td></tr>")
            print("<tr><td>Enabled: </td><td>",config["ServiceEngine"][i]["mgmt_vnic"]["enabled"],"</td></tr>")
            print("<tr><td>IF Name: </td><td>",config["ServiceEngine"][i]["mgmt_vnic"]["if_name"],"</td></tr>")
            print("<tr><td>VRF: </td><td>",(re.findall(r'name=\w+', config["ServiceEngine"][i]["mgmt_vnic"]["vrf_ref"]))[0].strip('name='),"</td></tr>")
            print("<tr><td>IP Address: </td><td>",config["ServiceEngine"][i]["mgmt_vnic"]["vnic_networks"][0]["ip"]["ip_addr"]["addr"],"</td></tr>")
            print("<tr><td>MAC Address: </td><td>",config["ServiceEngine"][i]["mgmt_vnic"]["mac_address"],"</td></tr>")
            print("<tr><th>Data VNICs: </th><th></th></tr>")
            for j in range(len(config["ServiceEngine"][i]["data_vnics"])):
                print("<tr><th>Linux Name: </th><th>",config["ServiceEngine"][i]["data_vnics"][j]["linux_name"],"</th></tr>")
                print("<tr><td>Enabled: </td><td>",config["ServiceEngine"][i]["data_vnics"][j]["enabled"],"</td></tr>")
                print("<tr><td>IF Name: </td><td>",config["ServiceEngine"][i]["data_vnics"][j]["if_name"],"</td></tr>")
                print("<tr><td>VRF: </td><td>",(re.findall(r'name=\w+', config["ServiceEngine"][i]["data_vnics"][j]["vrf_ref"]))[0].strip('name='),"</td></tr>")
                try:
                    print("<tr><td>IP Address: </td><td>",config["ServiceEngine"][i]["data_vnics"][j]["vnic_networks"][0]["ip"]["ip_addr"]["addr"],"</td></tr>")
                except:
                    pass
                print("<tr><td>MAC Address: </td><td>",config["ServiceEngine"][i]["data_vnics"][j]["mac_address"],"</td></tr>")
            try:
                print("<tr><td>VS: </td><td>", len(config["ServiceEngine"][i]["extension"]["vs_uuids"]),"</td></tr>")
                for l in range(len(config["ServiceEngine"][i]["extension"]["vs_uuids"])):
                    print("<tr><td>UUID:</td><td>",config["ServiceEngine"][i]["extension"]["vs_uuids"][l],"</td></tr>")
            except:
                print("<tr><td>VS UUIDs:</td><td> Key not found</td></tr>")
        except Exception as e:
            print("<tr><td>Exception:</td><td>",e,'</td></tr>')
        print('<table')
        print('<br /><br />')

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
            se()
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
