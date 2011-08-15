
###!/usr/bin/env python

#coding: utf8


import handler

class Commands_basic(handler.Handler):
        def privmsg(self, words):
                line = ' '.join(words)
                msg = line.split(':')[2]
                msg_words = msg.split(' ')
                nick = line.split(':')[1].split('!')[0]
                target = words[2]

                if target.find('#') != 0:
                        target = nick
                if len(msg_words) >= 1:
                        if self.commands.getcmd(msg_words[0], 'invite') and self.commands.getrank(nick) >= 4:
                                self.commands.invite(target, "%s" % msg_words[1])
			elif self.commands.getcmd(msg_words[0], 'invite') and self.commands.getrank(nick) <= 4:
        			self.commands.msg("err_permissions", nick, notice=True)   			
	
                if len(msg_words) >= 1:
                        if self.commands.getcmd(msg_words[0], 'nick') and self.commands.getrank(nick) >= 5:
                                self.commands.nick("%s" % msg_words[1])
			elif self.commands.getcmd(msg_words[0], 'nick') and self.commands.getrank(nick) <= 5:
				self.commands.msg("err_permissions", nick, notice=True)

                if len(msg_words) >= 1:
                        if self.commands.getcmd(msg_words[0], 'msg') and self.commands.getrank(nick) >= 2:
				if len(msg_words) >= 3:
					self.commands.privmsg(msg_words[1], "<%s> %s" % (nick, ' '.join(msg_words[2:])))
				elif len(msg_words) <= 1:
					self.commands.notice(nick, "ERROR: Channel and message not specified.")
				elif len(msg_words) == 2:
					self.commands.notice(nick, "ERROR: Channel or message not specified")
			elif self.commands.getcmd(msg_words[0], 'msg') and self.commands.getrank(nick) <= 2:
				self.commands.msg("err_permissions", nick, notice=True)

		if len(msg_words) >= 1:
                        if self.commands.getcmd(msg_words[0], 'modules') and self.commands.getrank(nick) >= 2:
                                self.commands.privmsg(target, "Modules loaded: %s" % self.client.modules)
                        elif self.commands.getcmd(msg_words[0], 'modules') and self.commands.getrank(nick) <= 2:
                                self.commands.msg("err_permissions", nick, notice=True)
