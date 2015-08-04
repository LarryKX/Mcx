#!coding=utf-8
import os
import json

CONF_LOCATIONS = ["/etc/mcx", "/home/tefx/.mcx", "~/Mcx/conf"]
CONF_FILE = "config.json"
HOSTS_DIRS = "hosts.d"

class Configuration(object):
    def __init__(self):
        for item in CONF_LOCATIONS:
            conf_path = os.path.expanduser(os.path.join(item, CONF_FILE))
            if os.path.exists(conf_path):
                with open(conf_path) as f:
                    for k,v in json.load(f).iteritems():
                        self.__setattr__(k, v)
        self.hosts = {}
        self.get_hosts()

    def get_hosts(self):
        for item in CONF_LOCATIONS:
            d = os.path.expanduser(os.path.join(item, HOSTS_DIRS))
            if os.path.exists(d):
                self.hosts.update(read_hosts_from_dir(d))


# CONN has the form:
# {"name" : "beijing/server1",
#  "conn_type" : "ssh",
#  "auth_type" : "password",
#  "username"  : "tefx"
#  "password"  : "123456"}
def read_hosts_from_dir(dir):
    conns = {}
    for (base, dirs, files) in os.walk(dir):
        for path in files:
            with open(os.path.join(base, path)) as f:
                conns.update(json.load(f))
    return conns

configuration = Configuration()
