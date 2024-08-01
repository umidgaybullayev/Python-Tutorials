# PYTHON DASTURLASH ASOSLARI

## 1-dars O'zgaruvchilar va ma'lumot turlari.

- Mavzular:
    - O'zgaruvchilar, ma'lumot turlari (int, float, str, bool).
    - O'zgaruvchilarni e'lon qilish va ularga qiymat berish.

>[!NOTE]
> Python dasturlash tilida o'zgaruvchilar va ma'lumot turlari dasturlarni tuzishda juda muhim. Quyida o'zgaruvchilar va ularning turli ma'lumot turlari haqida ma'lumot beriladi.

## O'ZGARUVCHILAR

**O'zgaruvchi** - kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy. `Python`da o'zgaruvchi yaratish va unga qiymat berish juda oson:

![alt text](images/image.png)

Quyidagi misolda 4 ta o'zgaruvchi yaratdik (`x`, `y`, `name` va `is_student`) va ularga har xil ma'lumot yukladik.

```python
x = 5 # Butun son (int)
y = 3.14 # Haqiqiy son (float)
name = "Alice"  # Matn (str)
is_student = True  # Mantiqiy qiymat (bool)
print(x)
print(y)
print(name)
print(is_student)
```

Natija: <br>
`5` <br>
`3.14` <br>
`Alice` <br>
`True`

O'zgaruvchi (variable) diyilishini sababi uning qiymati istalgan payt o'zgarishi mumkin:

```python
ism = 'Alisher'
print(ism)
ism = "Muhammad"
print(ism)
```

Natija: <br>
`Alisher` <br>
`Muhammad`

Yuqoridagi misolda `ism` nomli o'zgaruvchiga avval `Alisher` keyin esa `Muhammad` deb qiymat berdik.

### O'ZGARUVCHILARNI NOMLASH
> [!CAUTION]
> O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
> - O'zgaruvchi nomi harf yoki pastki chiziq (`_`) bilan boshlanishi kerak
> - O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
> - O'zgaruvchi nomida faqatgina lotin alifbosi harflari (`A-z`), raqamlar (`0-9`) va pastki chiziq (`_`) qatnashishi mumkin
> - O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
> - O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (`ism`, `ISM`, va `Ism` uchta turli o'zgaruvchi)

Qo'shimcha qoidalar:
- O'zgaruvchi nomini kichik harflar bilan yozing.
- O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (`_`) bilan ajrating (`ism_sharif="Umid G'aybullayev"`) 
- O'zgaruvchiga tushunarli nom bering (`y=20` emas `yosh=20`, `d="Korea"` emas `davlat = "Korea"` va hokazo)
- Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va maxsus kalit so'zlarning (keywords) nomini bermang. Kalit so'zlar ro'yhatini ko'rish uchun python faylga  uyidagi kodni yozamiz:
```python
import keyword
print(keyword.kwlist)
```
Marhamat, ekraningizda Pythondagi maxsus kalit so'zlar ro'yhatini ko'ryapsiz:
![alt text](images/keyword.png)

## MA'LUMOT TURLARI
Python dasturlash tilida 7ta ma'lumot turi bor, ular quyidagilar:

![alt text](images/data_types.png)

- **String(str)** - Matnli ma'lumotlarni ifodalaydi. Masalan: `"hello"`, `'world'`, `"123"`.
    ```python
    # ikkitalik qo'shtirnoqlar bilan
    text = "Hello world"

    # bittalik qo'shtirnoqlar bilan
    text = 'Hello world'

    # Ko'p qatorli stringlar uchlik qo'shtirnoqlar bilan
    text = """This is a
    multiline string."""

    text = '''This is also a
    multiline string.'''
    ```
    ### STRING USTIDA AMALLAR
    Matnlarni qo'shish uchun `+` operatoridan foydalanamiz.
    ```python
    ism = "Umid"
    print("Mening ismim " + ism)
    ```
    **Natija:** `Mening ismim Umid`
    ```python
    ism = "Umid"
    familiya = "G'aybullayev"
    print(ism + familiya)
    ```
    **Natija:** `UmidG'aybullayev` <br>
    Yuqoridagi kodimizda ism va familiya qo'shilib qoldi, uni to'g'irlash uchun quyidagi ko'rinishda yozamiz:
    ```python
    ism = "Umid"
    familiya = "G'aybullayev"
    print(ism + ' ' + familiya)
    ```
    **Natija:** `Umid G'aybullayev`

    ### STRING UZUNLIGINI ANIQLASH
    Matnlarimizni uzunligini topish uchun `len()` funksiyasidan foydalanamiz.
    ```python
    text = "Hello, World!"
    uzunlik = len(text)  # 13
    print(uzunlik)
    ```
    **Natija:** `13`

    ### STRING E'LEMENTLARIGA MUROJAT QILISH
    Matnlarimiz ichidan o'zimizga kerak bo'lgan harflarni ajratib olish uchun quyidagi usuldan foydalanamiz:
    ```python
    text = "Hello world!"
    first_char = text[0] # H
    last_char = text[-1]  # '!'
    substring = text[0:5]  # 'Hello'
    print(first_char)
    print(last_char)
    print(substring)
    ```
    **Natija:** <br>
    `H` <br>
    `!` <br>
    `Hello`

    ### STRINGLARNI KO'PAYTIRISH
    ```python
    text = "Hello"
    text_repeated = text * 3
    print(text_repeated)
    ```
    **Natija:** `HelloHelloHello`

- **Number** - Raqamli ma'lumot turi 2ga bo'linadi:
    - **Integer(int)** - Butun sonlarni ifodalaydi. Masalan: `10`, `-3`, `42`.
    - **Floating Point(float)** - O'nlik sonlarni ifodalaydi. Masalan: `3.14`, `-2.7`,` 0.99`.

- Pythonda `sequence types` (ketma-ketlik) ma'lumot turlari turli xil elementlarni tartiblangan shaklda saqlash uchun ishlatiladi. Asosiy `sequence` turlari quyidagilar:
    - **List(list):** Tartiblangan va o'zgaruvchan ma'lumotlar to'plami. Masalan: `my_list = [1, 'Hello', True, '5.6']`
    - **Tuple(tuple):** Tartiblangan, lekin o'zgarmas ma'lumotlar to'plami. Masalan: `my_tuple = (1, 2, 3, 4, 5)`
    - **Range(range):** `Ketma-ket` sonlar intervalini ifodalaydi. Masalan: `range(1, 11)`
- Pythonda `mapping types` ma'lumot turi `kalit-qiymat` juftlari ko'rinishida ma'lumotlarni saqlash uchun ishlatiladi. Pythonda asosiy mapping ma'lumot turi bu **dictionary(dict)** hisoblanadi. `Dictionary` - kalit (`key`) va qiymat (`value`) juftlaridan tashkil topgan tartibsiz ma'lumotlar to'plami.
- Pythonda `set` - bu unikal elementlar to'plami bo'lib, `tartibsiz` va `indekslanmagan` holda saqlanadi. `Set` ma'lumot turi `duplikat` elementlarni o'z ichiga olmaydi va asosiy foydalanish maqsadi to'plam operatsiyalarini bajarish (`union`, `intersection`, `difference` va boshqalar) hisoblanadi.
    - Pythonda frozenset `o'zgarmas set` ma'lumot turi bo'lib, setning barcha xususiyatlariga ega, lekin elementlari yaratilgandan so'ng o'zgartirilmaydi.
- Pythonda `boolean(bool)` ma'lumot turi ikkita qiymatni ifodalaydi: `True` va `False`. `Boolean` ma'lumot turi mantiqiy ifodalarni baholash va shartli tekshiruvlarni amalga oshirish uchun ishlatiladi. 
- Pythonda `binary` ma'lumot turlari ikkilik (`binary`) ma'lumotlar bilan ishlash uchun ishlatiladi. Asosiy `binary` ma'lumot turlari quyidagilardan iborat:
    - **bytes:** O'zgarmas ikkilik ma'lumotlar to'plami.
    - **bytearray:** O'zgaruvchan ikkilik ma'lumotlar to'plami.
    - **memoryview:** Mavjud ikkilik ma'lumotlarni ko'rish va manipulyatsiya qilish imkonini beradi.