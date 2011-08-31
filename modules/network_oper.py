#!/usr/bin/env python

#coding: utf8


import handler


class Network_oper(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0], 'oper') and self.commands.getrank(nick) >= 5:
				self.commands.oper(msg_words[1], msg_words[2])
			elif self.commands.getcmd(msg_words[0], 'kline') and self.commands.getrank(nick) >= 5:
				self.commands.kline(msg_words[1], msg_words[2], "%s" %  ' '.join(msg_words[3:]))
			elif self.commands.getcmd(msg_words[0], 'kill') and self.commands.getrank(nick) >= 5:
				self.commands.kill(msg_words[1], "%s" % ' '.join(msg_words[2:]))
