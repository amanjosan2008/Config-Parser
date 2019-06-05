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

def vs():
    print("<h3>\n############ VS INFO #############\n</h3>")
    for i in range(len(config["VirtualService"])):
        print('<table style="width:100%">')
        print("<tr><th>Name: </th><th>",config["VirtualService"][i]["name"],"</th></tr>")
        print("<tr><td>Enabled: </td><td>",config["VirtualService"][i]["enabled"],"</td></tr>")
        print("<tr><td>Cloud Type: </td><td>",config["VirtualService"][i]["cloud_type"],"</td></tr>")
        print("<tr><td>Cloud Name: </td><td>",config["VirtualService"][i]["cloud_ref"].split('name=')[-1],"</td></tr>")
        print("<tr><td>Application Profile: </td><td>",config["VirtualService"][i]["application_profile_ref"].split('name=')[-1],"</td></tr>")
        print("<tr><td>Network Profile: </td><td>",config["VirtualService"][i]["network_profile_ref"].split('name=')[-1],"</td></tr>")
        try:
            print("<tr><td>Pool: </td><td>",(config["VirtualService"][i]["pool_ref"].split("name=")[-1]).split('&')[0],"</td></tr>")
        except:
            print("<tr><td>Pool:</td><td> N.A. </td></tr>")
        try:
            #print("Pool Group: ",config["VirtualService"][i]["pool_group_ref"],"<br />")
            print("<tr><td>Pool Group: </td><td>", (re.findall(r'name=\w+', config["VirtualService"][i]["pool_group_ref"]))[0].strip('name='),"</td></tr>")
        except:
            print("<tr><td>Pool Group: </td><td>N.A. </td></tr>")
        try:
            print("<tr><td>Client Insights: </td><td>",config["VirtualService"][i]["analytics_policy"]["client_insights"],"</td></tr>")
        except:
            print("<tr><td>Client Insights: </td><td>N.A.</td></tr>")
        try:
            print("<tr><td>Full Client Logs Enabled: </td><td>",config["VirtualService"][i]["analytics_policy"]["full_client_logs"]["enabled"],"</td></tr>")
        except:
            print("<tr><td>Full Client Logs Enabled: </td><td>N.A. ", "</td></tr>")
        try:
            print("<tr><td>Log All Headers: </td><td>",config["VirtualService"][i]["analytics_policy"]["full_client_logs"]["all_headers"],"</td></tr>")
        except:
            print("<tr><td>Log All Headers: </td><td>N.A.", "</td></tr>")
        try:
            print("<tr><td>Realtime Metrics Enabled: </td><td>",config["VirtualService"][i]["analytics_policy"]["metrics_realtime_update"]["enabled"],"</td></tr>")
        except:
            print("<tr><td>Realtime Metrics Enabled: </td><td>N.A.", "</td></tr>")
        print("<tr><td>Active Standby SE Tag: </td><td>",config["VirtualService"][i]["active_standby_se_tag"],"</td></tr>")
        try:
            print("<tr><td>Is Primary: </td><td>",config["VirtualService"][i]["is_primary"],"</td></tr>")
            print("<tr><td>Is Secondary: </td><td>",config["VirtualService"][i]["is_standby"],"</td></tr>")
        except:
            print("<tr><td>Is Primary: </td><td>N.A.","</td></tr>")
            print("<tr><td>Is Secondary: </td><td>N.A.","</td></tr>")
        print("<tr><td>Tenant: </td><td>",config["VirtualService"][i]["tenant_ref"].split('name=')[-1],"</td></tr>")
        print("<tr><td>Additional SE: </td><td>",config["VirtualService"][i]["extension"]["vip_runtime"][0]["num_additional_se"],"</td></tr>")
        print("<tr><td>VIP: </td><td>", (config["VirtualService"][i]["vsvip_ref"].split("name=")[-1]).split('&')[0],"</td></tr>")

        print('<tr><td colspan="2"> SEs assigned to this VS:  </td></tr>')
        try:
            for j in range(len(config["VirtualService"][i]["extension"]["vip_runtime"][0]["se_list"])):
                for k in range(len(config["ServiceEngine"])):
                    if (config["VirtualService"][i]["extension"]["vip_runtime"][0]["se_list"][j]["se_ref"]).split('/')[-1] == config["ServiceEngine"][k]["uuid"]:
                        print("<tr><td> </td><td>", config["ServiceEngine"][k]["name"],'('+ str(config["VirtualService"][i]["extension"]["vip_runtime"][0]["se_list"][j]["vcpus"]),"VCPU)</td></tr>")
            #print("</table>")
                #print(" - ",(config["VirtualService"][i]["extension"]["vip_runtime"][0]["se_list"][j]["se_ref"]).split('/')[-1],'('+ str(config["VirtualService"][i]["extension"]["vip_runtime"][0]["se_list"][j]["vcpus"]),"VCPU)<br />")
        except KeyError:
            #print('<table style="width:100%">')
            print("<tr><td> </td><td>No SE assigned for this VS</td></tr>")
            #print("</table>")

        print('<tr><td colspan="2">Services: </td></tr>')
        #print('<table style="width:100%">')
        for k in range(len(config["VirtualService"][i]["services"])):
            print("<tr><td> </td><td>", config["VirtualService"][i]["services"][k]["port"], "(SSL: ", config["VirtualService"][i]["services"][k]["enable_ssl"],")","</td></tr>")
        print("</table>")
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
            vs()
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
