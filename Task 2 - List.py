List = list(range(1,21))

print("List of numbers from 1 to 20: ")
for num in List:
    print(num)

print("And here are the numbers divisible by 3 from the previous list: ")
for num in List:
    if num%3==0:
        print(num)

