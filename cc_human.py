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
		self.player_hand = UNKNOWN
		self.p1 = CommonPlayer()
		self.p2 = Player()
		self.game_state = self.PLAYING

	def start(self):
		while self.game_state==self.PLAYING:
			p2_cp = self.p2.cp
			print "charged AI:%d YOU:%d" %(self.p1.cp, self.p2.cp)
			self.p1.choice_hand(p2_cp)
			self.player_hand = raw_input("なにをしますか？ >")
			if self.player_hand =="charge": self.p2.charge()
			elif self.player_hand=="barrier": self.p2.barrier()
			elif self.player_hand=="fire":
				if self.p2.cp>=1:
					self.p2.fire()
				else:
					self.p2.charge()
			elif self.player_hand=="shoryuken" or self.player_hand=="shoryu":
				if self.p2.cp>=5:
					self.p2.shoryu()
				else:
					self.p2.charge()
			print "AI :",
			self.p1.show_hand()
			print "YOU:",
			self.p2.show_hand()
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
		if self.player_hand=="shoryuken" or self.player_hand=="shoryu":

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
		elif self.player_hand=="charge":
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




