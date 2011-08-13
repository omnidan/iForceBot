#!/usr/bin/env python

#coding: utf8


import handler


class Ping(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0], 'ping') == 1:
				self.commands.privmsg(target, "%s: pong" % nick)
			elif self.commands.getcmd(msg_words[0], 'rping') == 1:
				rank = int(msg_words[1])
				if self.commands.getrank(nick) >= rank:
					self.commands.privmsg(target, "%s: Rank-pong level %d" % (nick, rank))
				else:
					self.commands.msg("err_permissions", target, nick)
			elif self.commands.getcmd(msg_words[0], 'version') == 1:
				self.commands.msg("version", target, nick)
