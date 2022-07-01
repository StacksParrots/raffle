import random
import secrets

# Use https://arraythis.com/, to array string dump to list
OGS = ["0xLOC#8554", "3ternal.btc#5370", "AaronInAlaska#0001", "All-In#6135", "AmusedPresence#3737", "BowTiedPT#0268", "Brick#0690", "Burrito_Jon#9491", "Chang🦍#6705", "Choi1386#2767", "Cirro#0001", "Cruyff#7565", "DatGreenSpot#2106", "Destiny#0002", "EoMGames#3259", "Jaaykool | Brian JPEG Specialist#3882", "Kaylee.btc#7266", "Mohsen63#1008", "Murphy Lee#9780", "NICOLE🌸#0445", "NateB#3947", "NickySpecs.btc#0509", "Pablo Yanoski#9315", "Sean C#8064", "SteveM#5233", "Tangaroa#5313", "TheLight#5522", "TheOverflow#5159", "TimI#2797", "TracSpurs.btc#0279", "Venus Sun#7485", "Vova.btc#0453", "Win Win#3730", "Zoomed123#2133", "berry#6676", "bolt.btc#1244", "bond99#5269", "eliherf#0058", "incorrigiblewinnie#4887", "johnennis#6100", "nft_huntsman#2639", "nicksainato#2222", "ninebit#1519", "pekebuh-nft.btc#4433", "rbandy.btc#9247", "reubs.eth#9741"]

secure_random = random.SystemRandom()

print(f"Winner: {secure_random.choice(OGS)}")
