# Write a program to calculate pow(x,n)
#
#
# Input : x = 2, n = 3
# Output : 8
#
# Input : x = 7, n = 2
# Output : 49



def power(x, n):

    if (n == 0):
        return 1
    temp = power(x, int(n / 2))

    if (n % 2 == 0):
        return temp * temp
    else:
        if (n > 0):
            return x * temp * temp
        # else:
        #     return (temp * temp) / x

# Driver Code
x = 3
n = 5
print power(x, n)


"""
pow(3,5)        = 3 * 9 * 9  = 243
pow(3,2)        = 3 * 3      = 9
pow(3,1)        = 3 * 1 * 1  = 3
pow(3,0)        = 1
"""