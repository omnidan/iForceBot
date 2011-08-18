#!/usr/bin/env python

#coding: utf8


import handler


class Goodbot(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if self.commands.getcmd(msg_words[0], 'goodbot'):
			try:
				count = int(self.commands.getvar("goodbot"))+1
			except TypeError:
				count = 1
			self.commands.setvar("goodbot", count)
			self.commands.msg("mod_goodbot_thanks", target, nick)
		elif self.commands.getcmd(msg_words[0], 'goodies') == 1:
			try:
				count = int(self.commands.getvar("goodbot"))
			except TypeError:
				count = 0
			self.commands.privmsg(target, self.commands.msg("mod_goodbot_goodies", getmsg=True)[0] % (nick, count))
