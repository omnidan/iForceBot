#!/usr/bin/env python

#coding: utf8


import handler


class Channel_main(handler.Handler):
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
			temp_str += 'join'
			if msg_words[0] == temp_str:
				self.commands.join(msg_words[1])
				#self.commands.privmsg("ChanServ", "OP {0} {1}".format(msg_words[1], self.client.nick))
			temp_str = self.client.properties.get('prefix')
			temp_str += 'part'
			if msg_words[0] == temp_str:
				self.commands.part(msg_words[1], "Part command")
			temp_str = self.client.properties.get('prefix')
			temp_str += 'cycle'
			if msg_words[0] == temp_str:
				self.commands.part(target, "Cycling")
				self.commands.join(target)
