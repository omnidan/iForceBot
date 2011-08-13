#!/usr/bin/env python

#coding: utf8


import handler


class People_remove(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:

			target = nick
		
		if self.commands.getcmd(msg_words[0], 'remove') == 1 and self.commands.getrank(nick) >= 3:
			f_name = msg_words[1].lower()
			output = open("./people/{0}.txt".format(f_name), 'w')
			output.write('')
			output.close()
			print 'Removing {0}.txt'.format(f_name)
			self.commands.privmsg(target, "Removed entry for {0} D:".format(f_name))
