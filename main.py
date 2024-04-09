# Remove elements from a List while iterating in Python

my_list = [22, 33, 66, 77, 99]

for item in my_list.copy():
    if item < 50:
        my_list.remove(item)

print(my_list)  # 👉️ [66, 77, 99]