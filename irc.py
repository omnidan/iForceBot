#!/usr/bin/env python

#coding: utf8


import socket
import os
import re
import pymongo

class Client(object):
	def __init__(self, nick=None, password=None, ident=None, realname=None, host=None, port=6667, modules=[]):
		self.nick = nick
		self.ident = ident
		self.realname = realname
		self.host = host
		self.port = port
		self.password = password
		
		self.irc = None
		self.connected = False
		self.running = False
		self.commands = Commands(client=self)

		self.connection = pymongo.Connection()
		self.db = self.connection['iForceBot']
		
		self.modules = []
		for module in modules:
			self.load_module(module)
			
		self.properties = {}
		
	def connect(self):
		if self.irc is not None:
			raise IRCError('Cannot create socket: Already created')
		if self.nick is None:
			raise IRCError('Cannot connect: Nick is not set')
		if self.password is None:
			raise IRCError('Cannot connect: Password is not set')
		if self.ident is None:
			raise IRCError('Cannot connect: Ident is not set')
		if self.realname is None:
			raise IRCError('Cannot connect: Realname is not set')
		if self.host is None:
			raise IRCError('Cannot connect: Host is not set')
		
		self.irc = socket.socket()
		self.irc.connect((self.host, self.port))
		self.connected = True
		self.running = True
		self.commands.nick(self.nick)
		self.send("USER %s 0 0 :%s" % (self.ident, self.realname))
		self.listen()
		self.connected = False
		
	def disconnect(self):
		self.running = False
		self.irc.close()
		self.irc = None
		
	def reconnect(self):
		self.disconnect()
		self.connect()
		
	def load_module(self, module):
		if module.find('/') != -1 or module.find('\'') != -1:
			raise IRCError('Cannot load module \'%s\': Contains non-permitted chars' % module)
		self.unload_module(module)
		if os.path.isfile('./modules/%s.py' % module):
			exec open('./modules/%s.py' % module)
			try:
				self.modules.append(locals()[module.capitalize()](client=self))
			except NameError:
				raise IRCError('Cannot load module \'%s\': Class does not exist' % module)
		else:
			raise IRCError('Cannot load module \'%s\': File does not exist' % module)
		self.modules = sorted(self.modules, key=lambda module: module.priority, reverse=True)
		
	def unload_module(self, module):
		for i in range(len(self.modules)):
			if self.modules[i].__class__.__name__ == module.capitalize():
				del self.modules[i]
				break
		
	def send(self, text):
		self.irc.send(text + "\n")
		print text
		
	def handle(self, words):
		cmd = words[1].lower()
		if words[0].lower() in ('ping', 'pong'):
			cmd = words[0].lower()
		elif re.compile('[0-9]').match(cmd) is not None:
			cmd = '_' + cmd
		for module in self.modules:
			try:
				if hasattr(module, cmd):
					if getattr(module, cmd)(words) is True:
						break
				elif hasattr(module, 'all'):
					if getattr(module, 'all')(words) is True:
						break
			except Exception as e:
				print 'Error in module: ' + str(e)
		
	def listen(self):
		buffer = ""
		while self.running:
			buffer += self.irc.recv(4096)
			buffer = buffer.replace("\r", "")
			
			while buffer.find("\n") != -1:
				line, buffer = buffer.split("\n", 1)

				line = line.rstrip()
				
				if(line == ""):
					continue
				print line

				words = line.split(' ')
				
				if words[0] == "PING":
					self.send("PONG %s" % words[1])
					
				if words[1] == "433":
					print "Nickname '%s' is in use. Trying to use '%s_'" (self.nick, self.nick)
					self.nick += '_'
					self.commands.nick(self.nick)
				elif words[1] == "NICK":
					if words[0].find(':%s!' % self.nick) == 0:
						self.nick = words[2][1:]
						print 'Nick: ' + self.nick
						
				self.handle(words)

class Commands(object):
	def __init__(self, client):
		self.client = client

	def sendraw(self, message):
		# Do not use it unless you know what you are doing!
		self.client.send(message)

	def loadmodule(self, module):
		self.client.load_module(module)

	def unloadmodule(self, module):
		self.client.unload_module(module)
		
	def privmsg(self, target, text):
		self.client.send("PRIVMSG %s :%s" % (target, text))
		
	def notice(self, target, text):
		self.client.send("NOTICE %s :%s" % (target, text))
	
	def nick(self, new_nick):
		self.client.send("NICK %s" % new_nick)

	def join(self, channel=None):
		if channel is None:
			return
		elif isinstance(channel, str):
			channel = (channel,)
		
		self.client.send("JOIN " + ",".join(channel))

	def mode(self, flags, target=None):
		if target is None:
			target = self.client.nick
		self.client.send("MODE %s %s" % (target, flags))

	def names(self, channel):
		self.client.send("NAMES " + channel)

	def part(self, channel, message=""):
		self.client.send("PART %s :%s" % (channel, message))

	def quit(self, message=""):
		self.client.send("QUIT :" + message)

	def invite(self, channel, nick):
		self.client.send("INVITE %s %s" % (nick, channel))

	def disconnect(self):
		self.client.disconnect()
	
	def reconnect(self):
		self.client.connect()

	def kick(self, channel, target, message):
		self.client.send("KICK %s %s :%s" % (channel, target, message))
	
	def kban(self, channel, target, message):
		self.client.send("MODE %s +b $a:%s" % (channel, target))
		self.client.send("KICK %s %s :%s" % (channel, target, message)) 

        def remove(self, channel, target, message):
                self.client.send("REMOVE {0} {1} :{2}".format(channel, target, message))

	def getcmd(self, message, cmd):
		message = message.lower()
		cmd = cmd.lower()
		if len(message) >= 1:
			if len(cmd) >= 1:
				temp_str = '%s%s' % (self.client.properties.get('prefix'), cmd)
				if message == temp_str:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def db_open(self, collection):
		return self.db[collection]

	def db_post(self, collection, dict):
		collection.insert(dict)

	def db_update(self, collection, spec, dict, upsert=True):
		collection.update(spec, dict, upsert)

	def db_findone(self, collection, dict):
		return collection.find_one(dict)

	def db_find(self, collection, dict):
		return collection.find(dict)

	def getrank(self, nick, channel="global"):
		# Started coding channel-based ranks, unfinished!
		nick = nick.lower()
		channel = channel.upper()
		if os.path.exists("./users/%s.txt" % nick) and os.path.isfile("./users/{0}.txt".format(nick)):
			userfile = open("./users/%s.txt" % nick, 'r')
			rawrank = userfile.readline()
			rawranks = userfile.readlines()
			userfile.close()
			if channel == "GLOBAL":
				try:
					rank = int(rawrank)
				except ValueError:
					rank = 0			
			else:
				for i in range(0, count(rawranks)-1, 1):
					try:
						if rawranks.split('::')[0].upper() == channel:
							rank = rawranks.split('::')[1].lower()
							break;
					except ValueError:
						rank = 0
			return rank
		else:
			return 0

	def setrank(self, nick, rank):
		nick = nick.lower()
		try:
			wrank = int(rank)
		except ValueError:
			wrank = 0
		
		userfile = open("./users/%s.txt", nick, 'w')
		userfile.write('%s' % wrank)
		userfile.close()

        def msg(self, title, target=False, nick=False, notice=False, getmsg=False):
		if getmsg == False and target == False:
			return False
		if title.isalnum():
			output = open("./messages/%s.msg" % title.lower(), 'r+')
			try:
				msgs = output.readlines()
			finally:
				output.close()
		else:
			return False

                for line in msgs:
			if nick != False:
				msg = "%s: " % nick
			else:
				msg = ""
			msg += line
			if notice == True:
				self.notice(target, msg)
			else:
                        	self.privmsg(target, msg)

class IRCError(Exception):
	def __init__(self, text):
		self.text = text
	
	def __str__(self):
		return 'IRCError: %s' % self.text

