valuesToNames = {'Two':2,'Three':3,'Four':4,'Five':5,'Siv':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
def royalFlush(player):
    if not straightFlush(player):
        return False
    if player.flushCards[0].name == 'A' and \
            player.flushCards[1].name == 'K' and\
            player.flushCards[2].name == 'Q' and\
            player.flushCards[3].name == 'J' and\
            player.flushCards[4].name == 'T':
        player.handDetails = []
        for x in range(0,5):
            player.handDetails.append(player.flushCards[x])
        return True
    return False
def straightFlush(player):
    if not flush(player):
        return False
    for x in player.flushCards:
        player.flushnames.append(x.name)
    if 'A' in player.flushnames and '2' in player.flushnames and '3' in player.flushnames and '4' in player.flushnames and '5' in player.flushnames and '6' not in player.flushnames:
        return True
    for x in range(0,(len(player.flushCards)-4)):
        if player.flushCards[x].value - player.flushCards[x+4].value == 4:
            return True
    return False
def quads(player):
    for i in player.values:
        quadcount = player.values.count(i)
        if quadcount == 4:
            player.quadvalue = i
            return True
    return False
def boat(player):
    player.boatvalues = []
    for i in player.values:
        tripcount = player.values.count(i)
        if tripcount == 3:
            valuesWithoutTrips = player.values.copy()
            valuesWithoutTrips.remove(i)
            valuesWithoutTrips.remove(i)
            valuesWithoutTrips.remove(i)
            player.boatvalues.append(i)
            player.boatvalues.append(i)
            player.boatvalues.append(i)
            for j in valuesWithoutTrips:
                paircount = player.values.count(j)
                if paircount == 2:
                    player.boatvalues.append(j)
                    player.boatvalues.append(j)
                    return True
    return False
def flush(player):
    for suit in ['s','d','h','c']:
        if player.suits.count(suit) >= 5:
            player.flushCards = []
            for x in range(0,len(player.hand)):
                if player.hand[x].suit == suit:
                    player.flushCards.append(player.hand[x])
            player.flushCards.sort(key=lambda x: x.value, reverse=True)
            return True
    return False
def straight(player):
    if flush(player) == True:
        return False
    cardSet = set()
    for x in player.values:
        cardSet.add(x)
    player.straightCards=sorted(cardSet, reverse=True)
    if player.straightCards.count(14) >= 1 and player.straightCards.count(2) >= 1 and player.straightCards.count(3) >= 1 and player.straightCards.count(4) >= 1 and player.straightCards.count(5) >= 1 and player.straightCards.count(6) == 0:
        player.straightvalue = 5
        return True
    for x in range(0,len(player.straightCards)-4):
        if player.straightCards[x] - player.straightCards[x + 4] == 4:
            player.straightvalue = player.straightCards[x]
            return True
    return False
def trips(player):
    if straight(player) == True:
        return False
    for i in player.values:
        tripcount = player.values.count(i)
        if tripcount == 3:
            player.tripsvalue = i
            return True
    return False
def twopair(player):
    if flush(player) == True or quads(player) == True or boat(player) == True or trips(player) == True or straight(player) == True:
        return False
    for i in player.values:
        firstpaircount = player.values.count(i)
        if firstpaircount == 2:
            player.twopairvalues = []
            valuesWithoutFirstPair = player.values.copy()
            valuesWithoutFirstPair.remove(i)
            valuesWithoutFirstPair.remove(i)
            player.twopairvalues.append(i)
            player.twopairvalues.append(i)
            for y in valuesWithoutFirstPair:
                secondpaircount = valuesWithoutFirstPair.count(y)
                if secondpaircount == 2:
                    player.twopairvalues.append(y)
                    player.twopairvalues.append(y)
                    player.twopairvalues.sort(reverse=True)
                    return True
    return False
def pair(player):
    if twopair(player) == True:
        return False
    for i in player.values:
        paircount = player.values.count(i)
        if paircount == 2:
            player.pairvalue = i
            return True
    return False
def highcard(player):
    if pair(player) == True or twopair(player) == True:
        return False
    player.hand.sort(key=lambda x: x.value, reverse=True)
    hc = player.hand[0].name
    for x in range(0,5):
       player.handDetails.append(player.values[x])
    return hc
def wynik(player):
    if royalFlush(player) == True:
        return 10
    elif straightFlush(player) == True:
        return 9
    elif quads(player) == True:
        return 8
    elif boat(player) == True:
        return 7
    elif flush(player) == True:
        return 6
    elif straight(player) == True:
        return 5
    elif trips(player) == True:
        return 4
    elif twopair(player) == True:
        return 3
    elif pair(player) == True:
        return 2
    else:
        return 1
def handToName(player): #######nie chce mi sie kombinowac z przeksztalcaniem np 13s full of 14s na kings full of aces bo w tym jezyku chujowo slowniki sa zrobione
    if royalFlush(player) == True:
        return "a Royal flush! WOW!"
    elif straightFlush(player) == True:
        return "a Straight flush!"
    elif quads(player) == True:
        return "Quads!"
    elif boat(player) == True:
        return "Full house - {}s full of {}s!".format(player.boatvalues[0],player.boatvalues[3])
    elif flush(player) == True:
        return "Flush - {} high!".format(player.flushCards[0].value)
    elif straight(player) == True:
        return "Straight - {} high!".format(player.straightvalue)
    elif trips(player) == True:
        return "Three of a kind - {}s!".format(player.tripsvalue)
    elif twopair(player) == True:
        return "Two pair!"
    elif pair(player) == True:
        return "One pair!"
    else:
        return "A highcard of", highcard(player)
def handDetails(player):
    player.handDetails = []
    if straightFlush(player) == True:
        player.handDetails = []
        if 'A' in player.flushnames and '2' in player.flushnames and '3' in player.flushnames and '4' in player.flushnames and '5' in player.flushnames:
            player.handDetails.append(5)
        else:
            for x in range(0, 5):
                player.handDetails.append(player.flushCards[x].value)
    elif quads(player) == True:
        player.handDetails = []
        for x in range(0,4):
            player.handDetails.append(player.quadvalue)
        if player.values[0] == player.quadvalue:
            player.handDetails.append(player.values[4])
        else:
            player.handDetails.append(player.values[0])
    elif boat(player) == True:
        player.handDetails = []
        player.handDetails = player.boatvalues.copy()
    elif flush(player) == True:
        player.handDetails = []
        for x in player.flushCards:
            player.handDetails.append(x.value)
    elif straight(player) == True:
        player.handDetails = []
        player.handDetails = player.straightvalue
    elif trips(player) == True:
        player.handDetails = []
        player.handDetails.append(player.tripsvalue)
        player.handDetails.append(player.tripsvalue)
        player.handDetails.append(player.tripsvalue)
        tempValues = player.values.copy()
        tempValues.remove(player.tripsvalue)
        tempValues.remove(player.tripsvalue)
        tempValues.remove(player.tripsvalue)
        player.handDetails.append(tempValues[0])
        player.handDetails.append(tempValues[1])
    elif twopair(player) == True:
        player.handDetails = []
        player.twopairvalues.sort(reverse=True)
        player.handDetails.append(player.twopairvalues[0])
        player.handDetails.append(player.twopairvalues[1])
        player.handDetails.append(player.twopairvalues[2])
        player.handDetails.append(player.twopairvalues[3])
        if player.values[0] in player.twopairvalues:
            if player.values[2] in player.twopairvalues:
                player.handDetails.append(player.values[4])
            else:
                player.handDetails.append(player.values[2])
        else:
            player.handDetails.append(player.values[0])
    elif pair(player) == True:
        player.handDetails = []
        player.twopairvalues = []
        valueswithoutpair = player.values.copy()
        valueswithoutpair.remove(player.pairvalue)
        valueswithoutpair.remove(player.pairvalue)
        player.handDetails.append(player.pairvalue)
        player.handDetails.append(player.pairvalue)
        player.handDetails.append(valueswithoutpair[0])
        player.handDetails.append(valueswithoutpair[1])
        player.handDetails.append(valueswithoutpair[2])
    elif highcard(player) == True:
        print("highcard")
        print("player values:",player.values)
        for x in range(0,5):
            player.handDetails.append(player.values[x])
    return 0
      #  WYPIERDOLIC Z FUNKCJI SPRAWDZANIA UKLADU WRZUCANIE CZEGOKOLWIEK DO HANDDETAILS KURWA