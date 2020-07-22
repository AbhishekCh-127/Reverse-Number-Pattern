#!/usr/bin/env python
# coding: utf-8

# In[157]:


rows=int(input())
p=2*rows+1
for i in range(1,rows+1):
    n=1
    for j in range(0,p):
        if j<i:
            print(n,end="")
            n+=1
        if j>i and j<p-i:
            print(" ",end="")
    
    count=i
    k=i
    for j in range(p,0,-1):
        if j<=count:
            print(k,end="")
            k-=1
        
    print()        

