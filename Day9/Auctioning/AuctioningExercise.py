from art import logo

#  Print the logo
print(logo)

# Create the dictionary
bidderList =  {}

# Prompt for bidder's name and bid
bidder = input("What is your name?: ")
bid = input("What's your bid?: $ ")

# Add the bidder and their bid to the dictionary
bidderList[bidder] = bid

auctionStatus = input("Are there any other bidders? Type 'Yes' of 'No'. ")

# ~~~~~~~~~~Check if there are more bidders and allow them to enter their details
if auctionStatus == 'Yes':
    # Prompt for bidder's name and bid
    bidder = input("What is your name?: ")
    bid = input("What's your bid?: $ ")

    # Add the bidder and their bid to the dictionary
    bidderList[bidder] = bid
    auctionStatus = input("Are there any other bidders? Type 'Yes' of 'No'. ")
    
else:
    print("The highest bidder is: :) ")
    

# ~~~~~~~~~~~~~~~~~~~~~~~Get all the bids and find the maximum
bidsList = []

for key in bidderList:
    # Add each bid to the list
    bidsList.append(bidderList[key])

    
print(bidsList)
maxBid = max(bidsList)
print(f"The maximum is: {maxBid}")
    
# print(bidderList)
# print(f"Bidder: {bidder} && Bid: {bid}")
