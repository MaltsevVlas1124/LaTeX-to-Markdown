﻿~N~ карток викладені в ряд зліва направо. На кожній картці написане ціле число. Два гравці по черзі забирають картки, причому забирати можна лише з правого боку, або 1 картку, або 2 картки, або 3 картки (але, звісно, не більше карток, чим їх є). Закінчується гра, коли забрано всі картки (поки хоч одна картка є, гравець зобов'язаний робити один із можливих ходів).
Крім того, після кожного ходу кожного з гравців з імовірністю 10% стається (отже, з імовірністю 90% не стається) випадкове віднесення вітром картки, яка щойно стала крайньою правою.
(Це *найголовніша* відмінність цієї задачі від задачі «Гра на максимум суми (1/2/3)».)
Мета гри --- отримати якнайбільшу суму (чисел, записаних на забраних картках).

Які матсподівання сум, що їх наберуть гравці, якщо обидва гратимуть якнайкраще, намагаючись максимізувати кожен своє матсподівання?

## Вхідні дані
У першому рядку вказано кількість карток ~N~ (~1 \le N \le 1234~). У другому рядку через пробіли задані ~N~ цілих чисел (що не перевищують за модулем ~10^3~; інакше кажучи, з проміжку ~[-1000; +1000]~) --- значення, записані на картках.

## Вихідні дані
Виведіть в одному рядку через пропуск два дійсні числа --- матсподівання сум, що наберуть гравці (спочатку 1-й, потім 2-й).
Формат виведення може бути будь-яким зі стандартних (зокрема, байдуже, чи вивести `` 41.91 ``, чи `` 41.910000000 ``, чи `` 4.191e+1 ``), важливо лише забезпечити точність, вказану в «Оцінюванні».

## Приклади

**Вхідні дані:**
```
7
11 11 11 11 11 11 11
```

**Вихідні дані:**
```
41.91 33
```

**Вхідні дані:**
```
8
3 2 999 4 6 7 -5 1
```

**Вихідні дані:**
```
810.17 116.2
```

**Вхідні дані:**
```
9
23 -17 2 -13 5 3 11 -7 19
```

**Вихідні дані:**
```
26.7633 2.215
```

## Примітки
У першому тесті, числа додатні й однакові, тому гравцям вигідно забирати якнайбільше карток:
спочатку 1-й забирає три штуки;
потім вітер чи то відносить одну картку, чи то ні, й карток лишається чи то три штуки, чи то чотири;
в будь-якому разі, 2-й забирає три штуки;
залежно від вітру, повторний хід 1-го гравця може бути, а може й не бути: він буде з ймовірністю ~0,9 \cdot 0,9 = 0,81~,
якщо вітер не віднесе картки ні після ходу 1-го гравця, ні після ходу 2-го; в цьому разі, лишиться одна картка, яку вигідно забрати. Тобто, 1-й з імовірністю 81% набере ~33+11=44~, а з імовірністю ~100% - 81% = 19%~ набере 33; матсподівання дорівнює ~0,81 \cdot 44 + 0,19 \cdot 33 = 35,64 + 6,27 = 41,91~.
Для цих вхідних даних, вітер не може завадити 2-му гравцеві взяти три картки по 11 кожна, й результат 2-го завжди ~11+11+11 = 33~.
(Від вітру залежить, *які* це будуть три картки; але на кожній з них однакове 11, тому на результат не впливає.)

У другому прикладі, як і в задачі «Гра на максимум суми (1/2/3)» значення 999 усе ще настільки перевищує всю решту, що все ще варто дбати в першу чергу про те, щоб узяти це найбільше число.
Через те, що тепер є випадкові впливи вітру, перший хід *«узяти дві картки 1 та (–5)»* вже не гарантує цього, але все ще дає найбільшу ймовірність ~0,9 \cdot 0,9 = 0,81~,
якщо вітер не віднесе картки ні після ходу 1-го гравця, ні після ходу 2-го.

Як від ще детальніших пояснень відповіді другого тесту, так і від будь-яких коментарів щодо третього тесту утримаюся.

## Оцінювання
Потестове (кожен тест перевіряють і оцінюють незалежно від решти).
Тест зараховують, коли абсолютна або відносна похибка (хоча б одна з двох) не перевищує ~10^{-9}~.