
###!/usr/bin/env python

#coding: utf8


import handler


class Invite(handler.Handler):
        def privmsg(self, words):
                line = ' '.join(words)
                msg = line.split(':')[2]
                msg_words = msg.split(' ')
                nick = line.split(':')[1].split('!')[0]
                target = words[2]

                if target.find('#') != 0:
			target = nick
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0], 'invite'):
				self.commands.invite(target, "%s" % msg_words[1])
