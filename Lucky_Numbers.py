def lucky_number(num):
    a  = int(num/10)
    b = int(num%10)
    if b!=0:
        if a%b==0 or b%a==0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    
user_input = int(input(""))
lucky_number(user_input)