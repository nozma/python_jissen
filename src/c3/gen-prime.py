# -*- coding:utf-8 -*-

def genPrime(maxnum):
    num = 2
    while (num <= maxnum):
        is_prime = True # デフォルトで素数フラグon
        # 2以上num未満の整数で割る
        for i in range(2, num): # num = 2のときは実行されない
            if (num % i) == 0:  # 割り切れたら素数ではない
                is_prime = False
                break
        if is_prime: yield num # 素数のときだけyield文を実行
        num += 1

it = genPrime(10)

for i in it:
    print(i)
