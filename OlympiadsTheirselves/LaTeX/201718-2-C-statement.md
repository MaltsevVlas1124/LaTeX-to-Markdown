﻿# Цікаві числа

Напишіть програму, яка знаходитиме кількість «*цікавих*» чисел, менших за задане число ~N~. Число називається «*цікавим*», якщо в ньому використовуються лише цифри 1, 2, 4 та 8 (не обов'язково усі; обов'язково, щоб не було інших).
Наприклад числа 12, 18, 8, 284 є цікавими, а числа 246, 143, 3, 487 --- ні.

## Вхідні дані
В єдиному рядку задано єдине число ~N~ (обмеження див. у розділі «Оцінювання»).

## Вихідні дані
Виведіть єдине число в єдиному рядку --- кількість «*цікавих*» чисел, менших ~N~.

## Приклади

**Вхідні дані:**
```
18
```

**Вихідні дані:**
```
7
```


**Примітки:**
Цими сімома числами є: 1, 2, 4, 8, 11, 12, 14.

## Оцінювання

20% балів припадає на тести, де ~N = 10^T~, ~1 \leqslant T \leqslant 18~. Ще ~\geqslant~ 20% на тести, де ~1 \leqslant N \leqslant 10^5~. Ще ~\geqslant~ 40% на тести, де ~10^6 < N \leqslant 10^{12}~. Ще ~\geqslant~ 20% на тести, де ~10^{12} < N \leqslant 10^{18}~.

Писати треба одну програму, а не різні програми для різних випадків; єдина мета цього переліку різних блоків обмежень --- дати уявлення про те, скільки балів можна отримати, якщо розв’язати задачу частково.