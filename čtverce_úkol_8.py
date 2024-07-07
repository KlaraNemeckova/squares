symbol = input("Symbol tvořící čtverec: ") + " "

def square_a(size):
    n = 0
    k = size
    for i in range(size):
       print((" ") * n + symbol * k)
       n += 2
       k -= 1
      
square_a(int(input("Strana čtverce (sudé číslo): ")))


