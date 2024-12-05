from art import logo

#  Print the logo
print(logo)

# Create the dictionary
bidderList =  {}
bidding_ended = False

# ~~~~~~~~~~~~~~~~~Get the winner ~~~~~~~~~~~~~~~~~~~~
def getTheWinner(bidderRecord):
    maximumBid = 0
    winner = ""
    
    for bidder in bidderRecord:
        bid = bidderRecord[bidder]
        if bid > maximumBid:
            maximumBid = bid
            winner = bidder
    
    print(f"The winner is {winner} with ${maximumBid}")
    
    
# Prompt for bidder's name and bid
while not bidding_ended:
    bidder = input("What is your name?: ")
    # ~~~~~ Changing the input to integer
    bid = int(input("What's your bid?: $ "))
    
    # Add the bidder and their bid to the dictionary
    bidderList[bidder] = bid

    auctionStatus = input("Are there any other bidders? Type 'Yes' of 'No' ")
    if auctionStatus == "No":
        bidding_ended = True
        getTheWinner(bidderList)
    # elif auctionStatus == "Yes":
    #     clear()

    

