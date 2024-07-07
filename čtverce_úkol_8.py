
symbol = input("Symbol tvořící čtverec: ") + " "

# a 
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

