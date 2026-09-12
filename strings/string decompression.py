compressed=input("Enter a string: ")
result=""
i=0
while i<len(compressed):
    char=compressed[i]
    i+=1
    num_str=""
    while i<len(compressed) and compressed[i].isdigit():
        num_str+=compressed[i]
        i+=1
    count=int(num_str)
    result+=char*count
print("The decompressed string is: ", result)