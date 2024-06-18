#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    A = np.sum(X*Y, axis=1)
    B = np.sqrt(np.sum(np.square(X),axis=1)) * np.sqrt(np.sum(np.square(Y),axis=1))
    return np.degrees(np.arccos(np.clip(A/B,-1.0,1.0)))
                
    
def main():
    X = np.array([[0,0,1], [-1,1,0]])
    Y = np.array([[0,1,0], [1,1,0]])
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
