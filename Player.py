# -*- coding: utf-8 -*-
import random

UNKNOWN = 0
CHARGE = 1
FIRE = 2
SHORYUKEN =3
BARRIER = 4

class Player:

	def __init__(self, strategy = {}):
		self.cp = 0
		self.hand = UNKNOWN
		self.strategy = strategy

	def reset(self):
		self.cp = 0

	def print_strategy(self):
		for i in range(6): #0~5
			for j in range(6): #0~5
				print "when myself:%d opponent:%d charge:barrier:fire:shoryu= %.2f : %.2f : %.2f : %.2f" % (i, j, self.strategy[i][j]["charge"], self.strategy[i][j]["barrier"], self.strategy[i][j]["fire"], self.strategy[i][j]["shoryu"])

	def choice_hand(self, opponent_cp):
		rnd = random.random()
		charge_th = self.strategy[self.cp][opponent_cp]["charge"]
		barrier_th = self.strategy[self.cp][opponent_cp]["barrier"] + charge_th
		fire_th = self.strategy[self.cp][opponent_cp]["fire"] + barrier_th
		shoryu_th = 1
		if rnd <= charge_th:
			self.charge()
		elif rnd <= barrier_th:
			self.barrier()
		elif rnd <= fire_th:
			if self.cp >= 1:
				self.fire()
			else:
				self.choice_hand(opponent_cp)
		elif rnd <= shoryu_th:
			if self.cp >= 5:
				self.shoryu()
			else:
				self.choice_hand(opponent_cp)
		else:
			self.hand = UNKNOWN

	def show_hand(self):
		if self.hand==CHARGE:
			print "charge"
		elif self.hand==FIRE:
			print "fire"
		elif self.hand==SHORYUKEN:
			print "shoryuken"
		elif self.hand==BARRIER:
			print "barrier"
		else:
			print "unknown" 

	def charge(self):
		self.cp += 1
		self.hand = CHARGE

	def barrier(self):
		self.hand = BARRIER

	def fire(self):
		self.cp -= 1
		self.hand = FIRE

	def shoryu(self):
		self.cp -= 5
		self.hand = SHORYUKEN

	def make_random_strategy(self):
		s = {}
		for i in range(6): #0~5
			for j in range(6): #0~5
				if i in s:
					s[i][j] = self.make_random_ratio()
				else:
					s[i] = {}
					s[i][j] = self.make_random_ratio()
		s[0][0] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		for i in range(6):
			s[i][5] = {"charge":0.5, "barrier":0.5, "fire":0.0, "shoryu":0.0}
		for j in range(6):
			s[5][j] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		return s

	def make_random_ratio(self):
		partations = [random.random(), random.random(), random.random()]
		partations.sort()
		ratio_charge = partations[0]
		ratio_barrier = partations[1] - partations[0]
		ratio_fire = partations[2] - partations[1]
		ratio_shoryu = 1 - partations[2]
		ratio = {"charge":ratio_charge, "barrier":ratio_barrier, "fire":ratio_fire, "shoryu":ratio_shoryu}
		return ratio


class RandomPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.strategy = self.make_random_strategy()

	def make_random_strategy(self):
		s = {}
		for i in range(6): #0~5
			for j in range(6): #0~5
				if i in s:
					s[i][j] = self.make_random_ratio()
				else:
					s[i] = {}
					s[i][j] = self.make_random_ratio()
		s[0][0] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		for j in range(6):
			s[5][j] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		return s

	def make_random_ratio(self):
		partations = [random.random(), random.random()]
		partations.sort()
		ratio_charge = partations[0]
		ratio_barrier = 1 - partations[1]
		ratio_fire = 1 - (ratio_charge + ratio_barrier)
		ratio = {"charge":ratio_charge, "barrier":ratio_barrier, "fire":ratio_fire, "shoryu":0.0}
		return ratio


class CommonPlayer(Player):
	#over wright
	def __init__(self):
		Player.__init__(self)
		self.strategy = self.make_common_strategy()

	def make_common_strategy(self):
		s = {}
		s[0] = {}
		s[1] = {} 
		s[2] = {} 
		s[3] = {} 
		s[4] = {} 
		s[5] = {}
		s[0][0] = {"charge":1.00, "barrier":0.00, "fire":0.00, "shoryu":0.00}
		s[0][1] = {"charge":0.05, "barrier":0.14, "fire":0.28, "shoryu":0.52}
		s[0][2] = {"charge":0.03, "barrier":0.42, "fire":0.33, "shoryu":0.23}
		s[0][3] = {"charge":0.02, "barrier":0.65, "fire":0.09, "shoryu":0.24}
		s[0][4] = {"charge":0.39, "barrier":0.54, "fire":0.04, "shoryu":0.03}
		s[0][5] = {"charge":0.55, "barrier":0.33, "fire":0.12, "shoryu":0.00}
		s[1][0] = {"charge":0.02, "barrier":0.56, "fire":0.32, "shoryu":0.11}
		s[1][1] = {"charge":0.01, "barrier":0.47, "fire":0.23, "shoryu":0.29}
		s[1][2] = {"charge":0.07, "barrier":0.23, "fire":0.65, "shoryu":0.05}
		s[1][3] = {"charge":0.38, "barrier":0.21, "fire":0.10, "shoryu":0.31}
		s[1][4] = {"charge":0.02, "barrier":0.56, "fire":0.32, "shoryu":0.11}
		s[1][5] = {"charge":0.10, "barrier":0.38, "fire":0.53, "shoryu":0.00}
		s[2][0] = {"charge":0.18, "barrier":0.11, "fire":0.44, "shoryu":0.28}
		s[2][1] = {"charge":0.59, "barrier":0.03, "fire":0.13, "shoryu":0.25}
		s[2][2] = {"charge":0.11, "barrier":0.26, "fire":0.32, "shoryu":0.32}
		s[2][3] = {"charge":0.12, "barrier":0.39, "fire":0.28, "shoryu":0.20}
		s[2][4] = {"charge":0.00, "barrier":0.16, "fire":0.16, "shoryu":0.67}
		s[2][5] = {"charge":0.51, "barrier":0.31, "fire":0.18, "shoryu":0.00}
		s[3][0] = {"charge":0.22, "barrier":0.27, "fire":0.01, "shoryu":0.50}
		s[3][1] = {"charge":0.14, "barrier":0.03, "fire":0.09, "shoryu":0.73}
		s[3][2] = {"charge":0.47, "barrier":0.17, "fire":0.06, "shoryu":0.30}
		s[3][3] = {"charge":0.14, "barrier":0.20, "fire":0.50, "shoryu":0.16}
		s[3][4] = {"charge":0.28, "barrier":0.11, "fire":0.02, "shoryu":0.59}
		s[3][5] = {"charge":0.10, "barrier":0.44, "fire":0.46, "shoryu":0.00}
		s[4][0] = {"charge":0.09, "barrier":0.11, "fire":0.79, "shoryu":0.01}
		s[4][1] = {"charge":0.23, "barrier":0.26, "fire":0.32, "shoryu":0.19}
		s[4][2] = {"charge":0.43, "barrier":0.24, "fire":0.19, "shoryu":0.14}
		s[4][3] = {"charge":0.59, "barrier":0.14, "fire":0.02, "shoryu":0.26}
		s[4][4] = {"charge":0.21, "barrier":0.25, "fire":0.24, "shoryu":0.30}
		s[4][5] = {"charge":0.23, "barrier":0.53, "fire":0.25, "shoryu":0.00}
		s[5][0] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][1] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][2] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][3] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][4] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][5] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		"""
		s[0][0] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[0][1] = {"charge":0.7, "barrier":0.3, "fire":0.0, "shoryu":0.0}
		s[0][2] = {"charge":0.5, "barrier":0.5, "fire":0.0, "shoryu":0.0}
		s[0][3] = {"charge":0.5, "barrier":0.5, "fire":0.0, "shoryu":0.0}
		s[0][4] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[0][5] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[1][0] = {"charge":0.7, "barrier":0.0, "fire":0.3, "shoryu":0.0}
		s[1][1] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[1][2] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[1][3] = {"charge":0.3, "barrier":0.4, "fire":0.3, "shoryu":0.0}
		s[1][4] = {"charge":0.1, "barrier":0.2, "fire":0.7, "shoryu":0.0}
		s[1][5] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[2][0] = {"charge":0.5, "barrier":0.0, "fire":0.5, "shoryu":0.0}
		s[2][1] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[2][2] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[2][3] = {"charge":0.3, "barrier":0.4, "fire":0.3, "shoryu":0.0}
		s[2][4] = {"charge":0.1, "barrier":0.2, "fire":0.7, "shoryu":0.0}
		s[2][5] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[3][0] = {"charge":0.5, "barrier":0.0, "fire":0.5, "shoryu":0.0}
		s[3][1] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[3][2] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[3][3] = {"charge":0.3, "barrier":0.4, "fire":0.3, "shoryu":0.0}
		s[3][4] = {"charge":0.1, "barrier":0.2, "fire":0.7, "shoryu":0.0}
		s[3][5] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[4][0] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[4][1] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[4][2] = {"charge":0.3, "barrier":0.3, "fire":0.4, "shoryu":0.0}
		s[4][3] = {"charge":0.3, "barrier":0.4, "fire":0.3, "shoryu":0.0}
		s[4][4] = {"charge":0.1, "barrier":0.2, "fire":0.7, "shoryu":0.0}
		s[4][5] = {"charge":1.0, "barrier":0.0, "fire":0.0, "shoryu":0.0}
		s[5][0] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][1] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][2] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][3] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][4] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		s[5][5] = {"charge":0.0, "barrier":0.0, "fire":0.0, "shoryu":1.0}
		"""
		return s
