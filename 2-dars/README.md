# PYTHON DASTURLASH ASOSLARI

## 2-dars Oddiy matematik va mantiqiy amallar.

- Mavzular:
    - Arifmetik operatorlar
    - Solishtirish operatorlari
    - Mantiqiy operatorlar

## ARIFMETIK OPERATORLAR

Python dasturlash tilida arifmetik operatorlar matematik amallarni bajarish uchun ishlatiladi.

1. **Qo'shish** (`+`): Ikkita sonni qo'shish uchun ishlatiladi.

```python
a = 5
b = 3
c = a + b  # c 8 ga teng bo'ladi
print(c)
```

2. **Ayirish** (`-`): Ikkita sonni ayirish uchun ishlatiladi.
```python
a = 5
b = 3
c = a - b  # c 2 ga teng bo'ladi
print(c)
```

3. **Ko'paytirish** (`*`): Ikkita sonni ko'paytirish uchun ishlatiladi.
```python
a = 5
b = 3
c = a * b  # c 15 ga teng bo'ladi
print(c)
```

4. **Bo'lish** (`/`): Ikkita sonni bo'lish uchun ishlatiladi.

```python
a = 6
b = 3
c = a / b  # c 2.0 ga teng bo'ladi
print(c)
```

5. **Butun bo'lish** (`//`): Ikkita sonni butun qismiga bo'lish uchun ishlatiladi.

```python
a = 7
b = 3
c = a // b  # c 2 ga teng bo'ladi
print(c)
```

6. **Qoldiq** (`%`): Ikkita sonni bo'lgandan keyin qoldiqni topish uchun ishlatiladi.

```python
a = 7
b = 3
c = a % b  # c 1 ga teng bo'ladi
print(c)
```

7. **Daraja** (`**`): Bir sonni ikkinchi son darajasiga ko'tarish uchun ishlatiladi.

```python
a = 2
b = 3
c = a ** b  # c 8 ga teng bo'ladi
print(c)
```

## SOLISHTIRISH OPERATORLARI

Python dasturlash tilida `solishtirish` operatorlari ikki qiymatni `taqqoslash` uchun ishlatiladi.

1. **Teng** (`==`): Ikkita qiymat tengligini tekshiradi.

```python
a = 5
b = 3
result = (a == b)  # result False ga teng bo'ladi
print(result)
```

2. **Teng emas** (`!=`): Ikkita qiymat teng emasligini tekshiradi.

```python
a = 5
b = 3
result = (a != b)  # result True ga teng bo'ladi
print(result)
```

3. **Katta** (`>`): Chap tomondagi qiymat o'ng tomondagi qiymatdan katta ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a > b)  # result True ga teng bo'ladi
print(result)
```

4. **Kichik** (`<`): Chap tomondagi qiymat o'ng tomondagi qiymatdan kichik ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a < b)  # result False ga teng bo'ladi
print(result)
```

5. **Katta yoki teng** (`>=`): Chap tomondagi qiymat o'ng tomondagi qiymatdan katta yoki teng ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a >= b)  # result True ga teng bo'ladi
print(result)
```

6. **Kichik yoki teng** (`<=`): Chap tomondagi qiymat o'ng tomondagi qiymatdan kichik yoki teng ekanligini tekshiradi.

```python
a = 5
b = 3
result = (a <= b)  # result False ga teng bo'ladi
print(result)
```

## MANTIQIY OPERATORLAR

Python dasturlash tilida mantiqiy operatorlar mantiqiy qiymatlarni (`True` yoki `False`) birlashtirish yoki taqqoslash uchun ishlatiladi.

1. **va** (`and`): Ikkala shart ham `True` bo'lsa, natija `True` bo'ladi, aks holda `False`.

```python
a = True
b = False
result = a and b  # result False ga teng bo'ladi
print(result)
```

2. **yoki** (`or`): Hech bo'lmaganda bitta shart `True` bo'lsa, natija `True` bo'ladi, aks holda `False`.

```python
a = True
b = False
result = a or b  # result True ga teng bo'ladi
print(result)
```

3. **emas** (`not`): Shartning mantiqiy qiymatini teskariga o'zgartiradi (`True` bo'lsa `False`ga, `False` bo'lsa `True`ga).

```python
a = True
result = not a  # result False ga teng bo'ladi
print(result)
```

Quyidagi misolda mantiqiy operatorlar qanday ishlashini ko'rishimiz mumkin:

```python
x = 5
y = 10
z = 5

# and operatori
result = (x == z) and (y > x)  # result True ga teng bo'ladi, chunki ikkala shart ham True

# or operatori
result = (x == z) or (y < x)  # result True ga teng bo'ladi, chunki birinchi shart True

# not operatori
result = not (x == z)  # result False ga teng bo'ladi, chunki x va z teng
```