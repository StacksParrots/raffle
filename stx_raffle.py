import random

MAX_WINNERS = 3

# Use https://arraythis.com/, to array string dump to list

"""
41 voters

brick.btc
Arno from earth 🌍
Burrito_Jon
eparrot
Dash
hirox
j2p2
glitched-david.btc
Vova.btc
Cruyff
Squawker-Kaylee.btc
Pablo Yanoski
Repo ambiguously wearing shorts
Jaaykool | Brian JPEG Specialist
Win Win
Choi1386
NickySpecs.btc
All-In
Markiv
pryzm
BowTiedPT
F31ix.btc
Tokenmixer.btc
grumpy_coot
TheLight
Morguf
openroad
Venus Sun
GoodKitty
Tangaroa
TheOverflow
incorrigiblewinnie
AaronInAlaska🦜
BowTiedLawyer
TimI
bond99
TracSpurs.btc
longstreet.btc
AnonYMouse
DatGreenSpot
fitzroyjenkins
"""

voters = ["brick.btc", "Arno from earth 🌍", "Burrito_Jon", "eparrot", "Dash", "hirox", "j2p2", "glitched-david.btc", "Vova.btc", "Cruyff", "Squawker-Kaylee.btc", "Pablo Yanoski", "Repo ambiguously wearing shorts", "Jaaykool | Brian JPEG Specialist", "Win Win", "Choi1386", "NickySpecs.btc", "All-In", "Markiv", "pryzm", "BowTiedPT", "F31ix.btc", "Tokenmixer.btc", "grumpy_coot", "TheLight", "Morguf", "openroad", "Venus Sun", "GoodKitty", "Tangaroa", "TheOverflow", "incorrigiblewinnie", "AaronInAlaska🦜", "BowTiedLawyer", "TimI", "bond99", "TracSpurs.btc", "longstreet.btc", "AnonYMouse", "DatGreenSpot", "fitzroyjenkins"]

secure_random = random.SystemRandom()

print(f"\nTotal voters: {len(voters)} \n")

for n in range(MAX_WINNERS):

    WINNER = secure_random.choice(voters)

    print(f"STX Winner: {WINNER}\n")

    # Remove winner from list
    voters.remove(WINNER)

    # Shuffle the list
    random.shuffle(voters)
