# Коло і точки

Коло і точки

Є одне коло та ~N~ точок.

Напишіть програму, яка знаходитиме, скільки з цих ~N~ точок потрапили всередину цього кола, скільки на саме коло і скільки ззовні кола.

## Вхідні дані
Перші два рядки вхідних даних задають коло. Можуть бути два різні формати його задання:
1.  Якщо 1-ий рядок містить єдине число 1, то 2-ий рядок містить рівно три цілі числа ~x_C~, ~y_C~, ~R_C~ --- координати центра кола та його радіус.
2.  Якщо 1-ий рядок містить єдине число 2, то 2-ий рядок містить рівно шість цілих чисел ~x_A~, ~y_A~, ~x_B~, ~y_B~, ~x_C~, ~y_C~. Їх слід трактувати як координати трьох точок ~A~, ~B~, ~C~, через які проведене коло, котре треба дослідити. Ці три точки гарантовано всі різні і гарантовано не лежать на одній прямій. Гарантовано також, що ніяка з цих трьох точок не збігається ні з одною з точок подальшого переліку з ~N~ точок.

Третій рядок вхідних даних завжди містить єдине ціле число ~N~ --- кількість точок. Подальші ~N~ рядків містять по два цілі числа кожен --- ~x~ та ~y~ координати самих точок.

Абсолютно всі задані у вхідних даних числа є цілими і не перевищують за абсолютною величиною (модулем) 1000. При цьому кількість точок і радіус гарантовано додатні, а координати можуть бути довільного знаку.

Скрізь, де в одному й тому ж рядку записано по кілька чисел, вони відділені одне від одного пропусками (пробілами).

## Вихідні дані
Програма повинна вивести три цілі числа --- спочатку кількість точок всередині кола, потім кількість точок на самому колі, потім кількість точок ззовні кола.

Сума цих трьох чисел повинна дорівнювати ~N~. Зокрема, якщо коло задане 2-им способом, то ті три точки, якими воно задане, треба не вважати точками, належними колу.

## Приклади
**Вхідні дані:**
```
1
-1 2 5
4
0 0
-3 -3
-6 2
6 -2
```

**Вихідні дані:**
```
1 1 2
```

**Вхідні дані:**
```
2
-1 -3 2 6 3 5
4
0 0
-3 -3
-6 2
6 -2
```

**Вихідні дані:**
```
1 1 2
```

## Примітки
В обох наведених прикладах задане (різними способами) одне й те само коло, тому що коло, проведене через точки ~(-1; -3)~, ~(2; 6)~ та ~(3; 5)~ якраз і має радіус 5 та центр у точці ~(-1; 2)~.

Перша одиничка відповіді виражає, що лише одна точка з переліку потрапила всередину кола (і це точка ~(0; 0)~, але цього не питають). Друга одиничка відповіді виражає, що лише одна точка з переліку потрапила на саме коло (і це точка ~(-6; 2)~, але цього не питають). Число 2 у відповіді позначає, що решта дві точки переліку (це точки ~(-3; -3)~ та ~(6; -2)~, але цього не питають) потрапили ззовні кола.

Можна здавати програму, яка враховує лише подання кола через координати центра і радіус. На тести, в яких коло подається 1-им способом, припадатиме майже половина балів, і така програма може їх отримати. Але навіть така програма повинна враховувати, що в цих тестах все одно буде 1-ий рядок з єдиним числом 1.

Разом з тим, якщо враховувати обидва випадки, це все одно повинна бути одна програма.﻿
