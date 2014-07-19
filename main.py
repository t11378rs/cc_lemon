# -*- coding: utf-8 -*-
import random
from Player import *
from Game import *

UNKNOWN = 0
CHARGE = 1
FIRE = 2
SHORYUKEN =3
BARRIER = 4

NUM_OF_RELATIVES = 20
NUM_OF_GENERATION = 100

def make_new_strategy_by_two(mvp, svp):
	s = {}
	for i in range(6): #0~5
		for j in range(6): #0~5
			rnd = random.randint(0,1)
			if rnd==0:
				p = mvp
			else:
				p = svp
			if i in s:
				s[i][j] = p[i][j]
			else:
				s[i] = {}
				s[i][j] = p[i][j]
	return s

def make_random_ratio():
	partations = [random.random(), random.random(), random.random()]
	partations.sort()
	ratio_charge = partations[0]
	ratio_barrier = partations[1] - partations[0]
	ratio_fire = partations[2] - partations[1]
	ratio_shoryu = 1 - partations[2]
	ratio = {"charge":ratio_charge, "barrier":ratio_barrier, "fire":ratio_fire, "shoryu":ratio_shoryu}
	return ratio

def mutate(stra, num_of_gene = 2):
	s = stra
	for i in range(num_of_gene):
		rnd_myself = 0
		rnd_opponent = 0
		while(rnd_myself==0 and rnd_opponent==0):
			rnd_myself = random.randint(0,4)
			rnd_opponent = random.randint(0,4)
		s[rnd_myself][rnd_opponent] = make_random_ratio()
	return s

def make_new_gen(mvp, svp):
	ps = []
	for i in range(NUM_OF_RELATIVES):
		stra = make_new_strategy_by_two(mvp, svp)
		stra = mutate(stra)
		ps.append(Player(stra))
	return ps



if __name__ == '__main__':
	#最初のプレーヤー10人を作ってぶちこむ
	players = []
	for i in range(NUM_OF_RELATIVES):
		players.append(RandomPlayer())

	for generation in range(NUM_OF_GENERATION):	
		print "start %dth generation" % (generation+1)

		#1,2番目に良かったやつを記録
		mvp = 0
		svp = 0
		mvp_p = 0.0
		svp_p = 0.0
		for i,player in enumerate(players):
			game = Game(player)
			p = game.experiment()
			if mvp_p < p :
				svp = mvp
				svp_p = mvp_p
				mvp_p = p
				mvp = i
			else:
				pass

		print mvp_p
		print players[mvp].print_strategy()
		print svp_p
		print players[svp].print_strategy()
		print ""

		players = make_new_gen(players[mvp].strategy, players[svp].strategy)

