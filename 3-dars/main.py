# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# my_list.sort()
# print(my_list)

# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list)
# print(sorted_list)  # [1, 1, 3, 4, 5, 9]
# print(my_list)      # [3, 1, 4, 1, 5, 9]

# my_list = [3, 1, 4, 1, 5, 9]
# my_list.sort(reverse=True)
# # my_list.sort()
# print(my_list)  # [9, 5, 4, 3, 1, 1]

# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)  # [9, 5, 4, 3, 1, 1]
# print(my_list)      # [3, 1, 4, 1, 5, 9]

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged_list = list1 + list2
# print(merged_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# import itertools

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined_list = list(itertools.chain(list1, list2))
# print(combined_list)

# multi_dimensional_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     'hello',
#     ["Hello", "python"],

# ]

# print(multi_dimensional_list[4][1])  # 3
# multi_dimensional_list.append([10, 11, 12])
# multi_dimensional_list.insert(2, ['Behruz', 'Umid'])
# print(multi_dimensional_list)

# multi_dimensional_list[0] = [13, 14, 15]
# print(multi_dimensional_list)

# multi_dimensional_list[1][1] = 99
# print(multi_dimensional_list)

# my_list = [1, 2, 3]
# multiplied_list = my_list * 2
# print(multiplied_list)

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # True
# print(6 in my_list)  # False


# my_list = input("sonlarni taqoslsh uchun ikkta son kiriting:").split("")
# a = int(n[0])
# b = int(n[1])
# if a>b: max= a
# else:

# my_list = [1, 2, 3, 5, 8, 6, ]
# my_list.sort( reverse=True)
# # print(sorted_list)
# print(my_list)

# list1= [1, 2, 23,]
# list2 = [8, 12, 1]

# merged_list = list1 + list2
# merged_list.sort()
# print(merged_list)


# davlatlar = ["Uzbekistan", "India", "Japan"]
# sorted_list = sorted(davlatlar, reverse=False )
# print(sorted_list)

raqamlar = [2, 8, 1, 9]
# eng_katta = max(raqamlar)
# eng_kichik = min(raqamlar)
# print(f"Raqamlar ro'yhatimiz ichida eng kattasi {eng_katta}")
# print(f"Raqamlar ro'yhatimiz ichida eng kichigi {eng_kichik}")

yigindi = sum(raqamlar)
print(yigindi)