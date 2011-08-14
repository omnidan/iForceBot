
###!/usr/bin/env python

#coding: utf8


import handler

class Example(handler.Handler): # Change to your module's name
        def privmsg(self, words):
                line = ' '.join(words)
                msg = line.split(':')[2]
                msg_words = msg.split(' ')
                nick = line.split(':')[1].split('!')[0]
                target = words[2]

                if target.find('#') != 0:
                        target = nick
                if len(msg_words) >= 1:
                        if self.commands.getcmd(msg_words[0], 'example') and self.commands.getrank(nick) >= 1: ### Requires a rank of at least 1.
                                self.commands.privmsg(target, "This is an example script!") ### Sends a message to the channel.
			elif self.commands.getcmd(msg_words[0], 'example') and self.commands.getrank(nick) <= 1: # Error handling.
        			self.commands.notice(nick, "ERROR: You do not have the permissions for this command.")  

                        if self.commands.getcmd(msg_words[0], 'example_notice') and self.commands.getrank(nick) >= 1: ### Requires a rank of at least 1.
                                self.commands.notice(target, "This is an example notice!") ### Sends a notice to the channel.
                        elif self.commands.getcmd(msg_words[0], 'example_notice') and self.commands.getrank(nick) <= 1: # Error handling.
                                self.commands.notice(nick, "ERROR: You do not have the permissions for this command.")

			if self.commands.getcmd(msg_words[0], 'example_unotice') and self.commands.getrank(nick) >= 1: ### Requires a rank of at least 1.
                                self.commands.notice(msg_words[1], "This is an example user notice!") ### Sends a notice to the user.
                        elif self.commands.getcmd(msg_words[0], 'example_unotice') and self.commands.getrank(nick) <= 1: # Error handling.
                                self.commands.notice(nick, "ERROR: You do not have the permissions for this command.")
