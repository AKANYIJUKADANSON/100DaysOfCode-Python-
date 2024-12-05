
# a = [2, 4, 1, 90, 5, 23, 66, 38]

# print(max(a))


from art import logo

#  Print the logo
print(logo)

# Create the dictionary
bidderList =  {}
bidding_ended = False
# Prompt for bidder's name and bid
while not bidding_ended:
    bidder = input("What is your name?: ")
    bid = input("What's your bid?: $ ")
    
    # Add the bidder and their bid to the dictionary
    bidderList[bidder] = bid

    auctionStatus = input("Are there any other bidders? Type 'Yes' of 'No' ")
    if auctionStatus == "No":
        bidding_ended = True

# ~~~~~~~~~~Check if there are more bidders and allow them to enter their details
if bidding_ended == True:
    # ~~~~~~~~~~~~~~~~~~~~~~~Get all the bids and find the maximum
    bidsList = []
    currentbidderList = []

    for key in bidderList:
        # Add each bid to the list
        bidsList.append(bidderList[key])
        currentbidderList.append(key)
        
    print(bidsList)
    maxBid = max(bidsList)
    print(bidderList)
    
    winner = list(bidderList.keys())[list(bidderList.values()).index(maxBid)]
    
    print(f"The maximum is: {maxBid}")
    print(f"The winner is: {winner}")

