# Ко-анаграмічно-прості

Число називається *простим*, якщо воно має рівно два різні дільники --- себе і одиницю. Наприклад: 23 --- просте число, а 35 не просте, бо ~5*7=35~. Число 1 теж не просте (лише один дільник).

Якщо у числі змінити порядок цифр, властивість простоти може змінитися: наприклад, 35 --- не просте число, а 53 --- просте.

Будемо називати число *ко-анаграмічно-простим*, коли при хоча б одному можливому порядку цифр утворюється просте число. Наприклад, 35 є ко-анаграмічно-простим (бо 53 просте), а 225 --- не є, бо жодне з чисел 225, 252 та 522 не є простим.

Напишіть програму, яка читає одне ціле додатне значення ~n~ (~10 < n < 9999~) і виводить у першому рядку мінімальне можливе ко-анаграмічно-просте число, більше-рівне за ~n~, а у другому рядку --- ту перестановку цифр, яка робить його простим. Якщо при перестановці з’являються нулі спереду числа --- слід вважати, що вони не впливають на значення числа (05 дорівнює 5), але виводити слід обов’язково із цими нулями (якщо правильно 05, то вивести 5 неправильно). Разом з тим, перше число відповіді починати з нуля не можна.

Якщо можливі різні правильні відповіді --- виводьте будь-яку одну з них.

## Приклади

**Вхідні дані:**
```
35
```

**Вихідні дані:**
```
35
53
```

**Вхідні дані:**
```
49
```

**Вихідні дані:**
```
50
05
```

**Вхідні дані:**
```
225
```

**Вихідні дані:**
```
227
227
```﻿
