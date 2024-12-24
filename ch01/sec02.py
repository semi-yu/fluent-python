"""
    Making a french deck with dunder methods
"""
import collections

"""
    속성만 있는 클래스를 만들때는 이런 방식을 사용할 수 있다.
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks 
                                        for suit in self.suits]
        
    def __len__(self):
        """
        앞 뒤로 언더스코어가 붙은 메서드를 던더 메서드라고 한다.
        dunder; double underscore before and after

        인터프리터가 호출한다.
        """
        return len(self._cards)
    
    def __getitem__(self, pos):
        """
        - 접근을 []에 위임하므로 슬라이싱을 쓸 수 있다.
        - random.choice 쓸 수 있다.
        - 반복 접근(iterative access) 가능하다.
        - reverse() 가능하다.
        """
        return self._cards[pos]
    
deck = FrenchDeck()

"""
    __len__
"""
print(len(deck))

"""
    __getitem__
"""
from random import choice
print('first', deck[0])
print('random', choice(deck))
print('slicing', deck[:3])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high)[:5]:
    print(card)