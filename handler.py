#!/usr/bin/env python

#coding: utf8


class Handler(object):
	def __init__(self, client):
		self.client = client
		
		self.commands = client.commands
		self.priority = 1
