#!/usr/bin/env python

#coding: utf8


import handler


class Goodbot(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if self.commands.getcmd(msg_words[0], 'goodbot') == 1:
			innput = open("./goodbot/{0}.txt".format(self.client.nick), 'r')
			raw = innput.readline()
			innput.close()
			try:
				count = int(raw)
			except ValueError:
				count = 0
			count += 1
			output = open("./goodbot/{0}.txt".format(self.client.nick), 'w')
			output.write('{0}'.format(count))
			output.close()
			print 'Increasing value of {0}.txt to {1}'.format(self.client.nick, count)
			self.commands.privmsg(target, "Wooof! Thanks! Woof, Woof! :D")
		elif self.commands.getcmd(msg_words[0], 'goodies') == 1:
			innput = open("./goodbot/{0}.txt".format(self.client.nick), 'r')
			raw = innput.readline()
			innput.close()
			try:
				count = int(raw)
			except ValueError:
				count = 0
			self.commands.privmsg(target, "I have {0} goodies :) Woof!".format(count))
