import requests
import threading
from winsound import Beep
from random import randint


def req(d):
    r = requests.post("http://{}/{}".format(target, d))
    status = r.status_code
    if status != 404:
        # print(f"\tpath=\"{d}\"\t{status=}")
        print(f"\t{status=}")


def run():
    with open('common.txt') as file:
        file = list(file)
        l = len(file)
        for i, line in enumerate(file):
            ln = line.rstrip()
            req(ln)
            loading_bar(i + 1, l, ln)
            # Just for kool guy
            # t = threading.Thread(target=loading_bar, args=(i + 1, l, ln))
            # t.start()
            t1 = threading.Thread(target=beep)
            t1.start()


def beep():
    Beep(randint(700, 1500), randint(50, 200))


def loading_bar(n, l, ln):
    print("\rPwning : {} ({:.2f}%)\tpath=/{}".format("█" * round(n / l * 100 / 2), n / l * 100, ln), end="")


def test_conn(tar):
    try:
        requests.post("http://{}".format(tar))
    except Exception as e:
        print("ERROR: {}".format(e))
        exit()


if __name__ == '__main__':
    target = input("Input target : ")
    test_conn(target)
    print('-' * 50)
    run()
