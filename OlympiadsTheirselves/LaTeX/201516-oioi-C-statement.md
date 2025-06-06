﻿# Нестандартне рівняння

Напишіть програму, яка шукатиме (шляхом перебору) кількість розв'язків на проміжку ~[a; b]~ рівняння ~k \times f(n) = n~, де ~f(n)~ — сума квадратів цифр&nbsp;у&nbsp;десятковому записі числа́ ~n~.

## Вхідні дані
Єдиний рядок містить три розділених пробілами цілі чи́сла,&nbsp;у&nbsp;порядку `k a b`. Гарантовано ~a < b~, а&nbsp;також,&nbsp;що&nbsp;усі ці чи́сла не&nbsp;менші 1&nbsp;й&nbsp;не&nbsp;більші ~10^{18}~.

## Вихідні дані
Програма повинна вивести єдине число — кількість таких ~n~&nbsp;з&nbsp;проміжку ~a \le n \le b~,&nbsp;що&nbsp;задовольняють рівняння.

## Приклади

**Вхідні дані:**
```
51 5000 10000
```

**Вихідні дані:**
```
3
```

## Примітки
Цими трьома розв'язками є 7293, 7854 та 7905.
Наприклад, 7293 є розв'язком,&nbsp;бо&nbsp;~51 \times (7^2+2^2+9^2+3^2) = 51 \times (49+4+81+9) = 51 \times 143 = 7293~.

Але нічого цього виводити не&nbsp;треба, треба лише кількість розв'язків.