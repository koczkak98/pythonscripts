def fib(n):
    a0 = 0
    a1 = 1
    print(a0)
    for i in range(n):
        a2 = (a0 + a1)
        a0 = a1
        print(a1)
        a1 = a2

        

def main():
    print("coding...")
    fib(2)
    
        
main()