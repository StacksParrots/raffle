import pandas as pd
import numpy as np

# NFTs to raffle
NFTS_COUNT = 10

# TSV file of the tickets
# i.e
#   user,entries
#   Cirro,1
USERS = pd.read_csv('users.tsv', sep='\t')

# Duplicate users based on tickets
# i.e Cirro,2 =>
#     Cirro
#     Cirro
tickets = []
for index, row in USERS.iterrows():

    # Insert mutiple name to tickets based on the number of entries
    for entry in range(int(row['entries'])):
        tickets.append(row['user'])

# Reconstruct the list of duplicated names to a table
tickets = pd.DataFrame(tickets, columns=['name'])

# And shuffle the rows randomly
tickets = tickets.sample(frac=1)

print(f"\n\nInitial no. of entries now: {len(tickets)} \n\n")

# Run the Raffle
for i in range(NFTS_COUNT):

    # Select one row randomly using sample()
    winner = tickets.sample(n=1)
    print(f"NFT #{i} Winner: {winner.name.to_string(index=False)} ")

    # Remove the winning row from table
    tickets = tickets.drop(winner.index)

    print(f"     INFO: Winning row => {winner.index} removed. No. of entries now: {len(tickets)}\n\n")

    # Yes! shuffle the rows randomly again
    tickets = tickets.sample(frac=1)
