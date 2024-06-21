#!/usr/bin/env python3

import numpy as np

def diamond(n):
    x = np.eye(n,dtype=int)
    
    x = np.concatenate([x[::-1],x[:,1:]],axis=1)
    
    return np.concatenate([x[:-1],x[::-1]],axis=0)

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
