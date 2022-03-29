import sys,random
import time
import itertools

def main():
    words = "1234567890"
    temp = itertools.permutations(words,2)
    # print(temp)
    with open("dic.txt","w") as f:
        for i in temp:
            f.write("".join(i)+"\n")


if __name__ == '__main__':
    main()