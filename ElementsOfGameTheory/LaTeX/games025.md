﻿Є&nbsp;одна купка, яка спочатку містить ~N~&nbsp;паличок.
Двоє грають у&nbsp;таку гру.
Кожен з&nbsp;гравців на кожному своєму ході може забрати з&nbsp;купки деяку кількість паличок (звісно, не&nbsp;більше, чим їх є в&nbsp;купці), **причому кількості паличок, які можна забирати, для різних суперників різні: 1-й гравець може забирати або&nbsp;4, або&nbsp;8, або&nbsp;16, або&nbsp;32&nbsp;палички, тоді як 2-й&nbsp;— або&nbsp;2, або&nbsp;7, або&nbsp;14**.
Ніяких інших варіантів ходу нема.
Ходять гравці по&nbsp;черзі, пропускати хід не&nbsp;можна.
Програє́ той, хто не&nbsp;може походити. Зверніть увагу: оскільки в&nbsp;цій задачі гравці не&nbsp;можуть забирати 1&nbsp;паличку, можливі також&nbsp;і&nbsp;ситуації, коли палички ще&nbsp;є, а&nbsp;походити вже не&nbsp;можна. Точніше кажучи, 1-й вже не&nbsp;може ходити не&nbsp;лише коли йому не&nbsp;лишили паличок, але також&nbsp;і&nbsp;коли лишили 1&nbsp;паличку, 2&nbsp;або&nbsp;3&nbsp;палички; 2-й вже не&nbsp;може ходити не&nbsp;лише коли йому не&nbsp;лишили паличок, але також&nbsp;і&nbsp;коли лишили 1&nbsp;паличку.

## Вхідні дані
Єдине ціле число ~N~ (~1 \le N \le 12345~)&nbsp;— початкова кількість паличок у&nbsp;купці.

## Вихідні дані
Перший рядок має містити єдине ціле число, або&nbsp;`1` (якщо перший гравець може забезпечити собі виграш), або&nbsp;`2` (якщо *другий*).
Якщо відповідь з першого рядка `2`, то&nbsp;на&nbsp;цьому виведення слід припинити. А&nbsp;якщо відповідь з першого рядка `1`, то&nbsp;далі треба вивести також перелік всіх можливих перших ходів першого гравця, після яких *другий* (при правильній грі першого) вже *ніяк* не&nbsp;зможе виграти. Цей перелік виводити&nbsp;в такому форматі: вибрати лише потрібні *числа* з&nbsp;переліку допустимих ходів 4, 8, 16, 32, і&nbsp;записати&nbsp;в другому рядку всі вибрані («виграшні»)&nbsp;в порядку зростання через пробіли. Кількість «виграшних ходів» виводити не&nbsp;треба&nbsp;і&nbsp;не&nbsp;можна.

## Приклади

**Вхідні дані:**
```
7
```

**Вихідні дані:**
```
2
```

**Вхідні дані:**
```
10
```

**Вихідні дані:**
```
1
4
```

## Примітка
У&nbsp;першому тесті, 1-й гравець фактично може забрати лише 4&nbsp;палички; після цього, у&nbsp;2-го теж нема ви́бору (може лише забрати 2&nbsp;палички), але 2-й походити ще&nbsp;зміг, а&nbsp;1-й, якому лишається 1&nbsp;паличка, більше не&nbsp;ма́є ходів&nbsp;і&nbsp;програє́.

У&nbsp;другому тесті, у&nbsp;1-го гравця на&nbsp;першому ході фактично є&nbsp;ви́бір «забирати 4&nbsp;чи&nbsp;забирати 8», причому якщо&nbsp;він забере 8, то&nbsp;2-й забере 2&nbsp;палички&nbsp;і&nbsp;тим *виграє*, бо&nbsp;1-му гравцю нема паличок&nbsp;і&nbsp;тому нема ходів. (Отже, 1-му гравцю не&nbsp;ва́рто забирати 8&nbsp;на&nbsp;своєму першому ході.) А&nbsp;от якщо&nbsp;1-й гравець на&nbsp;першому ході здогадається забрати 4&nbsp;палички (залишиться 6), то&nbsp;у&nbsp;2-го нема ви́бору (може лише забрати 2&nbsp;палички, лишається 4), після&nbsp;чого 1-й гравець може забрати 4&nbsp;палички&nbsp;і&nbsp;тим виграє́, бо&nbsp;2-му гравцю нема паличок&nbsp;і&nbsp;тому нема ходів.