# -*- coding: utf-8 -*-
from random import *
from Player import *

UNKNOWN = 0
CHARGE = 1
FIRE = 2
SHORYUKEN =3
BARRIER = 4


class Game:
	PLAYING = 0
	PLAYER1_WON = 1
	PLAYER2_WON = 2

	def __init__(self, p1):
		self.p1 = p1
		self.p2 = CommonPlayer()
		self.game_state = self.PLAYING
		#self.p1.print_strategy()
		#print ""
		#self.p2.print_strategy()

	def reset(self):
		self.p1.reset()
		self.p2.reset()
		self.game_state = self.PLAYING

	def experiment(self):
		NUM_OF_GAME = 1000
		w1 = 0.0
		w2 = 0.0
		for i in range(NUM_OF_GAME):
			result = self.start()
			if result==self.PLAYER1_WON:
				w1 += 1
			elif result==self.PLAYER2_WON:
				w2 += 1
			else:
				pass
		r1 = w1/NUM_OF_GAME
		r2 = w2/NUM_OF_GAME
		print "winning rate  player1: %.2f player2: %.2f" % (r1, r2)
		return r1


	def start(self):
		while self.game_state==self.PLAYING:
			p1_cp = self.p1.cp
			p2_cp = self.p2.cp
			self.p1.choice_hand(p2_cp)
			self.p2.choice_hand(p1_cp)
			#print "Player1:",
			#self.p1.show_hand()
			#print "Player2:",
			#self.p2.show_hand()
			#print ""
			self.game_state = self.judge()
		if(self.game_state == self.PLAYER1_WON): 
			#print "player1 won"
			self.reset()
			return self.PLAYER1_WON
		elif(self.game_state == self.PLAYER2_WON): 
			#print "player2 won"
			self.reset()
			return self.PLAYER2_WON
		else: 
			#print "unknown" 
			self.reset()
			return -1

	def judge(self):
		if self.p1.hand==SHORYUKEN:
			if self.p2.hand==SHORYUKEN:
				pass
			else:
				return self.PLAYER1_WON
		elif self.p1.hand==FIRE:
			if self.p2.hand==SHORYUKEN:
				return self.PLAYER2_WON
			elif self.p2.hand==FIRE:
				pass
			elif self.p2.hand==BARRIER:
				pass
			else:# player2.hand==CHARGE
				return self.PLAYER1_WON
		elif self.p1.hand==BARRIER:
			if self.p2.hand==SHORYUKEN:
				return self.PLAYER2_WON
			else:
				pass
		else: # player1.hand==CHARGE
			if self.p1.hand==SHORYUKEN:
				return self.PLAYER2_WON
			elif self.p2.hand==FIRE:
				return self.PLAYER2_WON
			elif self.p2.hand==BARRIER:
				pass
			else: # player2.hand==CHARGE
				pass
		return self.PLAYING