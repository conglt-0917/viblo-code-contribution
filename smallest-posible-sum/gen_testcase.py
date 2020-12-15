import random
import sys
import os
import string
import itertools

random.seed()


def main(source, folder_name):
    config = [
        # (range(20, 30), (200, 500)),
        (range(1, 11), (4, 30, 4, 100)),
        (range(11, 21), (4, 30, 4, 100)),
        (range(21, 31), (4, 30, 4, 100)),
        (range(31, 41), (4, 30, 4, 100)),
        (range(41, 51), (4, 30, 4, 100)),
    ]
    for ran, cfg in config:
        for i in ran:
            file_name_in = "test%03d.txt" % i
            file_name_out = "out%03d.txt" % i

            # in_text = gen_testcase(cfg)
            # in_handle = open(os.path.join(folder_name, file_name_in), "w")
            # in_handle.write(in_text)
            # in_handle.close()

            print("python %s < %s > %s" % (
                source, file_name_in, file_name_out))


def generate_random_string(n=7):
    return ''.join([c for i in range(n) for c in random.choice(string.lowercase)])


def gen_testcase(cfg):
    l = random.randint(cfg[0], cfg[1])
    arr = [random.randint(cfg[2], cfg[3]) for i in range(l)]
    txt = "%s \n" % " ".join(map(str, arr))

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
