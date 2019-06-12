#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb

print ("Content-type:text/html\r\n\r\n")
print ("""
<!DOCTYPE html>
<html lang="en">

<title>Tech Support Analyzer Tool</title>
 <head>
  <script type="text/javascript">
    function select() {
        var1=document.getElementById("radio1");
        var2=document.getElementById("radio2");
        var3=document.getElementById("radio3");
        var4=document.getElementById("radio4");
        var5=document.getElementById("radio5");
        var6=document.getElementById("radio6");
        var7=document.getElementById("radio7");
        var8=document.getElementById("radio8");
        var9=document.getElementById("radio9");
        var10=document.getElementById("radio10");
        var11=document.getElementById("radio11");
        var12=document.getElementById("radio12");
        var13=document.getElementById("radio13");
        var14=document.getElementById("radio14");
        var15=document.getElementById("radio15");
        var16=document.getElementById("radio16");
        var17=document.getElementById("radio17");
        var18=document.getElementById("radio18");
        var19=document.getElementById("radio19");
        var23=document.getElementById("radio23");
        var24=document.getElementById("radio24");
        var25=document.getElementById("radio25");
        var26=document.getElementById("radio26");
        if(var1.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_stats.py";
        }
        else if(var2.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_cloud.py";
        }
        else if(var3.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_vs.py";
        }
        else if(var4.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_vip.py";
        }
        else if(var5.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_pool.py";
        }
        else if(var6.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_se.py";
        }
        else if(var7.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_segroup.py";
        }
        else if(var8.checked==true)
        {
            document.myform.action="/cgi-bin/parsed_gslb.py";
        }
        else if(var9.checked==true)
        {
            document.myform.action="/cgi-bin/version.py";
        }
        else if(var10.checked==true)
        {
            document.myform.action="/cgi-bin/license.py";
        }
        else if(var11.checked==true||var12.checked==true||var13.checked==true||var14.checked==true||var15.checked==true||var16.checked==true||var17.checked==true||var18.checked==true||var23.checked==true||var24.checked==true||var25.checked==true|var26.checked==true)
        {
            document.myform.action="/cgi-bin/config.py";
        }
        else if(var19.checked==true)
        {
            document.myform.action="/cgi-bin/config_full.py";
        }
        else
        {
            document.myform.action="/cgi-bin/error.py";
        }
   }
  </script>
</head>

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

* {
  box-sizing: border-box;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 33.3%;
  padding: 10px;
  height: 350px; /* Should be removed. Only for demonstration */
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
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

      <form action="/cgi-bin/parsed_stats.py" method="get" name="myform" onsubmit="select()">
            <h4>Logs Location: <input type = "text" name = "path" maxlength="200" size="100" required >  <br /></h4>
            <div class="row">
              <div class="column" style="background-color:#aaa;">
                <h5>Parse Config</h5>
                <input type="radio" id="radio1" name = "option" value = "Stats"> Deployment Stats <br />
                <input type="radio" id="radio2" name = "option" value = "Clouds"> Cloud <br />
                <input type="radio" id="radio3" name = "option" value = "Virtual Service"> Virtual Service <br />
                <input type="radio" id="radio4" name = "option" value = "VIPs"> VIP <br />
                <input type="radio" id="radio5" name = "option" value = "Pools"> Pool <br />
                <input type="radio" id="radio6" name = "option" value = "Service Engine"> Service Engine <br />
                <input type="radio" id="radio7" name = "option" value = "SE Group"> SE Group <br />
                <input type="radio" id="radio8" name = "option" value = "GSLBs"> GSLB <br />
              </div>
              <div class="column" style="background-color:#bbb;">
                <h5>Dump Config</h5>
                <input type="radio" id="radio19" name = "option" value = "Full"> Config Full(WIP) <br />
                <input type="radio" id="radio12" name = "option" value = "Cloud"> Cloud <br />
                <input type="radio" id="radio11" name = "option" value = "VS"> Virtual Service <br />
                <input type="radio" id="radio18" name = "option" value = "VIP"> VIP <br />
                <input type="radio" id="radio14" name = "option" value = "Pool"> Pool <br />
                <input type="radio" id="radio15" name = "option" value = "SE"> Service Engine <br />
                <input type="radio" id="radio17" name = "option" value = "SEGroup"> SE Group <br />
                <input type="radio" id="radio13" name = "option" value = "GSLB"> GSLB <br />
                <input type="radio" id="radio26" name = "option" value = "GSLBSite"> GSLBSite  <br />
                <input type="radio" id="radio16" name = "option" value = "PoolGroup"> PoolGroup <br />
                <input type="radio" id="radio23" name = "option" value = "WafProfile"> WAF Profile <br />
                <input type="radio" id="radio24" name = "option" value = "Tenant"> Tenant <br />
                <input type="radio" id="radio25" name = "option" value = "Meta"> Meta <br />
              </div>
              <div class="column" style="background-color:#aaa;">
                <h5>Parse Logs</h5>
                <input type="radio" id="radio9" name = "option" value = "Version"> Version <br />
                <input type="radio" id="radio10" name = "option" value = "License"> License <br />
                <input type="radio" id="radio20" name = "option" value = "Heartbeats" onclick="this.checked = false;" > Heartbeats(WIP) <br />
                <input type="radio" id="radio21" name = "option" value = "Cluster failures" onclick="this.checked = false;" > Cluster failures(WIP) <br />
                <input type="radio" id="radio22" name = "option" value = "Resources" onclick="this.checked = false;" > Resources(WIP) <br />
              </div>
            </div>
              <div align="right">
                <input type="submit" value="Submit">
              </div>
      </form>
      </p>
    </div>

<!-- END MAIN -->
</div>
</body>
</html>

""")
