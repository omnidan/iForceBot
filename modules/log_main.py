#!/usr/bin/env python

#coding: utf8


import handler
import time

class Log_main(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':', 2)[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick

		global time
		
		output = open("./logs/%s.txt" % target, 'a')
		output.write("[%s]<%s> %s\n" % (time.strftime('%d.%m.%Y %H:%M:%S'), nick, ' '.join(msg_words)))
		output.close()

	def join(self, words):
                line = ' '.join(words)
                nick = line.split(':')[1].split('!')[0]
                target = words[2].split(':')[1]

		global time

		output = open("./logs/%s.txt" % target, 'a')
		output.write("[%s] <-- %s joined %s\n" % (time.strftime('%d.%m.%Y %H:%M:%S'), nick, target))
		output.close()

	def part(self, words):
                line = ' '.join(words)
                nick = line.split(':')[1].split('!')[0]
                target = words[2]

		global time

		output = open("./logs/%s.txt" % target, 'a')
		output.write("[%s] --> %s parted %s\n" % (time.strftime('%d.%m.%Y %H:%M:%S'), nick, target))
		output.close()
