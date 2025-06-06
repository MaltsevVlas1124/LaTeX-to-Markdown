# Сума квадратів

Для заданого натурального число́ ~N~, визначити, скількома різними способами можна розкласти його&nbsp;в&nbsp;суму двох точних додатних квадратів.

Іншими словами: для заданого ~N~, з’ясувати, скільки є&nbsp;різних способів подати його&nbsp;як&nbsp;~N = x^2 + y^2~, причому ~x~&nbsp;та&nbsp;~y~&nbsp;являють собою цілі строго додатні чи́сла, а&nbsp;розкладення, в&nbsp;яких значення ~x~&nbsp;та&nbsp;~y~&nbsp;лише обміняні місцями, вважаються однаковими.

## Вхідні дані
Вхідні дані&nbsp;— натуральне число́ ~N~&nbsp;— слід прочитати зі&nbsp;стандартного входу (клавіатури).

## Вихідні дані
Результат&nbsp;— знайдену кількість способів&nbsp;— слід вивести на&nbsp;стандартний вихід (екран).

## Приклади

**Вхідні дані:**
```
16
```

**Вихідні дані:**
```
0
```
Розкласти у&nbsp;суму додатних точних квадратів неможливо

**Вхідні дані:**
```
10
```

**Вихідні дані:**
```
1
```
Єдине розкладення ~10 = 1^2 + 3^2~

**Вхідні дані:**
```
4225
```

**Вихідні дані:**
```
4
```
Чотири різні розкладення: ~4225 = 16^2 + 63^2 = 25^2 + 60^2 = 33^2 + 56^2 = 39^2 + 52^2~

## Примітка
100&nbsp;балів (з&nbsp;250) припадатиме на&nbsp;тести, в&nbsp;яких ~1 < N < 1234~.

Ще&nbsp;50&nbsp;балів&nbsp;— на&nbsp;тести, в&nbsp;яких ~12345 < N < 123456~.

Решта 100&nbsp;балів&nbsp;— на&nbsp;тести, в&nbsp;яких ~12345678 < N < 123456789~.

Здати потрібно одну програму, а&nbsp;не&nbsp;окремі для&nbsp;трьох випадків; різні обмеження вводяться виключно для&nbsp;того, щоб&nbsp;дати приблизне уявлення, скільки&nbsp;балів можна&nbsp;отримати, розв’язавши задачу&nbsp;не&nbsp;повністю.
