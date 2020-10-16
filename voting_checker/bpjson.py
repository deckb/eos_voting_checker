import os
from .schema import BpJsonSchema
from colander import Invalid
from eospy import cleos
import socket

class BpJson:
    def __init__(self, bp_json):
        # add json to 
        for k,v in bp_json.items() :
            setattr(self, k, v)
        # validate 
        self.is_valid = True
        try:
            self._schema = BpJsonSchema()
            self._schema.deserialize(bp_json)
        except:
            self.is_valid = False
    
    def _check_version(self, url, version):
        ce = cleos.Cleos(url)
        try:
            info = ce.get_info()
            if info["server_version_string"].startswith(version):
                print(f'Correct Version: {url}')
                return True              
        except Exception as ex:
            print(f'api_check: {ex}')
        return False

    def check_apis(self, version):
        for node in self.nodes:
            if "ssl_endpoint" in node:
                if self._check_version(node["ssl_endpoint"], version) :
                    return True
            elif "api_endpoint" in node:
                if self._check_version(node["api_endpoint"], version):
                    return True
        return False

    def check_github(self):
        if "github_user" in self.org:
            return self.org["github_user"]
        return ""

    def check_peers(self):
        is_valid = False
        for node in self.nodes:
            if "p2p_endpoint" in node:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peer_info = node["p2p_endpoint"].split(":")
                peer_ip = socket.gethostbyname(peer_info[0])
                if len(peer_info) > 1:
                    peer_port = int(peer_info[1])
                else:
                    peer_port = 80
                try:
                    s.connect((peer_ip, peer_port))
                    # send some bs message
                    #s.send(b"hello")
                    data = s.recv(1024)
                    print(data)
                    s.close()
                    print(f'Available {node["p2p_endpoint"]}')
                    is_valid = True
                except Exception as ex:
                    print(f'p2p_check: {ex}')
            # else:
            #     print("no p2p endpoint listed")
            #     is_valid = False
        return is_valid