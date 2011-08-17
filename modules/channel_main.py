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
		
		if len(msg_words) < 1:
			msg_words.append(target)
		if self.commands.getrank(nick) >= 3:
			temp_str = self.client.properties.get('prefix')
			temp_str += 'join'
			if msg_words[0] == temp_str:
				if len(msg_words) <= 1:
					self.commands.notice(nick, "ERROR: Please specify a channel.")
				else:
					self.commands.join(msg_words[1])
			temp_str = self.client.properties.get('prefix')
			temp_str += 'part'
			if msg_words[0] == temp_str:
				if len(msg_words) <= 1:
					self.commands.notice(nick, "ERROR: Please specify a channel.")
				else:
					self.commands.part(msg_words[1], "Parting")
			temp_str = self.client.properties.get('prefix')
			temp_str += 'cycle'
			if msg_words[0] == temp_str:
				if len(msg_words) <= 1:
					self.commands.notice(nick, "ERROR: Please specify a channel.")
				else:
					self.commands.part(msg_words[1], "Cycling")
					self.commands.join(msg_words[1])
		elif len(msg_words) >= 1 and self.commands.getrank(nick) <=3:
			temp_str = self.client.properties.get('prefix')
			temp_str += 'join'
			if msg_words[0] == temp_str:
				self.commands.msg("err_permissions", nick, notice=True)
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'part'
                        if msg_words[0] == temp_str:
                                self.commands.msg("err_permissions", nick, notice=True)
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'cycle'
                        if msg_words[0] == temp_str:
                                self.commands.msg("err_permissions", nick, notice=True)
