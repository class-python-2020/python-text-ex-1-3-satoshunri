import random
random.seed(1)
msgs = ["Hi", "Hello","Good morning","Good night","See you later","How are you","Have a good day"]
with open("some.txt","w")as f:
     for i in range(100000):
         f.write("{}, {}\n".format(i, random.choice(msgs)))