#!/usr/bin/python

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator, GLib as glib

gi.require_version("Notify", "0.7")
from gi.repository import Notify

import subprocess
import signal
import os
import time
import threading

def main():
  #child = subprocess.Popen(["bash", "/home/dungnt/ShellScript/test3.sh"])
  #streamdata = child.communicate()[0]
  #print('pid '+str(child.pid))
  #print('pid '+str(child.returncode))
  #with open("/home/dungnt/hello.txt", "r") as file:
  #          first_line = file.readline()
  #          for last_line in file:
  #              pass
  #print("lastline of hello.txt:"+last_line)
  #if last_line=='go to sleep\n':
   #  print ('ok')
  #child = subprocess.Popen(["pgrep", "/home/dungnt/ShellScript/test3.sh","-f"])
  #print('pid '+str(child.pid))
  #print('pid '+str(child.output))
  process = subprocess.Popen(["echo", "hello"], stdout=subprocess.PIPE)
  #process.communicate()[0]
  #print(process.communicate()[0])
  x=process.stdout.readlines()
  print(x)
if __name__ == "__main__":
  main()


