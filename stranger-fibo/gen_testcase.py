import random
import sys
import os
import string
import itertools

random.seed()


def main(source, folder_name):
    config = [
        # (range(20, 30), (200, 500)),
        (range(1, 11), (1, 100)),
        (range(11, 21), (-100, -1)),
        (range(21, 31), (100, 10000)),
        (range(31, 41), (10000, 100000)),
        (range(41, 51), (1000000, 1500000)),
    ]
    for ran, cfg in config:
        for i in ran:
            file_name_in = "test%03d.txt" % i
            file_name_out = "out%03d.txt" % i

            in_text = gen_testcase(cfg)
            in_handle = open(os.path.join(folder_name, file_name_in), "w")
            in_handle.write(in_text)
            in_handle.close()

            print("python %s < %s > %s" % (
                source, file_name_in, file_name_out))


def generate_random_string(n=7):
    return ''.join([c for i in range(n) for c in random.choice(string.lowercase)])


def gen_testcase(cfg):
    n = random.randint(cfg[0], cfg[1])
    # k = random.randint(cfg[0], cfg[1])
    # arr = []
    txt = "%s\n" % n

    return txt


if __name__ == '__main__':

    folder_name = sys.argv[2]
    source = sys.argv[1]
    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
        except Exception as e:
            print(e)
            sys.exit(1)
    main(source, folder_name)
