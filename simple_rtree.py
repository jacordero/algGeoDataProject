#!/usr/bin/env python
from rtree import index

class SimpleRTree(object):

	def __init__(self):
		self.id = 0
		self.tree = index.Index()

	def insert(self, x, y):
		self.tree.insert(self.id, (x, y, x, y))
		#left, bottom, right, top = (x, y, x, y)

	def delete(self, point):
		self.tree.delete(self.id, (point[0], point[1], point[0], point[1]))

	def rectangle_query(self, x_left, y_bottom, x_right, y_top):
		return list(self.tree.intersection((x_left, y_bottom, x_right, y_top)))

