								###Count Primes###

#Count the number of prime numbers less than a non-negative number, n.

#Refer this https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  and hints of the question in leetcode:
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes : Jikai Tang

#Answer is according to the hints and pseudo code mentioned in the quest


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
           return 0      # 1,2 are not primes
        A = [True] * n   # A[0] = True, A[1] = True, ... , A[n-1] = True
        for i in range(2,int(n**0.5)+1):
            if A[i]:                     #True 
               for j in range(i**2,n,i):   # removing all multiples of the values of i
                   A[j] = False
        return sum(A) - 2          # - 2 because 1 ad 2 are not primes. Written sum of all True values

