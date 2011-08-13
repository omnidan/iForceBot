#!/usr/bin/env python

#coding: utf8


import handler


class Channel_op(handler.Handler):
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
			temp_str += 'op'
			if msg_words[0] == temp_str:
				if len(msg_words) >= 2:
					self.commands.privmsg("ChanServ", "OP {0} {1}".format(target, msg_words[1]))
				else:
					self.commands.privmsg("ChanServ", "OP {0} {1}".format(target, nick))
			temp_str = self.client.properties.get('prefix')
			temp_str += 'deop'
			if msg_words[0] == temp_str:
				if len(msg_words) >= 2:
					self.commands.privmsg("ChanServ", "DEOP {0} {1}".format(target, msg_words[1]))
				else:
					self.commands.privmsg("ChanServ", "DEOP {0} {1}".format(target, nick))

			temp_str = self.client.properties.get('prefix')
			temp_str += 'voice'
			if msg_words[0] == temp_str:
				if len(msg_words) >= 2:
					self.commands.privmsg("ChanServ", "VOICE {0} {1}".format(target, msg_words[1]))
				else:
					self.commands.privmsg("ChanServ", "VOICE {0} {1}".format(target, nick))
			temp_str = self.client.properties.get('prefix')
			temp_str += 'devoice'
			if msg_words[0] == temp_str:
				if len(msg_words) >= 2:
					self.commands.privmsg("ChanServ", "DEVOICE {0} {1}".format(target, msg_words[1]))
				else:
					self.commands.privmsg("ChanServ", "DEVOICE {0} {1}".format(target, nick))
                        temp_str = self.client.properties.get('prefix')
                        temp_str += 'quiet'
                        if msg_words[0] == temp_str:
                                if len(msg_words) >= 2:
                                        self.commands.privmsg("ChanServ", "QUIET {0} {1}".format(target, msg_words[1]))
                                else:
                                        self.commands.privmsg("ChanServ", "QUIET {0} {1}".format(target, nick))
                        temp_str = self.client.properties.get('prefix')
                        temp_str += 'unquiet'
                        if msg_words[0] == temp_str:
                                if len(msg_words) >= 2:
                                        self.commands.privmsg("ChanServ", "UNVOICE {0} {1}".format(target, msg_words[1]))
                                else:
                                        self.commands.privmsg("ChanServ", "UNVOICE {0} {1}".format(target, nick))

