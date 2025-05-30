﻿### Знаходження 1-ї відповіді.
З "при сповзанні кубики ніколи не летять, перекидаючись" *випливає*, що вони лише зміщуються на правіші позиції, тобто ніякий кубик не міняє своєї висоти. Кубикам, що лежать на дні, сповзати нема куди (з ~1 < a_j~ слідує, що увесь нижній ряд зайнятий). Будь-який інший кубик на початку лежав на нижчому, а не висів у повітрі; от і при нахилі він або сповзає разом із нижчим, на якому лежить, або, якщо той нижчий впирається у правого сусіда, а сам поточний ні, то поточний зсувається праворуч, на нового нижчого, теж не змінюючи своєї висоти. (Ситуація, що поточний впирається у правого сусіда, а нижчий ні, неможлива, бо для цього треба, щоб кубик праворуч до того вже висів у повітрі, що неможливо.)

Звідси, для простого часткового випадку, коли стовпчиків лише два і ~a_1 > a_2~ (на початку 1-й стовпчик був вищим за 2-й), верхні ~a_1 - a_2~ кубиків сповзають з 1-го на 2-й, після чого вже 1-й стовпчик виявляється нижчим (*тієї ж* висоти ~a_2~, якої раніше був 2-й), а 2-й вищим (висоти ~a_1~). Якщо ж на початку ~a_1 < a_2~, взагалі нічого не змінюється. В обох випадках, *перший рядок відповіді являє собою відсортовану послідовність висот зі вхідних даних*.

Якщо стовпчиків не два, а більше, то все одно кубики або не рухаються відносно дна, або зсуваються послідовно на наразі сусідній стовпчик (можливо, багатократно, але кожен з цих багатьох разів --- на сусідній), і завжди призводить до того, що в кожній парі сусідніх стовпчиків висоти чи то лишаються які були, чи то обмінюються місцями (більша йде праворуч, менша ліворуч). Так що всі сповзання разом узяті, хоч і можуть відбуватися в іншому порядку, ніж сортування, в результаті дають відсортовану послідовність висот.

Отже, 1-й рядок відповіді зручно отримати, не моделюючи весь процес сповзань, а застосувавши ефективний алгоритм сортування (див. далі).

### Знаходження 2-ї відповіді.
Щоб не плутати вже відсортовану (для 1-ї відповіді) послідовність висот із початковою, будемо в цьому тексті називати відсортовану послідовність ~h_1~, ~h_2~, ..., ~h_N~ (хоча технічно це той самий масив у різні моменти часу).
Усі рядки з №1 по №~h_1~ заповнені повністю (бо ~h_1~ --- *мімінальна* з усіх висот), тобто можна вивести у 2-й рядок відповіді ~h_1~ штук значень ~N~ (де ~N~ --- загальна кількість стовпчиків). Потім ~h_2 - h_1~ рядків містять ~N - 1~ кубиків, причому це так і при ~h_2 > h_1~ (тоді у кожному з рядків від №~(h_1 + 1)~ до №~h_2~ включно після зсувів рівно один крайній лівий стовпчик вільний, а решта зайняті, бо рівно один крайній лівий стовпчик має строго меншу висоту, а решта більшу-або-рівну), і при ~h_2 = h_1~ (тоді у відповідь не потрапляє жодне значення ~N - 1~, і це теж правильно, бо тоді на всіх висотах по ~h_1~ включно по ~N~ кубиків, а починаючи з висоти ~h_1 + 1~ строго менше ніж ~N - 1~ кубик). Аналогічне міркування можна повторити багатократно й отримати, що далі є рівно ~h_3 - h_2~ значень ~N - 2~, рівно ~h_4 - h_3~ значень ~N - 3~, ..., рівно ~h_N - h_{N-1}~ значень ~1~.

### Асимптотична складність
визначається, в основному, використаним сортуванням. Бульбашка, вибір та інші прості методи сортування мають складність ~O(N^2)~ і не мають шансів укластися в обмеження часу на всіх тестах. Сортування злиттям, сортування Хоара (QuickSort) та пірамідальне сортування мають складність ~Θ(N log N)~ що при ~N < 123456~ цілком прийнятно.

(Хто не знає цих алгоритмів --- знайдіть у літературі або в Інтернеті; сортування Хоара, хоч і називається QuickSort, насправді має складність ~Θ(N log N)~ не завжди, а тільки у більшості випадків, іноді погіршуючись аж до ~N^2~; ця задача не містить спеціальних анти-quick-sort-івських тестів, тому саме тут це не важливо, але для розуміння загальної картини варто це знати.)

Можна й скористатися бібліотечним сортуванням, якщо таке є (функція `sort` бібліотеки `algorithm` мови C++, або метод `Arrays.sort` мови Java, або метод `sort` пітонівського `list`-а, тощо), не розбираючись, як це влаштовано всередині. Так робити не заборонено. Інша справа, що знання про те, як насправді влаштовані ці підпрограми, можуть знадобитися в якихось інших ситуаціях.

### Альтернативний розв'язок: асимптотика ~Θ(N + max a_j)~ та отримання 2-ї відповіді навіть без 1-ї.
В цій задачі можна застосувати *сортування підрахунком* (*counting sort*). Його суть така: заводиться масив `num`, *індекси* якого відповідають *висотам*, а значення --- *кількості* стовпчиків відповідної висоти (технічно --- усі елементи ініціалізуються нулями, а при читанні вхідних даних, замість `read(a[i])`, робляться дії `read(a); num[a]:=num[a]+1`).

1-а відповідь (саме сортування підрахунком) формується як "`num[1]` штук одиниць, потім `num[2]` штук двійок, тощо" (до речі, це дещо схоже на формування 2-го рядка відповіді раніше розглянутим способом, так що знання сортування підрахунком може бути корисним як для того, щоб використати його тут, так і для придумування вищезгаданого знаходження 2-ї відповіді 1-м способом).

А 2-у відповідь можна отримати так: сформувати на основі масиву `num` масив `num_gr_eq`, тобто "кількість більших-або-рівних" (наприклад, способом, показаним у коді праворуч), і просто вивести усі елементи `num_gr_eq` чи то до кінця, чи то доки вони ненульові.
```text
num_gr_eq[max_a_j]:=num[max_a_j];
for j:=max_a_j-1 downto 1 do
    num_gr_eq[j]:=num_gr_eq[j+1]+num[j];
```

Легко бачити, що асимптотика такого підходу ~Θ(N + max a_j)~, що формально краще за ~Θ(N log N)~. Втім, на практиці різниця між ними невелика й у значній мірі нівелюється часом читання вхідних даних. Так що питання більше в тому, що зручніше писати. Якщо є зручне готове бібліотечне сортування --- мабуть, краще використати його і знаходження 2-ї відповіді через 1-у.