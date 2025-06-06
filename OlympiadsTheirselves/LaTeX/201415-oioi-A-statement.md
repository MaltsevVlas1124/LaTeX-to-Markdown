﻿# Три круги

Є три круги радіусами ~R_1~, ~R_2~ та ~R_3~.
Чи можна перекласти їх так, щоб відразу два менші круги лежали один поруч з іншим на найбільшому, не накладаючись один на одного і не звисаючи за його межі? Торкатися один одного менші круги можуть.

## Вхідні дані
Програма повинна прочитати три цілі числа ~R_1~, ~R_2~ та ~R_3~, в один рядок, через пропуски (пробіли). Усі три значення ~R_1~, ~R_2~ та ~R_3~ є цілими числами в межах від 1 до 1000.

## Вихідні дані
Якщо перекласти круги вказаним чином неможливо, програма повинна вивести єдине слово `NO` (без лапок).
Якщо можливо, то в єдиному рядку повинно бути записано `YES, the  ...  disk is the maximal`, де замість `...` повинно бути одне з трьох значень:
- `1st`, якщо 2-й і 3-й круги можна покласти поверх 1-го;
- `2nd`, якщо 1-й і 3-й круги можна покласти поверх 2-го;
- `3rd`, якщо 1-й і 2-й круги можна покласти поверх 3-го.
Зверніть увагу: фраза повинна бути однаковою з правильною байт-у-байт, тобто всі великі чи маленькі літери, всі пропуски (пробіли) та інші подібні дрібниці важливі.

## Приклади
**Вхідні дані:**
```
1 2 3
```

**Вихідні дані:**
```
YES, the 3rd disk is the maximal
```

**Вхідні дані:**
```
2 3 4
```

**Вихідні дані:**
```
NO
```

**Вхідні дані:**
```
9 3 1
```

**Вихідні дані:**
```
YES, the 1st disk is the maximal
```
