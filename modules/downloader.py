#!/usr/bin/env python

#coding: utf8


import handler
import urllib2

class Downloader(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0], 'instmodule'):
				if len(msg_words) == 0:
					self.commands.notice(nick, "Usage: %sinstmodule <modulename> - Installs the selected module from the iFB module repository." % self.client.properties.get('prefix'))
				elif len(msg_words) == 1:
					try:
						moduledown = urllib2.urlopen("http://www.wiseeyes.co.cc/ifb/modules/%s.py" % msg_words[1])
						output = open('%s.py' % msg_words[1], 'wb')
						output.write(moduledown.read())
						output.close				
					except IOError:
						self.commands.notice(nick, "ERROR: 404 module not found")
