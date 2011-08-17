#!/usr/bin/env python

#coding: utf8


import handler


class People_log(handler.Handler):
	def __init__(self, *args1, **args2):
		super(self.__class__, self).__init__(*args1, **args2)
		self.priority = 0

	def join(self, words):
                line = ' '.join(words)
                msg = line.split(':')[2]
                msg_words = msg.split(' ')
                nick = line.split(':')[1].split('!')[0]
                target = words[2]

                if target.find('#') != 0:
                        target = nick
		
		output = open("./people/%s.txt" % msg.upper(), 'a+')
		try:
			users = output.readlines()
		finally:
			output.close()
		if users.count("%s\n" % nick) != 1:
			output = open("./people/%s.txt" % msg.upper(), 'a')
			try:
				output.write("%s\n" % nick)
			finally:
				output.close()

        def privmsg(self, words):
                line = ' '.join(words)
                msg = line.split(':')[2]
                msg_words = msg.split(' ')
                nick = line.split(':')[1].split('!')[0]
                target = words[2]

                if target.find('#') != 0:
                        target = nick

		if self.commands.getcmd(msg_words[0], "viewpeople"):
			if len(msg_words) < 2:
				msg_words.append(target)
			output = open("./people/%s.txt" % msg_words[1].upper(), "r")
			lines = output.readlines()
			msg = "All visitors of %s (%d people): " % (msg_words[1].lower(), len(lines))
			visitors = 0
			msgs = 0
			for user in lines:
				msg += user.replace("\n", "") + ", "
				visitors += 1
				if visitors >= 25:
					if msgs < 5:
						self.commands.privmsg(target, msg)
					visitors = 0
					msg = ""
					msgs += 1
			self.commands.privmsg(target, msg)
