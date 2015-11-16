from __future__ import absolute_import, print_function, unicode_literals

#import pymongo
from pymongo import Connection
connection = Connection("localhost")
 
db = connection.product1
 
import re
from streamparse.bolt import Bolt

class ParseMessage (Bolt):
    def initialize(self, conf, ctx):
        connection = Connection("localhost")
	self.db = connection.product1
    def process(self, tup):
	measure = tup.values[0] # extract the messages
	# Split the message into fields
	fields = measure.split(',')
	# Emit all the fields
	self.db.product1.save({"measure":fields});
	for field in fields:
        	self.emit([field])
	        self.log('%s' % field) 
