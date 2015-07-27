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
	redis_dict={"192.168.1.106":[6429,6439]}
	data = {}
	for key in redis_dict:
	    for port in redis_dict[key]:
	    	R_INFO = Get_Redis_info(str(key),port)
	    	data["%s:%s"%(key,port)] = R_INFO.info()
        self.render('index.html', data = data) 
       

class ChartHandler(BaseHandler):
    def get(self):
        self.render('chart.html') 
       

class Log_displayHandler(BaseHandler):
    def get(self):
        self.render('log_display.html') 
