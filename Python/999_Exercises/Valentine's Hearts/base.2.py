peoplelist = ["U" , "me", "you", "ur mom", "ur dad", "ur lover", "ur dog", "ur cat", "ur lover", "ur friend"]
complimentlist = ["is hot", "be mine", "let's kiss", "you and me", "loves me", "- sweatheart", "can hug me", "marry me"]

import random
peoplenum = random.randrange(0, len(peoplelist))
compnum = random.randrange(0, len(complimentlist))
print()
print(peoplelist[peoplenum] + " " + complimentlist[compnum])