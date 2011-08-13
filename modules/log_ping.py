#!/usr/bin/env python

#coding: utf8


import handler


class Log_ping(handler.Handler):
	pnick = 'daniel0108'
	def search(self, string, find, cs=0):
	        if cs == 0:
	                string = string.lower()
	                find = find.lower()
	        result = string.find(find)
	        return result

	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':', 2)[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:

			target = nick

		if self.search(' '.join(msg_words), self.pnick) != -1:				
			import time
			
			output = open("./logs/{0}.txt".format(self.pnick), 'a')
			output.write("{0}->[{1}]<{2}> {3}\n".format(target, time.strftime('%d.%m.%Y %H:%M:%S'), nick, ' '.join(msg_words)))
			output.close()
