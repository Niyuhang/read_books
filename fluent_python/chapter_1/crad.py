#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:chapter_1.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple

# 利用namedtuple 实现牌 具有 rank 和 suit
Card = namedtuple('card', ['rank', 'suit'])


class Deck(object):
    """
    the first sample for fluent python
    Card game
    why you these guys like using cards for sample in book
    >-<
    """
    ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        # 新的小知识 实现了 __getitem__ 也可以让一个对象变成可迭代的对象
        # 调用next 会从item 为0 的下标开始调用，直到index error
        return self._cards[item]

    def get_sorted_deck(self):
        self._cards = sorted(self._cards, key=self._calculate_card_value)

    # def _calculate_card_value(self, card):
    #     return self.ranks.index(card.rank) * len(self.suit_values) + \
    #            int(self.suit_values[card.suit])
#
#
if __name__ == '__main__':
    if __name__ == '__main__':
        deck = Deck()
    deck = Deck()
    deck.get_sorted_deck()
    deck.get_sorted_deck()

