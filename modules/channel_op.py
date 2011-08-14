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
		
		if len(msg_words) >= 1 and self.commands.getrank(nick) >= 4:
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
                                        self.commands.privmsg("ChanServ", "UNQUIET {0} {1}".format(target, msg_words[1]))
                                else:
                                        self.commands.privmsg("ChanServ", "UNQUIET {0} {1}".format(target, nick))
			temp_str = self.client.properties.get('prefix')
			temp_str += 'kick'
                        if msg_words[0] == temp_str:
                                if len(msg_words) >= 2:
                                        self.commands.kick(target, msg_words[1], msg_words[2])      
			if len(msg_words) >= 1:
				if self.commands.getcmd(msg_words[0], 'mode'):
					self.commands.mode("%s" % ' '.join(msg_words[1:]), target)
			temp_str = self.client.properties.get('prefix')
			temp_str += 'kban'
			if msg_words[0] == temp_str:
				if len(msg_words) >= 2:
					self.commands.kick(target, msg_words[1], msg_words[2])
		                        self.commands.mode("+b $x:%s" % msg_words[1], target)
			temp_str = self.client.properties.get('prefix')
			temp_str += 'unban'
                        if msg_words[0] == temp_str:
                                if len(msg_words) >= 2:
                                        self.commands.mode("-b $x:%s" % msg_words[1], target)
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'ban'
                        if msg_words[0] == temp_str:
                                if len(msg_words) >= 2:
                                        self.commands.mode("+b $x:%s" % msg_words[1], target)
		else:
			temp_str = self.client.properties.get('prefix')
			temp_str += 'kick'
			if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
				self.commands.notice(nick, "ERROR: You do not have permissions to do this command.")
			temp_str = self.client.properties.get('prefix')		
			temp_str += 'op'
			if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
				self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
			temp_str += 'deop'
			if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
				self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
			temp_str += 'voice'
			if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
				self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'devoice'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'quiet'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'unquiet'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'mode'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'kban'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
			temp_str += 'unban'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
			temp_str = self.client.properties.get('prefix')
                        temp_str += 'ban'
                        if msg_words[0] == temp_str and self.commands.getrank(nick) <= 4:
                                self.commands.notice(nick, "ERROR: You do not have the permissions to do this command.")
