Розглянемо узагальнення біматричної гри на&nbsp;трьох гравців: щодо кожного з&nbsp;трьох гравців задано, які стратегії йому доступні, і&nbsp;для кожного гравця є свій тривимірний масив: елемент `a[i][j][k]` масиву `a` виражає виграш першого гравця за&nbsp;умови,&nbsp;що перший гравець вибрав стратегію номер `i`, дру́гий гравець стратегію номер `j`, третій гравець стратегію номер `k`; елемент `b[i][j][k]` масиву `b` виражає виграш дру́гого гравця за тих самих умов, а елемент `c[i][j][k]` масиву `c` — виграш третього. (Всього є три тривимірні масиви однакових розмірів, аналогічно тому, як&nbsp;у класичних біматричних іграх є дві матриці однакових розмірів.)

Напишіть програму, яка за вказаними тривимірними масивами виграшів визначить, в&nbsp;яких парах стратегій кожного з&nbsp;гравців одна домінує іншу.

##Вхідні дані

У&nbsp;першому рядку через пропуски (пробіли) задано кількість стратегій першого гравця ~N~ (~2 \le N \le 8~), кількість стратегій другого гравця ~M~ (~2 \le M \le 8~) та&nbsp;кількість стратегій третього гравця ~K~ (~2 \le K \le 8~). Далі йде один порожній рядок. Наступні ~M*K + (M—1)~ рядків містять масив виграшів першого гравця, у&nbsp;вигляді: спочатку по&nbsp;рівно ~M~ рядків по&nbsp;рівно ~K~ чисел, розділених одинарними пропусками (пробілами), причому *j*-е число *i*-го рядка являє собою виграш першого гравця у випадку, якщо перший гравець застосує стратегію №1, другий стратегію №*i*, а третій стратегію №*j*. Далі йде один порожній рядок, після якого задані ще рівно ~M~ рядків по&nbsp;рівно ~K~ чисел, розділених одинарними пропусками (пробілами), де *j*-е число *i*-го рядка являє собою виграш першого гравця у випадку, якщо перший гравець застосує стратегію №2, другий стратегію №*i*, а третій стратегію №*j*; і так далі. Після вичерпання всіх ~M*K + (M—1)~ рядків (з&nbsp;яких ~M*K~ непорожніх та ~M—1~ порожніх) слідують три підряд порожні рядки, а після них в аналогічному форматі задано тривимірний масив виграшів другого гравця. Потім слідують ще три підряд порожні рядки, а після них в аналогічному форматі задано тривимірний масив виграшів третього гравця. Всі значення елементів усіх масивів є цілими числами,&nbsp;що&nbsp;не перевищують за&nbsp;модулем (абсолютною величиною) 999.

##Вихідні дані
Ваша програма повинна вивести спочатку в&nbsp;окремому рядку фразу `1st player`, потім всі можливі пари стратегій ~i, j~ (при ~i != j~) першого гравця, де *i*-а стратегія домінує *j*-у стратегію. Якщо домінування строге, то фраза в&nbsp;окремому рядку повинна мати вигляд "`i strictly dominates j`"; якщо строгого домінування нема, але є слабке домінування, то фраза в&nbsp;окремому рядку повинна мати вигляд "`i weakly dominates j`". Виводити слід без лапок, а замість "~i~" та "~j~" треба виводити конкретні чи́сла-номери стратегій (вважаючи,&nbsp;що&nbsp;нумерація починається з&nbsp;1). Всі ці фрази повинні бути відсортовані за&nbsp;зростанням ~i~, а при однакових ~i~ — за&nbsp;зростанням ~j~.

Потім слід вивести в&nbsp;окремому рядку фразу `2nd player`, а після неї — аналогічні, в&nbsp;такому ж форматі, результати порівнянь стратегій другого гравця.

Потім слід вивести в&nbsp;окремому рядку фразу `3rd player`, а після неї — аналогічні, в&nbsp;такому ж форматі, результати порівнянь стратегій третього гравця.

## Приклади:

**Вхідні дані:**
```
2 2 2
2 2
3 3
1 0
1 2
1 3
1 3
0 2
0 2
0 3
0 1
2 0
0 0
```

**Вихідні дані:**
```
1st player
1 strictly dominates 2
2nd player
1 weakly dominates 2
2 weakly dominates 1
3rd player
```

##Примітка
Якщо 1-ий гравець вибирає свою 1-шу стратегію, то:&nbsp;в&nbsp;разі вибору 1-ої стратегії 2-им гравцем і&nbsp;1-ої стратегії 3-им гравцем 1-ий отримує ~2~ (замість ~1~, якби вибрав 2-гу стратегію);&nbsp;в&nbsp;разі вибору 1-ої стратегії 2-им гравцем і&nbsp;2-ої стратегії 3-им гравцем 1-ий отримує ~2~ (замість ~0~, якби вибрав 2-гу стратегію);&nbsp;в&nbsp;разі вибору 2-ої стратегії 2-им гравцем і&nbsp;1-ої стратегії 3-им гравцем 1-ий отримує ~3~ (замість ~1~, якби вибрав 2-гу стратегію);&nbsp;в&nbsp;разі вибору 2-ої стратегії 2-им гравцем і&nbsp;2-ої стратегії 3-им гравцем 1-ий отримує ~3~ (замість ~2~, якби вибрав 2-гу стратегію). Таким чином, 1-ша стратегія строго домінує 2-гу.

Другому гравцеві зміна стратегії ніколи не змінює величину виграшу:&nbsp;в&nbsp;разі вибору 1-ої стратегії 1-им гравцем і&nbsp;1-ої стратегії 3-ім гравцем, 2-ий незалежно від свого вибору отримує ~1~;&nbsp;в&nbsp;разі вибору 1-ої стратегії 1-им гравцем і&nbsp;2-ої стратегії 3-ім гравцем, 2-ий незалежно від свого вибору отримує ~3~;&nbsp;в&nbsp;разі вибору 1-ої стратегії 1-им гравцем і&nbsp;1-ої стратегії 3-ім гравцем, 2-ий незалежно від свого вибору отримує ~0~;&nbsp;в&nbsp;разі вибору 2-ої стратегії 1-им гравцем і&nbsp;1-ої стратегії 3-ім гравцем, 2-ий незалежно від свого вибору отримує ~0~;&nbsp;в&nbsp;разі вибору 2-ої стратегії 1-им гравцем і&nbsp;2-ої стратегії 3-ім гравцем, 2-ий незалежно від свого вибору отримує ~2~. Таким чином, формально виходить взаємне слабке домінування стратегій одна одною, хоча водночас це більш схоже на&nbsp;рівність (рівноцінність).

Для&nbsp;3-го гравця, ніяка стратегія не домінує іншу ні строго,&nbsp;ні слабко, бо,&nbsp;наприклад,&nbsp;в&nbsp;разі вибору 1-ої стратегії 1-им гравцем і&nbsp;1-ої стратегії 2-им гравцем, 3-му вигідніше вибрати свою 2-гу стратегію&nbsp;й&nbsp;отримати ~3~, ніж вибрати свою 1-шу стратегію&nbsp;й&nbsp;отримати ~0~; але, водночас, в&nbsp;разі вибору 2-ої стратегії 1-им гравцем і&nbsp;1-ої стратегії 2-им гравцем, 3-му вигідніше вибрати свою 1-шу стратегію&nbsp;й&nbsp;отримати ~2~, ніж вибрати свою 2-гу стратегію&nbsp;й&nbsp;отримати ~0~. Тобто, в&nbsp;одних ситуаціях строго більший виграш дає одна стратегія, а&nbsp;в&nbsp;інших — інша.
