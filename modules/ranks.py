#!/usr/bin/env python

#coding: utf8


import handler
import string
import random

class Ranks(handler.Handler):
	def addowner(self, nick):
		if self.commands.getvar("owner_verified") != True:
			try:
				self.code
			except:
				self.code = None
			if self.code is None:
        	       		global string, random
        	        	chars = string.letters + string.digits
        	        	code = ""
        	        	for i in range(10):
        	        	        code = code + random.choice(chars)
        	        	self.code = code

			print "Your owner code is: '%s'. Please PM your bot: 'addowner %s <YOURNAME>'. Replace <YOURNAME> with your nick on IRC." % (self.code, self.code)
			self.commands.privmsg(nick, "By the way, you need to verify that you are the real owner of the bot, please look at the bots console for a verification code.")

	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target == self.client.nick and self.commands.getvar("owner_verified") != True:
			if len(msg_words) >= 3:
				if msg_words[0] == "addowner":
					if msg_words[1] == self.code:
						print "Told: %s, Code: %s" % (msg_words[1], self.code)
						self.commands.setrank(msg_words[2], 7)
						self.commands.setvar("owner_verified", True)
						self.commands.privmsg(nick, "Successfully added '%s' as bot-owner." % msg_words[2])
					else:
						self.commands.privmsg(nick, "Wrong code.")
					self.addowner(nick)
				else:
					self.commands.privmsg(nick, "Sorry, I do not have this command in my database. You may want to try 'addowner <CODE> <USERNAME>'.")
			elif len(msg_words) >= 1 and msg_words[0] == "addowner":
				self.commands.privmsg(nick, "Not enough arguments, try: 'addowner <CODE> <USERNAME>'.")
				self.addowner(nick)
		elif self.commands.getvar("owner_verified") == True and msg_words[0] == "addowner":
			self.commands.privmsg(nick, "You already verified the owner of this bot")

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0],'getrank'):
				if len(msg_words) >= 1:
					self.commands.privmsg(target, "%s: %s has the rank %s" % (nick, msg_words[1], self.commands.getrank(msg_words[1])))
			elif self.commands.getcmd(msg_words[0],'setrank'):
				if self.commands.getrank(nick) >= int(msg_words[2]):
					try:
						self.commands.setrank(msg_words[1], int(msg_words[2]))
					except ValueError:
						self.commands.privmsg(target, "Error, rank must be an integer")
					finally:
						self.commands.privmsg(target, "Rank of %s successfully set to %d." % (msg_words[1], int(msg_words[2])))
				else:
					self.commands.msg("err_permissions", target, nick)
