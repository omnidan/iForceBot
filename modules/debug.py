#!/usr/bin/env python

#coding: utf8


import handler

class Debug(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getrank(nick) >= 7:
				if self.commands.getcmd(msg_words[0], 'setvar'):
					if self.commands.getrank(nick) >= 7:
						try:
							if len(msg_words) >= 4:
								channel = msg_words[3]
							else:
								channel = None
							self.commands.setvar(msg_words[1], msg_words[2], channel)
							self.commands.msg("success", target, nick)
						except IndexError:
							self.commands.msg("error", target, nick)
					else:
						self.commands.msg("err_permissions", target, nick)
				elif self.commands.getcmd(msg_words[0], 'getvar'):
					if self.commands.getrank(nick) >= 7:
						try:
							if len(msg_words) >= 3:
								channel = msg_words[2]
							else:
								channel = None
							self.commands.privmsg(target,
								self.commands.msg("mod_debug_getvar", getmsg=True)[0]
								% (nick, self.commands.getvar(msg_words[1], channel))
							)
						except IndexError:
							self.commands.msg("error", target, nick)
					else:
						self.commands.msg("err_permissions", target, nick)
				elif self.commands.getcmd(msg_words[0], 'exec'):
					if self.commands.getrank(nick) >= 7:
						self.commands.privmsg(target, "%s: Executing '%s'. Output: %s" % (nick, ' '.join(msg_words[1:]), eval(' '.join(msg_words[1:]))))
					else:
						self.commands.msg("err_permissions", target, nick)
