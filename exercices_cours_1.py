# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:39:25 2021

@author: guillaume
"""



#EXERCICE 1 : MULTIPLES OF 3 OR 5 : 
  

base = 0 

for i in range (1 , 1000 ):
    if i % 3 == 0 or i % 5 == 0:
        
        base +=i #on somme tout les i dont la divison par 3 ou 5 donne un reste nul , i étant dans l'intevalle [1;1000]
        
print(base)        

    

#EXERCICE 2 : 10001st PRIME NUMBER : 


def nth_prime(nth):
 primes = list()
 i=1
 while len(primes)<nth:
    i+=1
    is_prime = True
    for j in range(2,(round(i/2)+2)):
        if i/j == round(i/j) and i!=j:
            is_prime = False

        if is_prime == False:
            break
    if is_prime == True : 
        primes.append(i)

 print(primes[nth-1])
 
nth_prime(1)

nth_prime(10001)

#EXERCICE 3 : Nombre de dimanche tombés le premier du mois pendant le 21e siècle : du 01/01/1901 au 31/12/2000
    



