#!/usr/bin/env python

#coding: utf8


import handler


class Msg(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]
		msg_stuff = words[1]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1 and self.commands.getrank(nick) >= 2:
			if self.commands.getcmd(msg_words[0], 'msg'):
				self.commands.privmsg(msg_words[1], "<%s> %s" % (nick, ' '.join(msg_words[2:])))
