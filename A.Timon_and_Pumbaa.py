def timon_ans(arr):
    a = arr[0]
    b = arr[1]
    if a-b>=0:
        print(a-b)
    else:
        print(0)
    
user_input = input("")
split_input = user_input.split()
new_array = [int(num) for num in split_input]
timon_ans(new_array)