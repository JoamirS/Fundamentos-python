from dominio import User, Bid, Auction, AuctionEvaluator

user_one = User('Joamir')
user_two = User('Gabriel')

bid_user_one = Bid(user_one, 100.0)
bid_user_two = Bid(user_two, 150.0)

auction = Auction('Celular')

auction.bids.append(bid_user_one)
auction.bids.append(bid_user_two)

for bid in auction.bids:
    print(f'O usuário {bid.user.name} deu um lance de {bid.value}')

evaluator = AuctionEvaluator()
evaluator.assess(auction)

print(f'O menor lance foi de {evaluator.lowest_bid} \ne o maior lance foi de {evaluator.highest_bid}')
