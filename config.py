# -*- coding:utf-8 -*-  
import datetime
import redis

r = redis.Redis(host="localhost", port=6379, db=0)
botUsername = ""
botPassword = ""
workers = 20
aistart = datetime.datetime(2016,10,18,0,0,0).strftime("%Y-%m-%dT%H:%M:%SZ")
