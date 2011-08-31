#!/usr/bin/env python

#coding: utf8


import handler


class Register(handler.Handler):
	def login_timeout(self, nick):		
		self.commands.setvar('user_%s_loggedin' % nick, True)
		import time
		time.sleep(600)
		self.commands.setvar('user_%s_loggedin' % nick, False)
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		import thread
		import md5

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0], 'register') and self.commands.getvar("user_%s_registered" % nick) == True:
                                self.commands.notice(nick, 'ERROR: You have already registered with the bot.')
                        elif self.commands.getcmd(msg_words[0], 'register'):
                                self.commands.setvar("user_%s_registered" % nick, True)
                                mm = md5.new()
                                mm.update(msg_words[1])
                                self.commands.setvar("user_%s_password" % nick, mm.hexdigest())
                                self.commands.notice(nick, "You have registered this nick with the bot.")
                                if self.commands.getrank(nick) == 0:
                                        self.commands.setrank(nick, 1)
                                elif self.commands.getrank(nick) >= 0:
                                        print "Not changing the rank of user %s" % nick
                        elif self.commands.getcmd(msg_words[0], 'login'):
				if self.commands.getvar("user_%s_loggedin") == True:
					self.commands.notice(nick, "ERROR: You are already logged in.")
				mm = md5.new()
                                mm.update(msg_words[1])
                                if mm.hexdigest() == self.commands.getvar('user_%s_password' % nick):
                                        self.commands.notice(nick, "You have been logged in.")
					thread.start_new_thread(self.login_timeout,(nick,))
                                elif mm.hexdigest() != self.commands.getvar('user_%s_password' % nick):
                                        self.commands.notice(nick, "ERROR: Incorrect password.")
