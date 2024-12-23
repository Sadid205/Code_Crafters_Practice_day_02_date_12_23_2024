def print_and_return():
    print("YES")
    return
def calculate(arr):
    a = arr[0]
    b = arr[1]
    c = arr[2]
    ans = arr[3]
    if(a+b*c==ans):
        print_and_return()
    elif(a+b-c==ans):
        print_and_return()
    elif(a-b+c==ans):
        print_and_return()
    elif(a-b*c==ans):
        print_and_return()
    elif(a*b+c==ans):
        print_and_return()
    elif(a*b-c==ans):
        print_and_return()
    else:
        print("NO")


user_input = input("")
input_list = user_input.split()
int_list = [int(num) for num in input_list]
calculate(int_list)