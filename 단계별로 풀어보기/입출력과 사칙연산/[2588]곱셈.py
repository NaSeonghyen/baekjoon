first_num = int(input())
second_num = int(input())

print(first_num * (second_num % 10))
print(first_num * (int(second_num / 10) % 10))
print(first_num * (int(second_num / 100)))
print(first_num * second_num)