#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Masukan Nama Web \n(cth : papakcoy.com or www.papkcoy.com ): ")
	print "\n\nLink Tersedia : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "#===================================#"
	Space(9); print "#      +++ Admin Finder Web +++     #"
        Space(9); print "#       Created By :Mr.Har-Har      #"
	Space(9); print "#        Evolution Cyber Team       #"
	Space(9); print "#===================================#"

Credit()
findAdmin()
