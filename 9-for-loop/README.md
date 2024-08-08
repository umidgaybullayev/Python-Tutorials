# PYTHON DASTURLASH ASOSLARI

## 4-dars For takrorlash operatori

## `for` BILAN TANISHAMIZ

Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. 

Mana shunday vaziyatlarda bizga `for` operatori yordam beradi. Dasturlashda bu **tsikl(loop)** deb ataladi. 

Quyidagi misolda `fruits` ro'yhati bor, har bir mevani alohida qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Natija:** <br>
`apple` <br>
`banana` <br>
`cherry` <br>

1-qatorda `fruits` degan ro'yhat yaratdik va uni mevalarni nomi bilan to'ldirdik. <br>
2-qatorda `for` tsiklini boshladik. Bu qator pythonga `fruits` degan ro'yhatdan har bir elementni olib uni yangi, `fruit` degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nomni berishimiz mumkin tushunarli bo'lishi uchun `fruit` deb nomladik). <br>
3-qatorda `fruit` degan o'zgaruvchining qiymatini terminalga chiqardik. Bu tsikl to `fruits` ro'yhatidagi elementlar tugaguncha takrorlanadi.

> [!NOTE]
> **"For"** so'zi ingliz tilidan **"uchun"** deb tarjima qilinadi.

For loop orqali string ichidagi elementlarni ham alohida qatordan chiqarishimiz mumkin:

```python
for x in "banana":
  print(x)
```
**Natija:**

`b` <br>
`a` <br>
`n` <br>
`a` <br>
`n` <br>
`a` 

