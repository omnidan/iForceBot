#!/usr/bin/env python

#coding: utf8


import handler


class People(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if msg_words[0][0:1] == self.client.properties.get('prefix_people'):
				command = msg_words[0].replace(self.client.properties.get('prefix_people'),'',1)
				command = command.lower()
				if command == 'me':
					self.commands.privmsg(target, "You are {0} :)".format(nick))
				else:
					try:
						output = open("./people/{0}.txt".format(command), "r")
						try:
							rline = output.readline()
							if rline != '':
								self.commands.privmsg(target, "{0}".format(rline))
						finally:
							print "Reading: {0}".format("./people/{0}.txt".format(command))
							output.close()
					except IOError:
						pass
