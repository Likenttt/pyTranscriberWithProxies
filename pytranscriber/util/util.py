'''
   (C) 2019 Raryel C. Souza
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import platform
import os
import subprocess
import socket
from pathlib import Path
import traceback
import json
import requests
proxy_settings_dict = {"http":{"ip":"127.0.0.1","protocol":"socks5","port":"10808"},"https":{"ip":"127.0.0.1","protocol":"socks5","port":"10808"}}

class MyUtil(object):
    @staticmethod
    def cleanProxySettings():
        proxySettingsFilePath = Path.home() / 'pyTranscriber_proxy_settings.json'
        if os.path.exists(proxySettingsFilePath):
            os.remove(proxySettingsFilePath)


    @staticmethod
    def loadProxySettings():
        proxySettingsFilePath = Path.home() / 'pyTranscriber_proxy_settings.json'
        httpConfig = {}
        httpsConfig = {}
        proxy_settings_dict = {}
        if os.path.exists(proxySettingsFilePath):
            with open(proxySettingsFilePath,'r') as jf:
                try:
                    proxy_settings_dict = json.load(jf)
                    httpConfig = proxy_settings_dict["http"]
                    httpsConfig = proxy_settings_dict["https"]
                    return httpConfig,httpsConfig
                except Exception:
                    traceback.print_exc()
                    return "",""
        else:
            return httpConfig,httpsConfig
    
    @staticmethod
    def persistenceProxySettings(httpPort,httpsPort):
        proxySettingsFilePath = Path.home() / 'pyTranscriber_proxy_settings.json'
        if os.path.exists(proxySettingsFilePath):
            with open(proxySettingsFilePath, 'w') as jf:
                try:
                    httpConfig = proxy_settings_dict["http"]
                    httpConfig["port"] = httpPort
                    httpsConfig = proxy_settings_dict["https"]
                    httpsConfig["port"] = httpsPort
                    json.dump(proxy_settings_dict,jf)
                    return "Success!"
                except Exception as e:
                    traceback.print_exc()
                    return "Failed!"+str(e)
        else:
            with open(proxySettingsFilePath,'w') as jf:
                proxy_settings_dict["http"]["port"] = httpPort
                proxy_settings_dict["https"]["port"]  = httpsPort
                json.dump(proxy_settings_dict,jf)
                return "Success!"        

    @staticmethod
    def loadProxies():
        proxies = {}
        httpConfig,httpsConfig = MyUtil.loadProxySettings()
        if len(httpConfig) == 0 and len(httpsConfig) == 0:
            return proxies
        if len(httpConfig) != 0:
            proxies["http"] = httpConfig["protocol"]+ "://"+httpConfig["ip"]+":"+httpConfig["port"]            
        if len(httpsConfig) != 0:
            proxies["https"] = httpConfig["protocol"]+ "://"+httpConfig["ip"]+":"+httpConfig["port"]
        return proxies
 
    @staticmethod
    def open_file(path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    @staticmethod
    def is_internet_connected():
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            proxies = MyUtil.loadProxies()
            if len(proxies) == 0:
            #     headers = {"Content-Type": "text/html; charset=UTF-8"}
            #     resp = requests.get("http://www.google.com", headers=headers,proxies=proxies)
            # else:
                s = socket.create_connection(("www.google.com", 80), 2)
                s.close()
            return True
        except OSError:
            traceback.print_exc()
            pass
        return False

    @staticmethod
    def percentage(currentval, maxval):
        return 100 * currentval / float(maxval)

                