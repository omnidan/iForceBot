#!/usr/bin/env python

#coding: utf8


import handler


class Ranks(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0],'getrank'):
				self.commands.privmsg(target, "%s: %s" % (msg_words[1], self.commands.getrank(msg_words[1])))
			elif self.commands.getcmd(msg_words[0],'setrank'):
				self.commands.setrank(msg_words[1], int(msg_words[2]))
				self.commands.privmsg(target, "Rank of %s successfully set to %d." % (msg_words[1], int(msg_words[2])))
