import time
import random
start = time.time()
num_terms = 200
fibonacci = [1, 1, 2]
while num_terms > len(fibonacci):
    next_term = fibonacci[-1] + fibonacci [-2] + fibonacci [-3]
    fibonacci.append(next_term)
end = time.time()
print(fibonacci)


i = random.randrange(len(fibonacci))
x = fibonacci[i]
print("случайное число номер:",i + 1,"-", x)
print("время выполнения:", time.time() - start,"секунд")