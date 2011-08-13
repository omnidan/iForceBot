#!/usr/bin/env python

#coding: utf8


import handler


class General(handler.Handler):
	def __init__(self, *args1, **args2):
		super(self.__class__, self).__init__(*args1, **args2)
		self.priority = 100
		
	def _376(self, words):
		self.__autojoin()
		
	def _442(self, words):
		self.__autojoin()
		
	def __autojoin(self):
		self.commands.privmsg("NickServ", "identify {0}".format(self.client.password))
		self.commands.join(self.client.properties.get('autojoin'))
		joinlist = self.client.properties.get('autojoin')[0].split(",")
		for i in range(0, len(joinlist)):
			self.commands.privmsg("ChanServ", "OP {0} {1}".format(joinlist[i], self.client.nick))
