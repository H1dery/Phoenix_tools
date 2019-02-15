#coding=utf-8
## __author__ = "Fidcer" ##

import os
import re

def template_scan_results(domain_Filename,Scan_results):
    f_path = r'template.html'
    f = open (f_path, "r+")
    open('%s.html'%domain_Filename, 'w').write(re.sub(r'{{%Scan_results%}}', Scan_results, f.read()))
def template_web_dirb(domain_Filename,dirb_name):
    with open(domain_Filename+'.html', 'rt') as f:
    	data = f.read()
    	#print(data)
    	a = data.replace("{{%Web_Directory%}}",dirb_name)
    	with open(domain_Filename+'.html', 'w') as b:
    		b.write(a)
#template_web_dirb('www.baidu.com.html','/admin')