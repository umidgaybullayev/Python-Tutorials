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

```python
print(my_list[0])  # Birinchi element
print(my_list[-1])  # Oxirgi element
```

### RO'YHAT UZUNLIGINI TOPISH

```python
print(len(my_list))
``` 

### RO'YHATGA E'LEMENT QO'SHISH

- **Oxiriga element qo'shish:** `append()`

```python
my_list.append(6)
print(my_list)
```