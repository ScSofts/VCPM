# coding: ANSI
import os
import sys
import _sitebuiltins as _sb
import requests as req
exit = _sb.Quitter("exit",0)
vcpm_path=os.getenv('vcpm_path')

DEPMAX = 10 

if sys.argv.__len__() <= 2 or (sys.argv[1] != "install" and sys.argv[1] != "remove"):
 print("Usage: vcpm install [Package Name]")
 print("       vcpm remove  [Package Name]")
 exit()

if vcpm_path == None:
  print("Error:Please run from vcpm.bat!")
  exit() 

try:
 f_cfg = open(vcpm_path + r"vcpm\cfg.txt" ,"r")
 str_cfg = f_cfg.read()
 f_cfg.close()
except:
 print("Error:No cfg.txt in "+vcpm_path + r"vcpm\cfg.txt!")
 exit()

def install_pkg_on(site_pkg,depth=0,pkg=sys.argv[2]):
 print("Installing " + pkg + " ...")
 if depth > DEPMAX:
  print("Error: So much the depth of depedence is!")
  exit()
 dep = depth+1
 try:
  pkg_name = pkg
  pkg = site_pkg[pkg_name]
 except:
  print("Package \"" + pkg + "\" not found!")
  return -1
  pass
 f = open(vcpm_path + r"vcpm\installed.txt","r")
 if pkg_name in f.read().split("\n"):
  print("Already installed " + pkg_name)
  f.close()
  return 0
  pass
 f.close()
 if pkg["dep"].__len__() > 0:
  for i in pkg['dep']:
   install_pkg_on(site_pkg,dep,i)
   pass
  pass
 for j in range(0,pkg['fetch'].__len__()):
  os.system(pkg['fetch'][j]+' ' + pkg['url'][j])
  print("Prepare to build and then press enter to build...")
  os.system("pause>nul")
  for k in pkg['build']:
   os.system(k)
   pass
  pass
 print("Installed " + pkg_name)
 f = open(vcpm_path + r"vcpm\installed.txt","a+")
 f.write(pkg_name+"\n")
 f.close()
 return 0
 pass

install = (sys.argv[1] != "remove")
if install:
 cfg = eval(str_cfg)
 sites = cfg["site"]
 for i in sites:
  print("Searching in "+ i + " ...")
  site_data = req.get(i)
  try: 
   if(site_data.ok):
     site_str = site_data.text
     site_pkg = eval(site_str)
     if install_pkg_on(site_pkg) ==0:
       exit()
       pass
     pass
   else:
     print("Error: Site \""+i+"\" is invalid£¡")
     raise
     pass
  except:
   exit(0)
  pass
else:
  try:
   f = open(vcpm_path + r"vcpm\installed.txt","r")
   str_f = f.read()
   f.close()
   str_f = str_f.replace(sys.argv[2],"")
   f = open(vcpm_path + r"vcpm\installed.txt","w")
   f.write(str_f)
   f.close()
   print("Removed "+sys.argv[2])
  except:
   print("Error:Cannot remove this package")
   exit()
   pass
  pass