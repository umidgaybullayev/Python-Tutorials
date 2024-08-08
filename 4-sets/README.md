# PYTHON DASTURLASH ASOSLARI

## 4-dars sets

Python dasturlash tilida toplamlar(`sets`) — bu to‘plamga qo‘shilgan elementlar faqat bir martadan saqlanadigan va tartibi ahamiyatga ega bo‘lmagan ma'lumotlar tuzilmasi. Bu ma'lumotlar tuzilmasi quyidagi asosiy xususiyatlarga ega:
- **Noyob elementlar:** Setdagi barcha elementlar yagona va takrorlanmaydi.
- **Tartibga ega emas:** Setdagi elementlar tartibi muhim emas va ular indekslanmaydi.
- **O'zgaruvchanlik:** Setlar o‘zgaruvchan bo‘lib, ularga yangi elementlarni qo‘shish yoki olib tashlash mumkin.

### TO'PLAM(SET) YARATISH

```python
# Bo'sh set yaratish
my_set = set()

# Elementlar bilan set yaratish
my_set = {1, 2, 3, 4, 5}
```

### TO'PLAM(SET)GA E'LEMENT QO'SHISH
To'plamga yangi e'lement qo'shish uchun `.add(value)` metodidan foydalaniladi:
```python
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}
```

**Natija:** `{1, 2, 3, 4, 5}`

### TO'PLAM(SET)DAN E'LEMENT O'CHIRISH
To'plamdan e'lement o'lib tashlash uchun `.remove(value)` metodidan foydalaniladi:
```python
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}
```

**Natija:** `{1, 2, 4, 5}`

Agar to'plamda e'lement mavjud bo'lmasa, `.remove()` xato beradi, `.discard()` xato bermaydi:

```python
my_set.remove(7)
print(my_set)  # {1, 2, 4, 5}
```

Natija: <br>
`Traceback (most recent call last):
  File "C:\Users\VICTUS\Desktop\Python-Tutorials\4-sets\main.py", line 3, in <module>
    my_set.remove(7)
KeyError: 7` 


```python
my_set.discard(6)
print(my_set)  # {1, 2, 4, 5}
```