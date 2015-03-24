#!/usr/bin/env python
#encoding:utf8
#author: linuxhub.org
#统计nginx日志IP数统计

import re,sys

data_file = '/data/log/nginx.log'


#读文件数据  

def ip_count(data_file):
              with open(data_file, 'r') as f:
                            #print f.readlines() #每次读一行
                            count = {}
                            for line in f.readlines():
                                          content = line.strip() # 把末尾的'\n'删掉
                                          log = content.split('- -')
                                          ip = log[0]
                                          count[ip] = count.get(ip,0)+1  #加1

                            return count




ip_count = ip_count(data_file)

print 'IPAddress\t\tcount'
for ip,count in ip_count.iteritems():
              print '%s\t%s'%(ip,count)



