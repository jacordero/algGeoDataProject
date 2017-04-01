#!/usr/bin/env python
from rtree import index

class SimpleRTree(object):

	def __init__(self):
		self.tree = index.Index()


	def insert(self, x, y, id):
		self.tree.insert(id, (x, y, x, y))

	def delete(self, id, point):
		self.tree.delete(id, (point[0], point[1], point[0], point[1]))

	def count(self, x_left, y_bottom, x_right, y_top):
		return self.tree.count((x_left, y_bottom, x_right, y_top))