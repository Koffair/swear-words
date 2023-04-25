import icu

collator = icu.Collator.createInstance(icu.Locale('hu_HU.UTF-8'))

with open("hu") as infile:
    hu_collection = infile.read().split("\n")

with open("own_collection.txt") as infile:
    own_collection = infile.read().split("\n")


union_set = set(hu_collection).union(set(own_collection))
union = sorted(set(e for e in union_set if len(e) > 1), key=collator.getSortKey)

with open("hungarian_swear_words.txt", "w") as outfile:
    outfile.write("\n".join(union))
