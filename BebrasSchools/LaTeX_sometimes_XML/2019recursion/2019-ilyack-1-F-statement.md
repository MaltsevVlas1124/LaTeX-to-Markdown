﻿# Сума кубів

Напишіть програму, що читатиме натуральне число ~N~ й подаватиме його у вигляді мінімальної кількості точних натуральних кубів. Інакше кажучи, програма повинна знайти такі натуральні ~m_1~, ~m_2~, ~\dots~, ~m_k~, що
~m_1^3 + m_2^3 + ... + m_k^3 = N~, а ~k~ при цьому якнайменше можливе.

## Приклади

**Вхідні дані:**
```
42
```

**Вихідні дані:**
```
7
2 2 2 2 2 1 1
```

**Вхідні дані:**
```
43
```

**Вихідні дані:**
```
3
3 2 2
```

## Вхідні дані
Єдиний рядок вхідних даних містить єдине число ~N~ (~1 \leqslant N \leqslant 44\,777\,444~).

## Вихідні дані
Слід вивести рівно два рядки. Перший має містити ~k~ - знайдену мінімальну кількість натуральних кубів. Другий рядок повинен містити такі ~k~ натуральних чисел, що сума їхніх кубів дорівнює ~N~.