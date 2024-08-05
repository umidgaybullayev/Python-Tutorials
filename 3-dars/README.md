# PYTHON DASTURLASH ASOSLARI

## 3-dars Ro'yxatlar va qatorlar.

- Mavzular
    - Ro'yxatlar(lists) bilan ishlash.
    - Qatorlar (tuples) va ular bilan ishlash.
    - Indekslar va bo'laklash (slicing).

## RO'YHATLAR(LISTS) BILAN ISHLASH

Python dasturlash tilida ro'yxatlar (`lists`) bir nechta qiymatlarni bitta o'zgaruvchiga saqlash imkonini beradi. Ro'yxatlar `dinamik` tuzilma bo'lib, ular yaratishdan keyin ham o'zgartirilishi mumkin.

### RO'YHAT YARATISH

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
```

### RO'YHATLARGA MUROJAT QILISH

> [!CAUTION]
> Dasturlash olamida indeks `0` dan boshlanadi! Ya'ni Listning birinchi elementing tartib raqami (indeksi) `0` ga, ikkinchi elementning indeksi `1` ga teng va hokazo.

```python
print(my_list[0])  # Birinchi element
print(my_list[-1])  # Oxirgi element
```

### RO'YHAT UZUNLIGINI TOPISH

Ro'yhat uzunligini topish ya'ni ichida nechta element borligini topish uchun `len()` funksiyasidan foydalanamiz.

```python
print(len(my_list))
``` 

### RO'YHATGA E'LEMENT QO'SHISH

- **Oxiriga element qo'shish:** `.append()`

```python
my_list.append(6)
print(my_list)
```

- **Belgilangan joyga element qo'shish:** `.insert()`

```python
my_list.insert(2, 99)  # 2-pozitsiyaga 99 ni qo'shish
print(my_list)
```

### E'LEMENTLARNI O'CHIRISH

- **Belgilangan elementni o'chirish:** `.remove()`

```python
my_list.remove(99)
print(my_list)
```

- **Indeks bo'yicha elementni o'chirish:** `.pop(index)`

```python
my_list.pop(0)  # Birinchi elementni o'chirish
print(my_list)
```

- **Oxirgi elementni o'chirish:** `.pop()`

```python
my_list.pop()
print(my_list)
```

### RO'YHATNI TOZALASH

Ro'yhatni tozalash uchun `.clear()` metodidan foydalanamiz.

```python
my_list.clear()
print(my_list)
```

### RO'YHATNI SARALASH

Ro'yhatni saralash uchun `.sort()` metodidan foydalanamiz. `.sort()` metodi ro'yhatimiz raqamlardan iborat bo'lsa o'sib borish tartibida saralaydi, agar ro'yhatimiz stringdan(harflardan) tashkil topgan bo'lsa alifbo tartibida saralaydi.

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)
```

### RO'YHATNI TESKARIGA O'ZGARTIRISH

Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning uchun 
`.reverse()` metodidan foydalanamiz.

```python
my_list.reverse()
print(my_list)
```

### RO'YHATNI BIRLASHTIRISH

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)
```

### RO'YHAT ICHIDAGI RO'YHAT

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # 5 ga murojaat
```

### RO'YHATNI KO'PAYTIRISH

```python
my_list = [1, 2, 3]
multiplied_list = my_list * 3
print(multiplied_list)
```

### RO'YHATDA E'LEMENT BORLIGINI TEKSHIRISH

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
```