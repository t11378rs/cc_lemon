# -*- coding: utf-8 -*-
import random
from Player import *
from Game import *

UNKNOWN = 0
CHARGE = 1
FIRE = 2
SHORYUKEN =3
BARRIER = 4


class PvC(Game):

	def __init__(self):
		self.player_cp = 0
		self.player_hand = UNKNOWN
		self.p1 = CommonPlayer()
		self.game_state = self.PLAYING

	def start(self):
		while self.game_state==self.PLAYING:
			p2_cp = self.player_cp
			self.p1.choice_hand(p2_cp)
			self.player_hand = raw_input("なにをしますか？ >")
			print "AI :",
			self.p1.show_hand()
			print "YOU:",
			print self.player_hand
			print ""
			self.game_state = self.judge()
		if(self.game_state == self.PLAYER1_WON): 
			print "あなたの勝ちです"
			return self.PLAYER1_WON
		elif(self.game_state == self.PLAYER2_WON): 
			print "あなたの負けです"
			return self.PLAYER2_WON
		else: 
			print "unknown" 
			return -1

	def judge(self):
		if self.player_hand=="shoryuken":
			if self.p1.hand==SHORYUKEN:
				pass
			else:
				return self.PLAYER1_WON
		elif self.player_hand=="fire":
			if self.p1.hand==SHORYUKEN:
				return self.PLAYER2_WON
			elif self.p1.hand==FIRE:
				pass
			elif self.p1.hand==BARRIER:
				pass
			else:# player2.hand==CHARGE
				return self.PLAYER1_WON
		elif self.player_hand=="barrier":
			if self.p1.hand==SHORYUKEN:
				return self.PLAYER2_WON
			else:
				pass
		elif self.player_hand=="shoryuken":
			if self.p1.hand==SHORYUKEN:
				return self.PLAYER2_WON
			elif self.p1.hand==FIRE:
				return self.PLAYER2_WON
			elif self.p1.hand==BARRIER:
				pass
			else: # player2.hand==CHARGE
				pass
		else:
			pass
		return self.PLAYING

if __name__ == '__main__':
	game = PvC()
	game.start()




