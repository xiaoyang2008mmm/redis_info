#!/usr/bin/python_old
# -*- coding: utf-8 -*- 

import tornado.web
import redis
from redis_info import Get_Redis_info
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
     return self.application.db
    def get_current_user(self):
     return self.get_secure_cookie("user")


class IndexHandler(BaseHandler):
    def get(self):
	redis_dict={"192.168.7.149":[6329,6339,6349,6359,6369,6319,6439,6409,6419,6429,6309]}
	data = {}
	for key in redis_dict:
	    for port in redis_dict[key]:
	    	R_INFO = Get_Redis_info(str(key),port)
	    	data["%s:%s"%(key,port)] = R_INFO.info()
        self.render('index.html', data = data) 
       

