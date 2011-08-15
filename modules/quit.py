#!/usr/bin/env python

#coding: utf8


import handler


class Quit(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:

			target = nick
		
		if len(msg_words) >= 1 and self.commands.getrank(nick) >= 6:
			if self.commands.getcmd(msg_words[0], 'quit') == 1:
				self.commands.notice(nick, "Okay... Bye :)")
				self.commands.quit(' '.join(msg_words[1:]))
				self.commands.disconnect()
			if self.commands.getcmd(msg_words[0], 'restart') == 1:
				self.commands.notice(nick, "I'm restarting :)")
				self.commands.quit(' '.join(msg_words[1:]))
				self.commands.disconnect()
				self.commands.reconnect()
