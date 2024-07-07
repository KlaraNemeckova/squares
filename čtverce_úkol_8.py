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

# e

def square_e(size):
    k = size
    n = 0
    for i in range(int(size/2)):
       print(" " * n + symbol * k + " " * n)
       n +=2
       k -=2
    n = size - 2
    k = 2
    for i in range(int(size/2)):
       print(" " * n + symbol * k + " " * n)
       n -= 2
       k += 2 

# f

def square_f(size):
    n = 1
    k = size - 1
    for i in range(int(size/2)):
        print(symbol * n + "  " * k + symbol * n)
        n += 1
        k -= 2
    n = 1
    k = int(size/2)
    for i in range(int(size/2)):
        print(symbol * k + "  " * n + symbol * k)
        n += 2
        k -= 1   

# g

def square_g(size):
   n = 0
   k = size
   for i in range(int(size/2)):
      print(symbol * n + " " * k)
      n += 1
      k -= 1
   n = 0
   k = int(size/2)
   for i in range(int(size/2)):
      print(symbol * k + (" ") * n)
      n += 2
      k -= 1         

# h

def square_h(size):
   n = 1
   k = int(size/2) - 1
   for i in range(int(size/2)):
      print("  " * k + symbol * n)
      n += 1
      k -= 1    
   n = 0
   k = int(size/2)
   for i in range(int(size/2)):
      print("  " * n + symbol * k)
      n += 1
      k -= 1
                  
       
