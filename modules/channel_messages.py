#!/usr/bin/env python

#coding: utf8


import handler


class Channel_messages(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':', 2)[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if self.commands.getcmd(msg_words[0], "entrymsg") and self.commands.getrank(nick) >= 2:
			if len(msg_words) >= 3:
				output = open("./channels/%s_entrymsg.txt" % msg_words[1].lower(), "w")
				output.write(' '.join(msg_words[2:]))
				output.close()
				self.commands.privmsg(target, "%s: Set entry message of '%s' to '%s'" % (nick, msg_words[1], ' '.join(msg_words[2:])))

		if self.commands.getcmd(msg_words[0], "rentrymsg") and self.commands.getrank(nick) >= 2:
			if len(msg_words) >= 3:
				output = open("./channels/%s_rentrymsg.txt" % msg_words[1].lower(), "w")
				output.write(' '.join(msg_words[2:]))
				output.close()
				self.commands.privmsg(target, "%s: Set entry message of '%s' to '%s'" % (nick, msg_words[1], ' '.join(msg_words[2:])))
	def join(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

                if target.find('#') != 0:
                        target = nick

                output = open("./people/%s.txt" % msg.upper(), 'a+')
                try:
                        users = output.readlines()
                finally:
                        output.close()
                if users.count("%s\n" % nick) == 1:
			output = open("./channels/%s_rentrymsg.txt" % msg.lower(), "r")
                        self.commands.privmsg(msg, "%s: %s" % (nick, output.readline()))
			output.close()
                else:
                        output = open("./channels/%s_entrymsg.txt" % msg.lower(), "r")
                        self.commands.privmsg(msg, "%s: %s" % (nick, output.readline()))
                        output.close()
