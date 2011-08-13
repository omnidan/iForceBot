#!/usr/bin/env python

#coding: utf8


import handler


class People_add(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:

			target = nick
		
		if self.commands.getcmd(msg_words[0], 'add') == 1:
			adding = 0
			if len(msg_words) >= 3:
				if len(msg_words) == 3:
					if len(msg_words[2]) >= 5:
						adding = 1
					else:
						adding = 0
						self.commands.privmsg(target, "You have to enter more than 5 characters to add an entry...")
				elif len(msg_words[3]) >= 1:
					adding = 1
				else:
					adding = 0
					self.commands.privmsg(target, "You have to enter more than 5 characters to add an entry...")
			else:
				adding = 0
				self.commands.privmsg(target, "You have to enter more than 5 characters to add an entry...")
			if adding == 1:
				f_name = msg_words[1]
				f_text = msg_words[2:]
				if f_name == 'me':
					f_name = nick
				f_name = f_name.lower()
				output = open("./people/{0}.txt".format(f_name), 'w')
				output.write(' '.join(f_text))
				output.close()
				print 'Creating {0}.txt: {1}'.format(f_name, ' '.join(f_text))
				self.commands.privmsg(target, "Added entry for {0} :D".format(f_name))
