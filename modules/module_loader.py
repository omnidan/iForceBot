#!/usr/bin/env python

#coding: utf8


import handler


class Module_loader(handler.Handler):

	def __init__(self, *args1, **args2):
		super(self.__class__, self).__init__(*args1, **args2)
		self.priority = 100 

		
	def privmsg(self, words):
		line = ' '.join(words)

		msg = line.split(':')[2]


		msg_words = msg.split(' ')

		nick = line.split(':')[1].split('!')[0] 

		
		if (len(msg_words) >= 2) and (self.commands.getrank(nick) >= 6):
			temp_str = self.client.properties.get('prefix')
			temp_str += 'load'
			if msg_words[0] == temp_str: 
				if msg_words[1] != 'module_loader':
					
					self.client.load_module(msg_words[1])
					self.commands.notice(nick, 'Module {0} loaded.'.format(msg_words[1]))
					return True 
			temp_str = self.client.properties.get('prefix')
			temp_str += 'unload'
			if msg_words[0] == temp_str:

				if msg_words[1] != 'module_loader':

					self.client.unload_module(msg_words[1])
					self.commands.notice(nick, 'Module {0} unloaded.'.format(msg_words[1]))
					return True
				elif msg_words[1] == 'module_loader':
					self.commands.notice(nick, 'ERROR: Cannot unload module module_loader'.format(msg_words[1])) 

			temp_str = self.client.properties.get('prefix')
			temp_str += 'reload'
			if msg_words[0] == temp_str:

				if msg_words[1] != 'module_loader':

					self.client.unload_module(msg_words[1])
					self.client.load_module(msg_words[1])
					self.commands.notice(nick, 'Module {0} reloaded.'.format(msg_words[1]))
				elif msg_words[1] == 'module_loader':
					self.commands.notice(nick, 'ERROR: Cannot reload module module_loader'.format(msg_words[1]))
