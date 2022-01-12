import sys


class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Bid:
    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:
    def __init__(self, description):
        self.description = description
        self.__bids = list()
        self.highest_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max


    def propose(self, bid: Bid):
        if bid.value > bid.highest_bid:
            bid.highest_bid = bid.value
        if bid.value < bid.lowest_bid:
            bid.lowest_bid = bid.value

        self.__bids.append(bid)

    @property
    def bids(self):
        return self.__bids

