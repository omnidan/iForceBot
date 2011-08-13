#!/usr/bin/env python

#coding: utf8


import irc

bot = irc.Client(
	nick='iForceBot',
	password='superword',
	ident='iForceBot',
	realname='iForceBot by Daniel Bugl (Daniel0108)',
	host='irc.freenode.net',
	modules=['module_loader', 'msg', 'general', 'ranks', 'ping', 'time', 'channel_main', 'log_main', 'quit']
)
bot.properties['autojoin'] = ['##iforcebot']
bot.properties['prefix'] = '?'

bot.connect()
