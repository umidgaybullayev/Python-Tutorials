# PYTHON DASTURLASH ASOSLARI

## 5-dars Lug'at(Dictionary)

## LUG'AT(DICTIONARY) NIMA?

Python dasturlash tilida **lug'at**(`dictionary`) — `kalit-qiymat` juftliklarini saqlash uchun mo'ljallangan ma'lumotlar tuzilmasidir. `Lug'atlar` kalitlar yordamida ma'lumotlarga kirishni ta'minlaydi va ular tartibsiz, o'zgaruvchan (`mutable`) va takrorlanmas (`unique`) kalitlardan iborat bo'ladi.

### LUG'ATLARNING ASOSIY XUSUSIYATLARI
1. **Kalitlar va qiymatlar:**
    - Kalitlar (`keys`) va qiymatlar (`values`) juftliklar sifatida saqlanadi. Kalitlar unikal(`takrorlanmas`) bo'lishi kerak.
2. **Tartibsizlik:**
    - Python 3.7 va undan keyingi versiyalarida lug'atlar saqlash tartibini saqlaydi, lekin avvalgi versiyalarda tartibni saqlash kafolatlanmagan.
3. **O'zgaruvchanlik:**
    - Lug'atlar o'zgaruvchan bo'lib, yangi kalit-qiymat juftliklarini qo'shish, mavjudlarini o'zgartirish va o'chirish mumkin.
4. **Unikal Kalitlar:**
    - Har bir kalit faqat bir marta mavjud bo'lishi mumkin. Agar yangi kalit qo'shsangiz yoki mavjud kalitni yangilasangiz, eski qiymat yangisi bilan o'zgartiriladi.

### LUG'AT SINTAKSISI

```python
dict_name = {
    'key':'value'
}
```

### LUG'AT YARATISH
- Bo'sh lug'at yaratish:
```python
my_dict = {}
```

- Elementlar bilan lug'at yaratish:
```python
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
```

### LUG'ATLARNI BOSHQARISH

- Lug'atga element qo'shish uchun o'zgaruvchi nomidan kn `[]` qavs ochib ichiga kalit(key) ni beramiz, undan keyin qo'shmoqchi bo'lgan qiymat(value)imizni beramiz.
```python
my_dict['email'] = 'alice@example.com'
```

- Lug'atni yangilash:
```python
my_dict['age'] = 31
```
- Lug'at ichidagi e'lementlarni o'chirish uchun `del` funksiyasidan foydalanamiz:
```python
del my_dict['city']
```
- Lug'atdagi e'lementlarni o'chirish uchun `.pop()` metodidan ham foydalansak bo'ladi:
```python
my_dict.pop('email')
```

### E'LEMENTLARNI KO'RISH
- Kalitlarni olish:
```python
keys = my_dict.keys()
```
- Qiymatlarni olish:
```python
values = my_dict.values()
```