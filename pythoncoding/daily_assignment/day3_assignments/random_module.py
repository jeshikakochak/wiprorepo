#random module
import random
print("random integer:",random.randint(1,100))
rand_list=[random.randint(1,50) for _ in range(5)]
print("random list:",rand_list)
random.shuffle(rand_list)
print("shuffled list:",rand_list)
