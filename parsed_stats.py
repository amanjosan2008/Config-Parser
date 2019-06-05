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
#path_form = form.getvalue('path')
#path = path_form.strip('&path=path')
#print(path_form)
#print(path)

dirlist = []

for root,dirc,files in os.walk(path):
    for filename in files:
       dirlist.append(os.path.join(os.path.realpath(root),filename))

# Untar log Files
#tech_node1.controller.local-172.30.41.40
#tech_node2.controller.local-172.30.41.41
#tech_node3.controller.local-172.30.41.42

#debuglogs.20190410-152417.tar.gz
#serviceengine_Avi-se-mwvab.20190410-152152.tar.gz
#serviceengine_Avi-se-oakck.20190410-152302.tar.gz

##tech_node*.controller.local-*
##debuglogs.*.tar.gz
##serviceengine_*.tar.gz

#print("<h2>Results for %s</h2>") % (path)

# Avi Config Parser
def clouds():
    print("<h3>\n############ DEPLOYMENT STATS #############\n</h3>")

    print("<h4>No of Clouds in Avi: ",len(config["Cloud"]),"</h4>")
    print('<table style="width:100%">')
    print("<tr><th>Cloud Name</th> <th>Cloud Type</th> </tr>")
    for i in range(len(config["Cloud"])):
        #print(config["Cloud"][l],'\n')
        print("<tr><td>",str(i+1) + '.', config["Cloud"][i]["name"],'</td><td>'+ str(config["Cloud"][i]["vtype"]), "</td></tr>")
    print('</table>')
    print("<br />")


def se():
    print("<h4>No of SEs in Avi: ",len(config["ServiceEngine"]),"</h4>")
    print('<table style="width:100%">')
    print("<tr><th>SE Name</th><th>SE Group</th><th>Tenant</th><th>Cloud Name</th></tr>")
    for i in range(len(config["ServiceEngine"])):
        print("<tr><td>",config["ServiceEngine"][i]["name"],"</td><td>",((re.findall(r'name=.*&', config["ServiceEngine"][i]["se_group_ref"]))[0].strip('name=')).strip('&'),"</td><td>", config["ServiceEngine"][i]["tenant_ref"].split('name=')[-1],"</td><td>", config["ServiceEngine"][i]["cloud_ref"].split('name=')[-1],"</td></tr>")
    print('</table>')
    print("<br />")

'''
def se():
    print("<h4>No of SEs in Avi: ",len(config["ServiceEngine"]),"</h4>")
    print('<table style="width:100%">')
    print("<tr><th> SE Name </th></tr>")
    for j in range(len(config["ServiceEngine"])):
        print("<tr><td>",str(j+1) + '.', config["ServiceEngine"][j]["name"],"</tr></td>")
    print('</table>')
    print("<br />")

def se_cloud():
    print("<h4>No of SEs in each Cloud: </h4><br />")
    for k in range(len(config["Cloud"])):
        c = 0
        #print(config["Cloud"][l],'\n')
        print(config["Cloud"][k]["name"],":<br />")
        print('<table style="width:100%">')
        #print("<tr><th> SE Name </th></tr>")
        for m in range(len(config["ServiceEngine"])):
            if config["Cloud"][k]["name"] == config["ServiceEngine"][m]["cloud_ref"].split('name=')[-1]:
                print("<tr><td>",str(m+1) + '.', config["ServiceEngine"][m]["name"],"</tr></td>")
                c += 1
        print('</table>')
        if c == 0:
            print('<table style="width:100%">')
            print("<tr><td>No SE in this Cloud</tr></td>")
            print('</table>')
        print("<br />")
    print("<br />")
'''

def vs():
    print("<h4>No of VSs in Avi: ",len(config["VirtualService"]),"</h4>")
    print('<table style="width:100%">')
    print("<tr><th>VS Name</th><th>SE Group</th><th>VRF Context</th><th>Tenant</th><th>Cloud Name</th></tr>")
    for i in range(len(config["VirtualService"])):
        print("<tr><td>",config["VirtualService"][i]["name"],"</td><td>",((re.findall(r'name=.*&', config["VirtualService"][i]["se_group_ref"]))[0].strip('name=')).strip('&'),"</td><td>", ((re.findall(r'name=.*&', config["VirtualService"][i]["vrf_context_ref"]))[0].strip('name=')).strip('&'), "</td><td>",config["VirtualService"][i]["tenant_ref"].split('name=')[-1],"</td><td>", config["VirtualService"][i]["cloud_ref"].split('name=')[-1],"</td></tr>")
    print('</table>')
    print("<br />")


'''
def vs():
    print("<h4>No of VSs in Avi: ",len(config["VirtualService"]),"</h4>")
    print('<table style="width:100%">')
    for l in range(len(config["VirtualService"])):
        print("<tr><td>",str(l+1) + '.</td><td>', config["VirtualService"][l]["name"],"</td></tr>")
    print('</table>')
    print("<br />")


def vs_cloud():
    print("<h4>No of VSs in each Cloud: </h4><br />")
    for m in range(len(config["Cloud"])):
        d=0
        print(config["Cloud"][m]["name"],"<br />")
        print('<table style="width:100%">')
        for n in range(len(config["VirtualService"])):
            if config["Cloud"][m]["name"] == config["VirtualService"][n]["cloud_ref"].split('name=')[-1]:
                print("<tr><td>", str(d+1) + '.</td><td>' ,config["VirtualService"][n]["name"],"</td></tr>")
                d += 1
        print('</table>')
        if d==0:
            print('<table style="width:100%">')
            print("<tr><td>","No VS in this Cloud","</td></tr>")
            print('</table>')
        print("<br />")
    print("<br />")
'''

def vs_se():
    print("<h4>No of VSs on each SE: </h4><br />")
    e = []
    for i in range(len(config["ServiceEngine"])):
        f = 0
        print("<h3>SE: ", config["ServiceEngine"][i]["name"],"</h3>")
        print('<table style="width:100%">')
        for j in range(len(config["VirtualService"])):
            try:
                for k in range(len(config["VirtualService"][j]["extension"]["vip_runtime"][0]["se_list"])):
                    if config["ServiceEngine"][i]["uuid"] == (config["VirtualService"][j]["extension"]["vip_runtime"][0]["se_list"][k]["se_ref"]).split('/')[-1]:
                        print("<tr><td>", str(f+1) + '. </td><td>',config["VirtualService"][j]["name"],"</td></tr>")
                        f += 1
            except KeyError:
                #print("no SE:", config["VirtualService"][j]["name"])
                e.append(config["VirtualService"][j]["name"])
        print('</table>')
        print("<br />")
        print("Total: ",f,"<br />")
        print("<br />")
    print("<br />")
    se_less_vs = set(e)
    print("<h3>VSs without any SE:",len(se_less_vs),"</h3>")
    print('<table style="width:100%">')
    g = 1
    for o in se_less_vs:
        print('<tr><td>', str(g)+'. </td><td>'+ o,"</td></tr>")
        g += 1
    print('</table>')
    print("<br />")


'''
def pool_vs:
    print("<h4>No of Pools for each VS: </h4><br />")
    # THIS IS NOT SHOWING SERVERS in a POOL
    for i in range(len(config["VirtualService"])):
   try:
       print(config["VirtualService"][i]["name"],':', (config["VirtualService"][i]["pool_ref"].split("name=")[-1]).split('&')[0])
   except:
       pass
    print("<br />")
'''

'''
def se_segroup():
    ## ADD UUID or match Cloud too
    print("<h4>No of SEs in each SE Group: </h4><br />")
    for i in range(len(config["ServiceEngineGroup"])):
        g = 0
        print(config["ServiceEngineGroup"][i]["name"], '(Cloud:'+str(config["ServiceEngineGroup"][i]["cloud_ref"].split('name=')[-1])+')',"<br />")
        print('<table style="width:100%">')
        for j in range(len(config["ServiceEngine"])):
            if ((re.findall(r'name=.*&', config["ServiceEngine"][j]["se_group_ref"]))[0].strip('name=')).strip('&') == config["ServiceEngineGroup"][i]["name"]:
                print("<tr><td>", str(g+1) + '.',config["ServiceEngine"][j]["name"],"</tr></td>")
                g += 1
        print('</table>')
        if g == 0:
            print('<table style="width:100%">')
            print("<tr><td>","No SE in this SE Group","</td></tr>")
            print('</table>')
        print("<br />")
    #for i in range(len(config["ServiceEngine"])):
        #for j in range(len(config["ServiceEngineGroup"])):
            #if (re.findall(r'name=\w+', config["ServiceEngine"][i]["se_group_ref"]))[0].strip('name=') == config["ServiceEngineGroup"][k]["name"]:
                #print((re.findall(r'name=\w+', config["ServiceEngine"][i]["se_group_ref"]))[0].strip('name='), config["ServiceEngineGroup"][k]["name"],"<br />")

    print("<br />")
'''

''' print("<h4>No of SEs in each SE Group: </h4><br />")
    for i in range(len(config["ServiceEngineGroup"])):
        g = 0
        print(config["ServiceEngineGroup"][i]["name"], '(Cloud:'+str(config["ServiceEngineGroup"][i]["cloud_ref"].split('name=')[-1])+')',"<br />")
        print('<table style="width:100%">')
        for j in range(len(config["ServiceEngine"])):
            if ((re.findall(r'name=.*&', config["ServiceEngine"][j]["se_group_ref"]))[0].strip('name=')).strip('&') == config["ServiceEngineGroup"][i]["name"]:
                print("<tr><td>", str(g+1) + '.',config["ServiceEngine"][j]["name"],"</tr></td>")
                g += 1
        print('</table>')
        if g == 0:
            print('<table style="width:100%">')
            print("<tr><td>","No SE in this SE Group","</td></tr>")
            print('</table>')
        print("<br />")
'''

def vs():
    print("<h4>No of VSs having Real Time Metrics Enabled: </h4>")
    print('<table style="width:100%">')
    print("<tr><th>VS Name</th><th>Realtime Metrics</th></tr>")
    c = 1
    for i in range(len(config["VirtualService"])):
        try:
            if config["VirtualService"][i]["analytics_policy"]["metrics_realtime_update"]["enabled"] == True:
                print("<tr><td>", str(c)+'.' ,config["VirtualService"][i]["name"],"</td><td>",config["VirtualService"][i]["analytics_policy"]["metrics_realtime_update"]["enabled"],"</td></tr>")
                c += 1
        except:
            pass

    print('</table>')
    print("<br />")

def tenant():
    print("<h4>No of Tenant:",len(config["Tenant"]),"</h4><br />")
    print('<table style="width:100%">')
    for i in range(len(config["Tenant"])):
        print("<tr><td>",i+1,".</td><td>",config["Tenant"][i]["name"],"</td></tr>")
    print('</table>')

#Avi Config Loader
for i in dirlist:
    if i.split('/')[-1] == "avi_config":
        f = open(i,'r')
        config = json.load(f)
        f.close
try:
    if config:
        #print("Avi Config found!  Processing.. ")
        clouds()
        se()
        vs()
        vs_se()
        tenant()
        print("<h3>\n############ DONE #############\n</h3>")
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
