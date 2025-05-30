﻿# Розбір

Якщо обчислити кілька перших трійок (~1 + 2 - 3 = 0~; ~4 + 5 - 6 = 3~; ~7 + 8 - 9 = 6~; ~10 + 11 - 12 = 9~; ~\dots~), можна помітити, що результати таких трійок дорівнюють 0, 3, 6, 9, ~\dots~, утворюючи тим самим арифметичну прогресію.

Таким чином, якщо порахувати кількість трійок через вираз `k:=n div 3` (Pascal), він же `k = n//3` (Python3), ~\dots~ (в разі потреби допишіть своєю мовою програмування самостійно), то суму всіх трійок можна порахувати через формулу ~\frac{0+3(k-1)}{2} \cdot k~.

Само собою, введене ~n~ може бути й не кратним 3, тобто можуть лишитися один чи два останні доданки, які не входять ні в яку трійку; їх можна додати до результату окремими `if`-ами.

**А без цих прогресій можна?** Якщо Вас влаштовує 70% балів, то можна просто порахувати в циклі суму всіх підряд натуральних чисел від 1 до ~n~, але доданки, кратні 3, не додавати, а віднімати (включивши `if` всередину `for`-а).

Само собою, можна прийти до правильного результату і ще якось. Можна, наприклад, не пам'ятаючи формулу суми арифметичної прогресії, вивести самостійно якийсь її аналог, враховуючи якісь особливості конкретно цієї задачі. Ніхто не перевіряє, чи знаєте Ви, що це називається арифметичною прогресією, та чи пам'ятаєте стандартну формулу. Зумієте замінити чимось іншим, що теж вкладеться в обмеження часу --- ну то й добре.

**А згорнути зовсім в один вираз, щоб обчислювати і без циклів, і без `if`-ів, можна?** В принципі, можна. Якби сума була не знакозмінною, а просто ~1+2+3+4+5+6+\ldots+n~, її можна було б перетворити (наприклад, за все тією ж формулою суми арифметичної прогресії) до ~\frac{n\cdot(n+1)}{2}~. Чим потрібна знакозмінна сума відрізняється від цієї? Тим, що доданки, кратні 3, віднімаються, а не додаються\dots{} але це саме можна сформулювати інакше: тим, що із ~\frac{n\cdot(n+1)}{2}~ треба двічі відняти ~3+6+9+\ldots+3k~ (де ~k~, як і кілька абзаців тому, має смисл ~n \text{ div } 3~, а віднімати двічі треба тому, що якщо просто відняти, то вийшла б сума ~1+2+4+5+7+8+10+\ldots~, тобто доданки, кратні 3, просто «щезли» б, а треба, щоб вони не «щезли», а стали від'ємними). Легко бачити, що ~3+6+9+\ldots+3k = 3\cdot(1+2+3+\ldots+k) =~ ~3\cdot\frac{k\cdot(k+1)}{2}~, а раз цю суму треба відняти двічі, маємо
$$ \text{остаточний результат} = \frac{n\cdot(n+1)}{2} - 3\cdot k\cdot(k+1), \quad \text{де } k=n \text{ div } 3. $$

Також, для отримання повних балів важливо рахувати суму, щонайменше, в 64-бітовому цілочисельному типі, бо в менших (хоч 32-бітовому цілочисельному, хоч з рухомою комою (плаваючою точкою), як-то `double`) не вистачає розрядів (відбувається переповнення (див. також про переповнення) чи похибка (див. також про похибки з рухомою комою), що призводить до неправильної відповіді (наскільки сильно не вистачає і наскільки неповні бали, може залежати від конкретної мови програмування та конкретних типів). Рахувати у ще більших типах (наприклад, `BigInteger` мови Java) теж можна.