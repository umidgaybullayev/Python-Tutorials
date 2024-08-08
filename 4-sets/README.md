# PYTHON DASTURLASH ASOSLARI

## 4-dars To'plamlar(sets)

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

To'plamga ko'proq e'lement qo'shish uchun `.update(values)` metodidan foydalanamiz:
```python
my_set.update([6, 7, 8])
print(my_set)  # {1, 2, 4, 5, 6, 7, 8}
```

### TO'PLAM(SET)DAN E'LEMENT O'CHIRISH
To'plamdan e'lement o'lib tashlash uchun `.remove(value)` metodidan foydalaniladi:
```python
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}
```

**Natija:** `{1, 2, 4, 5}`

Agar to'plamda e'lement mavjud bo'lmasa, `.remove(value)` xato beradi, `.discard(value)` xato bermaydi:

```python
my_set.remove(7)
print(my_set)  # {1, 2, 4, 5}
```

**Natija:** `KeyError: 7` 


```python
my_set.discard(7)
print(my_set)  # {1, 2, 4, 5}
```
**Natija:** `{1, 2, 3, 4, 5`

### TO'PLAM OPERATSIYALARI

To'plamlarda `.intersection()` metodi ikki yoki undan ortiq to'plamlar(sets) o'rtasida umumiy bo'lgan elementlarni aniqlash uchun ishlatiladi. Bu amalda natija sifatida barcha berilgan setlarda mavjud bo'lgan e'lementlar qaytariladi.

Python dasturlash tilida **to'plamlar**(`sets`) kesishishini amalga oshirish uchun bir nechta usullar mavjud:
1. **`&` operatori:** Kesishish amali uchun maxsus operator.
2. **`.intersection()` metodi:** Bir yoki bir nechta setlar bilan kesishish amalga oshiriladi.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
```
1-qatorda `set1` nomli to'plam yaratdik.
2-qatorda `set2` nomli to'plam yaratdik.
3-qatorda `set1` nomli to'plam uchun `.intersection()` metodiga `set2` nomli to'plamni berdik. Shunda ikkala to'plam ichida bir xil bo'lgan elementlarni chiqaradi.

