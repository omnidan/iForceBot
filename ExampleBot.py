#!/usr/bin/env python

#coding: utf8


import irc

bot = irc.Client(
	nick='ExampleBot',
	password='NickServPASSWORD',
	ident='iForceBot',
	realname='iForceBot by Daniel Bugl (Daniel0108)',
	host='irc.freenode.net',
	modules=['module_loader', 'general', 'ranks', 'ping', 'time', 'channel_main', 'channel_op', 'log_main']
)
bot.properties['autojoin'] = ['#theblackmatrix-admin']
bot.properties['prefix'] = '!'

bot.connect()
