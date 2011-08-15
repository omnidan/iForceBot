#!/usr/bin/env python

#coding: utf8


import handler


class Time(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:

			target = nick
		
		if len(msg_words) >= 1:
			temp_str = self.client.properties.get('prefix')
			temp_str += 'time'
			if msg_words[0] == temp_str:
				import time
				self.commands.privmsg(target, time.strftime(self.commands.msg("mod_time", getmsg=True)[0]))
