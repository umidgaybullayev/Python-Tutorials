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

Pythonda ro'yhatlarni birlashtirishni bir nechta usullari bor. Quyida ularga misollar ko'ramiz:

Birinchi usuli `+` operatori bilan birlashtirish:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

`.extend()` metodi bilan birlashtirish:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

`itertools.chain()` yordamida:

```python
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list(itertools.chain(list1, list2))
print(combined_list)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

### RO'YHAT ICHIDAGI RO'YHAT

Pythonda ro'yxatlar ichidagi ro'yxatlar, ya'ni `ko'p o'lchovli ro'yxatlar` yaratish va ulardan foydalanish juda oddiy. Quyida bunday ro'yxatlar bilan qanday ishlashni ko'rsatib beraman.

```python
multi_dimensional_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

#### Elementlarga murojaat qilish

Ro'yxat ichidagi ro'yxatdagi elementlarga indekslar yordamida murojaat qilish mumkin.

```python
print(multi_dimensional_list[0][2])  # 3
```
Yuqoridagi kodda `0` indexda turgan ro'yhatni tanlab oldim va tanlangan ro'yhatning ichidagi `2` indexda turgan elementga murojat qildim.

Ro'yxatlar ichidagi ro'yxatlarga yangi ro'yxat qo'shish mumkin:

```python
multi_dimensional_list.append([10, 11, 12])
print(multi_dimensional_list)
```

Ro'yhat ichidagi ro'yhatlarni o'zgartirish mumkin:

```python
multi_dimensional_list[0] = [13, 14, 15]
print(multi_dimensional_list)
```

Ma'lum bir ichki ro'yxat elementini o'zgartirish mumkin:

```python
multi_dimensional_list[1][1] = 99
print(multi_dimensional_list)
```

### RO'YHATNI KO'PAYTIRISH

```python
my_list = [1, 2, 3]
multiplied_list = my_list * 3
print(multiplied_list)
```

### RO'YHATDA E'LEMENT BORLIGINI TEKSHIRISH

Python'da ro'yxat ichida element borligini tekshirish uchun `in` operatoridan foydalanish mumkin. Bu operator juda sodda va qulay bo'lib, ro'yxat ichida ma'lum bir elementning mavjudligini aniqlash imkonini beradi.

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
```

## QATORLAR(TUPLES) VA ULAR BILAN ISHLASH

Qatorlar (`tuples`) Pythonda `o'zgarmas` ma'lumot tuzilmasi bo'lib, ularni bir marta yaratgandan keyin o'zgartirib bo'lmaydi. Ular ro'yxatlar (`lists`) ga o'xshash, lekin qatorlar bir marta yaratib olingandan keyin o'zgartirilmaydi, ya'ni ularga yangi element qo'shib bo'lmaydi, mavjud elementlarni o'chirib bo'lmaydi yoki o'zgartirib bo'lmaydi. Qatorlar ko'pincha o'zgarmas ma'lumotlar to'plamini saqlash uchun ishlatiladi.

```python
rgb = ('red', 'green', 'blue')
```
