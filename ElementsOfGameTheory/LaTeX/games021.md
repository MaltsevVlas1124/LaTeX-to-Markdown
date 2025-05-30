﻿~N~ карток викладені в ряд зліва направо. На кожній картці написане ціле число. Два гравці по черзі забирають по одній картці, причому забирати можна лише з правого боку, або 1 картку, або 2 картки, або 3 картки (але, звісно, не більше карток, чим їх лишилося). Закінчується гра, коли забрано всі картки (поки картки є, гравець зобов'язаний робити один із можливих ходів). Мета гри --- отримати якомога більшу суму (чисел, записаних на забраних картках).

Яку максимальну суму гарантовано зможе набрати перший гравець?

## Вхідні дані
У першому рядку вказано кількість карток ~N~ (~1 \le N \le 1234567~). У другому рядку через пробіли задані ~N~ цілих чисел (що не перевершують за модулем ~10^3~; інакше кажучи, належать проміжку ~[-1000; +1000]~) --- значення, записані на картках.

## Вихідні дані
Виведіть єдине ціле число --- максимальну суму, яку гарантовано зможе набрати перший гравець.

## Приклади

**Вхідні дані:**
```
7
11 11 11 11 11 11 11
```

**Вихідні дані:**
```
44
```

**Вхідні дані:**
```
8
3 2 999 4 6 7 -5 1
```

**Вихідні дані:**
```
1000
```

**Вхідні дані:**
```
9
23 -17 2 -13 5 3 11 -7 19
```

**Вихідні дані:**
```
30
```

## Примітка
У першому прикладі, всі числа додатні й абсолютно однакові, тому гравцям вигідно забирати якнайбільше штук карток: 1-й забирає три штуки, потім 2-й забирає три штуки, потім 1-й забирає останню і цим завершує гру з сумою ~(11+11+11)+(11)=44~.

У др*у*гому прикладі, значення 999 сильно перевищує всю решту, тому 1-му гравцю вигідно дбати в першу чергу про те, щоб це найбільше число дісталося саме йому.
І перший хід «взяти дві картки 1 та –5» це забезпечує: як би на нього не відповів 2-й (чи забере лише 7, чи дві картки 7 і 6, чи три картки 7, 6 і 4), все'дно на наступному ході 1-й гравець зможе взяти собі зокрема й картку 999. А інші можливі перші ходи 1-го гравця не гарантують йому взяття картки 999: якщо забрати на першому ході три картки, 2-й гравець зможе забрати 999 собі наступним же ходом; якщо забрати на першому ході одну картку, 2-й гравець у відповідь може взяти собі лише одну картку, тобто (згідно з уже наведеними міркуваннями) забезпечити, що картка 999 дістанеться йому. Звісно, для остат*о*чної відповіді потрібно не лише забрати картку 999, а й отримати точне значення суми; це ~(1+(-5))+(999+2+3)=1000~, що досягається при такому сценарії гри: 1-й забирає 1 та (-5); 2-й забирає 7, 6 та 4 (це найкраще, що йому лишається після того, як його позбавили надії взяти 999); 1-й забирає 999, 2 і 3.

Зверніть увагу: щойно розглянутий приклад містить дуже контрінтуїтивний, на перший абсолютно погляд неприродний перший хід: треба взяти від'ємне значення –5 (хоча його можна й не брати), і не взяти після цього додатне значення 7 (хоч його й можна взяти разом з 1 і –5). Однак, усе це нівелюється тим, що с*а*ме 1-й гравець може гарантувати, що потім візьме 999.

Очевидно, що при «середніх» значеннях (і різних, і нема яскраво вираженого найбільшого) вищезгадані підходи не працюють, а працює лише специфічне застосування динамічного програмування. Можливість від'ємних значень на картках додатково зменшує ймовірність правильності простих-але-не-завжди-правильних евристик, не заважаючи при цьому динамічному програмуванню.

У третьому прикладі, 30 досягається так:
1-й гравець забирає одну картку 19;
2-й гравець забирає три картки –7, 11, 3;
1-й гравець забирає одну картку 5;
2-й гравець забирає дві картки –13, 2;
1-й гравець забирає дві картки –17, 23, на чому гра закінчується;
~(19)+(5)+(-17+23)=30~.