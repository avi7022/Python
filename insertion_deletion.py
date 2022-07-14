# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:33:33 2022

@author: Abhishek
"""
#Hackerrank solution
def lcs(str1,str2,m,n):
    
    #Initializing array of L[m+1][n+1]= 0
    L = [[ 0 for i in range(n+1)] for i in range(m+1)]
    #comparing oldpasswad and newpasswd
    for i in range(m+1):
        for j in range(n+1):
            if (i == 0 or j == 0):
                L[i][j]=0
            elif (str1[i-1] == str2[j-1]):
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    # for i in range(m+1):
    #     for j in range(n+1):
    #         print(L[i][j],end=" ")
    return L[m][n]

def printMinDelAndInsert(str1, str2):
    m = len(str1)
    # print(m)
    n = len(str2)
    leng = lcs(str1, str2, m, n)
    # print(leng)
    print("Minimum number of deletions = ",
          m - leng, sep=' ')
    print("Minimum number of insertions = ",
          n - leng, sep=' ')
    print("total operation = ",(m-leng)+(n-leng),sep='')
 
 
# Driver Code
str1 = "password"
str2 = "p@ssw#rd"
 
# Function Call
printMinDelAndInsert(str1, str2)
