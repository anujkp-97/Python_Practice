# Adding the numbers from 1 to 100 also even number
# use of range()

# for i in range(1,11,2):
#     print(i)

result =0
target = int(input())
for i in range(2, target+1, 2):
    result = result +i

print(result)
