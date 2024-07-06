#!/usr/bin/env python3

def transform(s1, s2):
    #split the input strings into lists of words
     w1 = s1.split()
     w2 = s2.split()
     
     #convert te words to integeres using map() and list()
     
     n1 =list(map(int,w1))
     n2 =list(map(int,w2))
     
     # use zip( to pair up the corresponding integers from the two lines
     # and multiply them to get the result list)
     
     result = [ x * y for x , y  in zip(n1,n2)]
     
     return result
     
    
     

def main():
    pass

if __name__ == "__main__":
    main()
