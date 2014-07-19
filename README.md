cc_lemon
========
#基本ルール
* 2人のプレーヤーが同時に次の動作を行う。
* チャージ：チャージポイントが1貯まる
* ファイヤ：相手がチャージだった場合勝利する。チャージポイントが1減る
* バリア：ファイヤを防げる
* 昇竜拳：相手も昇竜拳をしない限り勝利する。チャージポイントが5減る

#プレイヤーの戦略
	・チャージポイントは0〜5がありうる
	・相手のチャージポイントの通り×自分のチャージポイントの通り＝36通り
	・36通りそれぞれにおいて、チャージ,バリア,ファイヤ,昇竜拳の比率を設定
	・ただし、チャージポイントが足りない時、ファイヤ,昇竜拳は発動しない

step1:  
◯ ◯ ◯ ◯ … ◯ ←20プレイヤー   
20プレイヤーの36の戦略(遺伝子と呼ぶ)それぞれにランダムな比率を設定する  
*正確には、[自分][相手]=[0][0]の時はチャージ率100%、[5][n]の時は昇竜拳率100%の固定値をとる  

step2:  
20プレイヤーが、固定戦略をとるサンプルプレイヤーと1000戦する  

step3:  
最も成績の良かった2プレイヤーを選ぶ  
 
step4:
2プレイヤーの持つ遺伝子をランダムに組み合わせ、20プレイヤーをつくる

step5:
さらに20プレイヤーそれぞれの2遺伝子をランダムに突然変異させる


step2-5を繰り替えす


現状
*戦略はだいたい同じようなものに収束している


困ってること
*1世代20プレイヤーってちょうどいいのか
*突然変異させる遺伝子数が2と言うのは多いのか少ないのか
*【特に聞きたい】「固定戦略を取るサンプルプレイヤー」との戦いじゃ最適評価ができている気がしない
