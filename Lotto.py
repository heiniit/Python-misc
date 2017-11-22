import numpy as np

print( "Random: \r\n" + str(np.random.rand()) )

a = np.ndarray(3)
for i in range(0, a.size):
    a[i] = np.random.random_sample()
print(a)

lotto_all = np.random.choice(range(1,39), 9, False)
lotto_numbers = lotto_all[:7]
lotto_additional = lotto_all[7:]
lotto_numbers.sort()
lotto_additional.sort()
print("This week Lotto-numbers are: " + str(lotto_numbers))
print("And additional numbers are: " + str(lotto_additional))

