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
