import sys
import os
from math import floor
from numpy.random import randint
from random import random, randrange, choice
# test.describe('Fixed Tests')
# test.it('Should pass example tests')
# test.assert_equals(solution([6, 9, 21]), 3*3)

# test.assert_equals(solution([9]), 9*1)
# test.assert_equals(solution([30, 12]), 6*2)
# test.assert_equals(solution([11, 22]), 11*2)

# test.assert_equals(solution([1, 21, 55]), 1*3)
# test.assert_equals(solution([4, 16, 24]), 4*3)
# test.assert_equals(solution([3, 13, 23, 7, 83]), 1*5)

# test.assert_equals(
#     solution([60, 12, 96, 48, 60, 24, 72, 36, 72, 72, 48]), 12*11)
# test.assert_equals(
#     solution([71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71]), 71*13)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

for i in range(31, 41):
    mult = 1
    while(random() > 0.4):
        mult *= choice(primes)
    arr = list(map(lambda n: n*max(floor(n/mult), 1),
                   [randrange(50, 500)*mult for _ in range(randrange(10, 100))]))

    txt = "%s \n" % " ".join(map(str, arr))

    file_name_in = "test%03d.txt" % i
    file_name_out = "out%03d.txt" % i
    in_handle = open(os.path.join('testcases', file_name_in), "w")
    in_handle.write(txt)
    in_handle.close()
    print("Testing for\n[{0}]".format(", ".join(map(str, arr))))


for i in range(41, 51):
    mult = 1
    while(random() > 0.4):
        mult *= choice(primes)
    arr = list(map(lambda n: n*max(floor(n/mult), 1),
                   [n * mult for n in randint(50, 500, size=randrange(30000, 50000))]))
    txt = "%s \n" % " ".join(map(str, arr))
    file_name_in = "test%03d.txt" % i
    file_name_out = "out%03d.txt" % i
    in_handle = open(os.path.join('testcases', file_name_in), "w")
    in_handle.write(txt)
    in_handle.close()
    print("Testing for\nlist too big to be displayed")
