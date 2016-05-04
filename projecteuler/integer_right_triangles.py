'''
Created on Oct 31, 2015

@author: Bryan
'''
import math

def main(p):
    num_solns = 0
    for x in range(1,p):
        y = 1
        for y in range(x,p-x):
            if x + y < p:
                z = p - x - y
                if z == math.sqrt(x*x + y*y):
                    num_solns += 1
    return num_solns
                    

if __name__ == "__main__":
    solns = {}
    max_val = 0
    max_key = ""
    # 420: 5 has the max number of solutions for p <= 420
    for i in range (420,1000):
        num_solns = main(i)
        solns[i] = num_solns
        if num_solns > max_val:
            max_val = num_solns
            max_key = i
        
    print ("Max key: ", max_key, ", Max value: ", max_val)