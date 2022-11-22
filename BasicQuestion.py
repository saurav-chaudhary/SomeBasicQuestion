# In this script i did some basic question with optimal way,


# given number is prime or not, by optimal solution
# A = 13

# upperLimit = int(A**0.5)
# print(upperLimit)
# def isPrime( A):
#     upperLimit = int(A ** 0.5)
#     if A==1:
#         return 0
#     for i in range(2, upperLimit + 1):
#         if i < A and A % i == 0 and A == 1:
#             return 0
#     return 1

# def isPrime(A):
#     upper = int(A ** 0.5)
#     for i in range(2, upper+1):
#         if i < A and A % i == 0:
#             return 0
#     return 1
# print(isPrime(A))

# Find GCD in given two number with optimal solution
# def GCD( A, B):
#     if B == 0:
#         return A
#     return GCD( B, A % B)
# print(GCD(4,6))


# reverse number solution

# def reverseNumber(A):
#     if A<0:
#         sign = -1
#     else:
#         sign = 1
#     A = abs(A)
#     String_number = str(A)
#     reverse_number = String_number[::-1]
#     result = int(reverse_number)
#     if result > 2*31 -1:
#         return 0
#     return result*sign
#
# print(reverseNumber(-1234567891))
# def finalLastDigit(A,B):
#     # return (A**B)%10
#     if A == 1:
#         return 1
#     if B % 4 == 0:
#         B == 4
#     else:
#         B = (B % 4)
#     A = A % 10
#
#     return (A ** B) % 10
#
# print(finalLastDigit(2,10))


# given string is palindrome or not using recursion
# def isPalindrome(A,r,l):
#
#     if r == l:
#         return True
#     if r>=l:
#         return True
#     if A[r] != A[l]:
#         return False
#     return isPalindrome(A,r+1,l-1)
#
# A = "aba"
# l = len(A)
# print(l)
# l = l-1
# r = 0
# print(isPalindrome(A,r,l))
