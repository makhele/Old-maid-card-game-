import copy

import time

start_time=time.time()
class cards:
    suitList = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rankList = ['nill', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rankList[self.rank] + ' of ' + str(self.suitList[self.suit]))


# print(cards(2,11)) everything works so far

class deck(cards):
    def __init__(self):
        self.cards = []
        for i in range(len(self.suitList)):
            for m in range(1, len(self.rankList)):
                self.cards.append(str(cards(i, m)))

    # def __str__(self):
    #     final = ''
    #     for i in range(len(self.cards)):
    #         final = final + '' + ' ' * i + str(self.cards[i]) + '\n'
    #
    #     return final


class hand():
    def __init__(self, name=''):
        self.name = name
        self.cards = []

    def __str__(self):
        return str(self.cards)

    def addhand(self, card):
        self.cards.append(card)
        return self.name, self.cards


class shuffledDeck(deck, hand):
    def __init__(self):
        super().__init__()
        self.tempshuffledcards = copy.deepcopy(self.cards)
        self.cardsleftonDeck = copy.deepcopy(self.shuffleCards())

    def shuffleCards(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)

            self.tempshuffledcards[i], self.tempshuffledcards[j] = self.tempshuffledcards[j], self.tempshuffledcards[i]
        self.shuffledcards = self.tempshuffledcards
        # print(self.shuffledcards)  #-->for debugging
        return self.shuffledcards

    def removeCard(self, cardname):

        return self.cardsleftonDeck.remove(cardname)

    def deal(self, numberofcards=len(deck().cards), hands=[]):
        numberofhands = len(hands)
        lst = []
        if numberofcards > len(self.cards):
            return 'you have exceded the Deck Size Try Again'

        if numberofcards * numberofhands > len(deck().cards):
            for a in range(numberofcards):
                try:
                    cardr = self.cardsleftonDeck.pop()
                except IndexError:
                    break
                handname = hands[a % numberofhands]
                lst.append(hand(handname).addhand(cardr))

        else:
            for b in range(numberofcards * numberofhands):
                try:
                    cardr = self.cardsleftonDeck.pop()
                except IndexError:
                    break
                handname = hands[b % numberofhands]
                lst.append(hand(handname).addhand(cardr))

        dictionaryofCardsandHands = {}
        for c in hands:
            dictionaryofCardsandHands[c] = []
            for d in lst:
                for e in d:
                    if c == e:
                        for f in d:
                            if isinstance(f, list):
                                for j in f:
                                    dictionaryofCardsandHands[c].append(j)
                    else:
                        break

        return dictionaryofCardsandHands


# print(shuffledDeck().deal(hands=['sabata', 'makhele', 'subzero', 'abel', 'boitumelo']))

class OldMaidHand(shuffledDeck, cards):
    def __init__(self, x):
        super().__init__()
        self.nhands = x
        self.remove = self.removeCard((str(cards(0, 12))))
        self.dicofdeltcards = self.deal(hands=x)
        self.matches = 0

    def removeMathces(self):

        for i in self.dicofdeltcards.keys():
            for h in range(13):
                # n = str(cards(0, 1 + h))  |
                # m = str(cards(3, 1 + h))  |
                # o = str(cards(1, 1 + h))
                # p = str(cards(2, 1 + h))
                if str(cards(0, 1 + h)) in self.dicofdeltcards[i]:
                    if str(cards(3, 1 + h)) in self.dicofdeltcards[i]:
                        print(i, 'matched', str(cards(0, 1 + h)), 'with', str(cards(3, 1 + h)))
                        self.dicofdeltcards[i].remove(str(cards(0, 1 + h)))
                        self.dicofdeltcards[i].remove(str(cards(3, 1 + h)))
                        self.matches = self.matches + 1

                if str(cards(1, 1 + h)) in self.dicofdeltcards[i]:
                    if str(cards(2, 1 + h)) in self.dicofdeltcards[i]:
                        print(i, 'matched', str(cards(1, 1 + h)), 'with', str(cards(2, 1 + h)))
                        self.dicofdeltcards[i].remove(str(cards(1, 1 + h)))
                        self.dicofdeltcards[i].remove(str(cards(2, 1 + h)))
                        self.matches = self.matches + 1

        # print(self.matches)
        # for i in self.dicofdeltcards.keys():
        #     count = 1
        #     print(len(self.dicofdeltcards[i]))
        #     print('The Hand of', i, 'is:\n')
        #     for c in self.dicofdeltcards[i]:
        #         print(' ' * count + c + '')
        #         count = count + 1

        return self.matches

    def play(self):  # input('please give a list of players e.g["name1","name2]"')):
        # self.removeCard((str(cards(0, 12))))
        # print(self.cardsleftonDeck)
        # dicofdeltcards = self.deal(hands=x)
        for i in self.dicofdeltcards.keys():
            count = 1
            # print(len(self.dicofdeltcards[i]))
            print('The Hand of', i, 'is:' + '\n',end='')
            for c in self.dicofdeltcards[i]:
                print(c,'\n', end='')
                count = count + 1
            print(''* 2, end='')

            # for i in dicofdeltcards.keys():
            #     for h in range(13):
            #         # n = str(cards(0, 1 + h))  |
            #         # m = str(cards(3, 1 + h))  |
            #         # o = str(cards(1, 1 + h))
            #         # p = str(cards(2, 1 + h))
            #         if str(cards(0, 1 + h)) in dicofdeltcards[i]:
            #             if str(cards(3, 1 + h)) in dicofdeltcards[i]:
            #                 print(i,'matched',str(cards(0, 1 + h)), 'with',str(cards(3, 1 + h)))
            #                 dicofdeltcards[i].remove(str(cards(0, 1 + h)))
            #                 dicofdeltcards[i].remove(str(cards(3, 1 + h)))
            #                 matches=matches+1
            #
            #         if str(cards(1, 1 + h)) in dicofdeltcards[i]:
            #             if str(cards(2, 1 + h)) in dicofdeltcards[i]:
            #                 print(i, 'matched', str(cards(1, 1 + h)), 'with', str(cards(2, 1 + h)))
            #                 dicofdeltcards[i].remove(str(cards(1, 1 + h)))
            #                 dicofdeltcards[i].remove(str(cards(2, 1 + h)))
            #                 matches=matches+1
            # --------------------------trail and Error--------------------------------------------------

            # elif g==str(cards(0,1+h)):
            #     dicofdeltcards[i].remove(str(cards(0,1+h)))
            #     dicofdeltcards[i].remove(str(cards(3,1+h)))
            #     #dicofdeltcards[i][f]=str(cards(3,1+h))
            # elif g==str(cards(1,1+h)):
            #     k=str(cards(1,1+h))
            #     l=str(cards(2,1+h))
            #
            #     dicofdeltcards[i].remove(str(cards(1,1+h)))
            #     dicofdeltcards[i].remove(str(cards(2,1+h)))
            #     #dicofdeltcards[i][f]=str(cards(2,1+h))
            # --------------------------trail and Error--------------------------------------------------
        # print(matches)
        # for i in dic_of_dealt_cards.keys():
        #     count = 1
        #     print(len(dic_of_dealt_cards[i]))
        #     print('The Hand of', i, 'is:\n')
        #     for c in dic_of_dealt_cards[i]:
        #         print(' ' * count + c + '')
        #         count = count + 1

        count = 0
        while self.matches < 25:
            # print(self.matches)
            # print(self.dicofdeltcards)
            try:
                for o in self.dicofdeltcards.keys():

                    if len(self.dicofdeltcards[o]) == 0:
                        del self.dicofdeltcards[o]
                        self.nhands.remove(o)

            except  RuntimeError:
                continue
            self.removeMathces()
            for keys in self.dicofdeltcards.keys():
                # print(keys,self.dic_of_dealt_cards[keys])
                self.shuffleHand(self.dicofdeltcards[keys])
                # print(keys,self.dic_of_dealt_cards[keys])
            Handturn = self.nhands[count % len(self.nhands)]

            try:
                self.pickCard(Handturn)
            except IndexError:
                for left in self.dicofdeltcards.keys():
                    if len(self.dicofdeltcards[left]) == 1:
                        return print(left, 'has','"{}"'.format(self.dicofdeltcards[left][0]),'and has lost the Game')
            count = count + 1

    def shuffleHand(self, cards):
        import random
        nCards = len(cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)

            cards[i], cards[j] = cards[j], cards[i]
        # self.shuffled_cards = self.temp_shuffled_cards
        # print(self.shuffled_cards)  #-->for debugging
        return cards

    def pickCard(self, name):
        templist = copy.deepcopy(self.nhands)
        templist.remove(name)
        import random
        choosenhand = random.choice(templist)
        takenCard = self.dicofdeltcards[choosenhand].pop()

        self.dicofdeltcards[name].append(takenCard)


x = OldMaidHand(x=['Sabata Makhele', 'Puseletso Makhele', 'Boitumelo Sehlabaka', 'Daniel Makhele', 'Hlophekile Ngundle',
                   'Tseko Malawaneng'])
x.play()

print(time.time()-start_time,'seconds')
print(x.cardsleftonDeck)
