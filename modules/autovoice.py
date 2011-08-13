#!/usr/bin/env python

#coding: utf8


import handler


class Autovoice(handler.Handler):
	def join(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:

			target = nick

		lav = self.client.properties.get('autovoice')[0].split(',')
		for i in range(0, len(lav)):
			if msg_words[0] == lav[i]:
				self.commands.notice(lav[i], "INFO: {0} has joined {1}!".format(nick, lav[i]))
				self.commands.mode("+v {0}".format(nick), lav[i])
