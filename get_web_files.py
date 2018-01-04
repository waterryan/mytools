#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:51:09 2018

@author: raopengyan

only for UNSW COMP9101, 
it can be modified for other course.
"""

import urllib3, re

def get_html(web_url):
    http = urllib3.PoolManager()
    r = http.request('GET', web_url)
    return r.data.decode('utf-8')
 
my_url = 'http://cgi.cse.unsw.edu.au/~cs3121/resources.php'
save_to = '/Users/raopengyan/Documents/UNSW课件/9101-2017S1/'
web_html = get_html(my_url)

filename_list = re.findall(r'href=.*\.pdf', web_html)


print('Downloading {} files...\n'.format(len(filename_list)))
i = 1
for f in filename_list:
    sub_url = f[6:]
    name = re.findall(r'\/[^\/]+$', f)[0][1:]
    print('File', i, ' >>>>>>')
    i += 1
    print(sub_url)
    print(name)
    response = http.request('GET', 'http://cgi.cse.unsw.edu.au/~cs3121/' + sub_url)
    with open(save_to + name, 'wb') as f:
        f.write(response.data)
        response.release_conn()
        print('Downloaded ', save_to + name)
    print()
    

print('-------- Finished, {} files -------'.format(len(filename_list)))
