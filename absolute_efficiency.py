from random import*

from utils import *

def absolute_efficiency(file_res):
    number_link = 0
    my_file=open(file_res,"r")
    my_file1 = open(file_res, "r")
    number_lines=sum(1 for _ in my_file1)
    total=0
    for line in  reversed(list(my_file)):
        line_split=line.split(" ")
        if number_link==0:
            previous=int(line_split[0])
            total+=number_lines
        else:
            current=int(line_split[0])
            total+=((previous-current)*number_lines)
            previous=current
        #previous=line_split[]
        number_lines-=1
        number_link+=1
    return total


def main():
    print(absolute_efficiency("testtt"))


if __name__ == '__main__':
    main()

