# a 

symbol = input("Symbol tvořící čtverec: ") + " "

def square_a(size):
    n = 0
    k = size
    for i in range(size):
       print((" ") * n + symbol * k)
       n += 2
       k -= 1
      
square_a(int(input("Strana čtverce (sudé číslo): ")))

# b

symbol = input("Symbol tvořící čtverec: ") + " "

def square_b(size):
    n = 0
    k = size
    for i in range(size):
       print(symbol * n + " " * k)
       n += 1
       k -= 1
       
square_b(int(input("Strana čtverce (sudé číslo): ")))

# c - pro přehlednost píšu už jen funkce (bez inputů od uživatele)

def square_c(size):
    n = 0
    k = size
    for i in range(int(size/2)):
       print(" " * n + symbol * k + " " * n)
       n += 2
       k -= 2
    for i in range(int(size/2)):
        print(" " * size) 

# d

def square_d(size):
    n = size
    k = 0
    for i in range(int(size/2)):
        print(" " * size)   
    for i in range(int(size/2)):
       print(" " * n + symbol * k + " " * n)
       n -= 2
       k += 2
