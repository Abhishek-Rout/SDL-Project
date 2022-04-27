import nltk
import math
import socket

# Prime number
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

# Fibonacci series up to n
def fib(n):   
    a, b = 0, 1
    l=[]
    while a < n:
        l.append(a)
        a, b = b, a+b
    return l


# Factorial of n
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)


# synonym
def synonyms(word):
    synonym = []
    for syn in nltk.wordnet.synsets(word):
        for lm in syn.lemmas():
                synonym.append(lm.name())
    return (set(synonym))

# antonyms
def antonyms(word):
    antonym = []
    for syn in nltk.wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonym.append(lm.antonyms()[0].name())
    return (set(antonym))


# host ip
def get_hostname_IP():
    hostname = input("Please enter website address(URL):")
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')
