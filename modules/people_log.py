#!/usr/bin/env python

#coding: utf8


import handler


class People_log(handler.Handler):
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
			self.commands.privmsg(msg, "I remember you, %s!" % nick)
		else:
			output = open("./people/%s.txt" % msg.upper(), 'a')
			try:
				output.write("%s\n" % nick)
			finally:
				output.close()
			self.commands.privmsg(msg, "Welcome, %s!" % nick)
