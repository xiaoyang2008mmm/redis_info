#!/usr/bin/python_old
import redis
class Get_Redis_info:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
    def info(self):
        r = redis.Redis(host=self.addr,port=self.port)
        CPU             =r.info(section="CPU")
        Stats           =r.info(section="Stats")
        Server          =r.info(section="Server")
        Memory          =r.info(section="Memory")
        Clients         =r.info(section="Clients")
        Keyspace        =r.info(section="Keyspace")
        Persistence     =r.info(section="Persistence")
        Replication     =r.info(section="Replication")
        Redis_Data = {  "CPU":CPU,
                        "Stats":Stats,
                        "Server":Server,
                        "Memory":Memory,
                        "Clients":Clients,
                        "Keyspace":Keyspace,
                        "Persistence":Persistence,
                        "Replication":Replication
                }

        return Redis_Data
