def k_divisors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)



user_input = int(input(""))
k_divisors(user_input)