from data import JSONDataloader

loader = JSONDataloader()

pirates = loader.load_pirates()
ducats = 1430
sum_of_ranks = sum(pirate.rank for pirate in pirates)

for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} ducats")

























# pirates = [
#     ("Harry", "Captain", 5),
#     ("Isabel","Quartermaster", 9),
#     ("BootStrap Bill", "Mate", 7),
#     ("Powder Joe", "Gunner", 6),
#     ("Four Finger Fritz", "Mate", 7)
# ]
#
# ducats = 850
# sum_of_ranks = sum(rank for name, title, rank in pirates)
#
# for name, title, rank in pirates:
#     share = rank / sum_of_ranks * ducats
#     print(f"{title} {name} gets {share:.2f} ducats")
