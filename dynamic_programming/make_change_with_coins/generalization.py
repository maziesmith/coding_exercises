#!/usr/bin/env python

# modified from: http://bryceboe.com/2009/11/04/dynamic-programming-%E2%80%93-coin-change-problem-in-python/

def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""
    # can also do with dictionary/actual hash table rather than list

    # table = [None for x in range(value + 1)] # initialize cache list
    table = [None] * (value + 1)
    table[0] = [] # set first element of list to an empty list; takes 0 coins to make zero

    for i in range(1, value + 1):
        
        for coin in coins:
            # print '' 
            # print 'i is', i
            # print 'coin is', coin
            # print 'table is', table
            # print table[i-coin]
            if coin > i: # coin > target value i; skip it 
                continue # cannot completely break out of loop, since input coins list is unsorted

            # if coin value not in table or if we can make a shorter list for existing table[i]
            can_improve_existing = (table[i - coin] != None and table[i] != None) and len(table[i - coin]) + 1 < len(table[i])
            if not table[i] or can_improve_existing: 

                if table[i - coin] != None: # empty list is valid, so we need to specify != None here
                    table[i] = table[i - coin][:] # create copy of list rather than point to same one
                    table[i].append(coin) # append new coin to list
                    # even if we're doing table[3], we're appending 3 to an empty list, since table[i-coin] = table[0] = []

    # print table
    if table[value] != None:
        print '%d coins to sum to target value %d: %s' % (len(table[value]), value, table[value])
    else:
        print 'No solution possible for coin list %r and target value %r.' % (coins, value)


coins = [1, 3, 4]
value = 11
solve_coin_change(coins, value)

coins = [2, 4]
value = 3
solve_coin_change(coins, value)