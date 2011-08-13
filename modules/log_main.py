#!/usr/bin/env python

#coding: utf8


import handler


class Log_main(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':', 2)[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		import time
		
		output = open("./logs/{0}.txt".format(target), 'a')
		output.write("[{0}]<{1}> {2}\n".format(time.strftime('%d.%m.%Y %H:%M:%S'), nick, ' '.join(msg_words)))
		output.close()
