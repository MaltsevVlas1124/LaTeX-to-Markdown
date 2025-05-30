﻿Купейний вагон містить 36 пасажирських місць --- 9 купе по 4 місця у кожному. Половина серед цих місць нижні, решта --- верхні. На рисунку наведено схему розміщення місць 1, 2, 3, 4 у купе №1. Купе №2 містить аналогічно розміщені місця 5, 6, 7, 8, і так далі, до купе №9, яке містить аналогічно розміщені місця 33, 34, 35, 36.

Напишіть програму, яка, прочитавши номери двох різних місць одного купейного вагону, визначатиме:
1.  чи в одному й тому ж купе розміщені ці місця;
2.  верхнє чи нижнє перше з цих місць;
3.  верхнє чи нижнє друге з цих місць.

## Вхідні дані
Два числа ~p_1 \,\, p_2~ у одному рядку, розділені одним пропуском (пробілом). Гарантовано виконуються обмеження ~1 < p_1 < 36~, ~1 < p_2 < 36~, ~p_1 \neq p_2~.

## Вихідні дані
Перший рядок повинен містити або єдине слово `NO` (якщо місця у різних купе), або слово `YES` і після нього через пробіл номер того купе, в якому розміщені обидва ці місця. Другий рядок повинен містити або єдине слово `LOW` (якщо перше з уведених місць нижнє), або єдине слово `HIGH` (якщо верхнє). Третій рядок теж повинен містити або слово `LOW`, або слово `HIGH`, але стосовно другого з уведених місць.

## Приклади

**Вхідні дані:**
```
2 3
```

**Вихідні дані:**
```
YES 1
HIGH
LOW
```

**Вхідні дані:**
```
23 17
```

**Вихідні дані:**
```
NO
LOW
LOW
```

## Примітка
Перевірте правильність написання у Вашій програмі слів `YES`, `NO`, `LOW`, `HIGH` (ВЕЛИКИМИ латинськими літерами). Автоматична перевіряюча система зараховує відповідь, лише коли вона правильна буква-в-букву.