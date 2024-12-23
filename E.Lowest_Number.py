def LowestNumber(size,array):
    temp = {
        "value":array[0],
        "position":1
    }
    
    for i in range(1,size):
        if array[i]<temp["value"]:
            temp["value"] = array[i]
            temp["position"] = i+1

    print(f"{temp['value']} {temp['position']}")

size = int(input(""))
array_input = input("")
split_input = array_input.split()
new_array = [int(num) for num in split_input]
LowestNumber(size,new_array)