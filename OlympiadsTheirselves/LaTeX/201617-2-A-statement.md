Один зі&nbsp;способів обчислити сумарну площу доріг — це&nbsp;взяти загальну площу всього міста (включаючи квартали та&nbsp;дороги) і&nbsp;відняти від неї сумарну площу всіх кварталів (без доріг).

1.  **Розміри всього мі́ста:**
    *   Кількість кварталів зі&nbsp;сходу на&nbsp;захід: `n`.
    *   Кількість кварталів з&nbsp;півночі на&nbsp;південь: `m`.
    *   Ширина ву́лиці: `a`.
    *   Розмір сторони́ кварталу: `b`.

    Якщо є `n` кварталів зі&nbsp;сходу на&nbsp;захід, то&nbsp;між ними та&nbsp;по&nbsp;краях буде `n + 1` вертикальна вулиця.
    Загальна ширина мі́ста = (сумарна ширина `n` кварталів) + (сумарна ширина `n + 1` вертикальних вулиць)
    Загальна ширина міста = `n * b + (n + 1) * a`

    Аналогічно, якщо є `m` кварталів з&nbsp;півночі на&nbsp;південь, то&nbsp;між ними та&nbsp;по&nbsp;краях буде `m + 1` горизонтальна вулиця.
    Загальна висота міста = (сумарна висота `m` кварталів) + (сумарна висота `m + 1` горизонтальних вулиць)
    Загальна висота міста = `m * b + (m + 1) * a`

2.  **Загальна площа всього міста:**
    Площа = (Загальна ширина міста) * (Загальна висота міста)
    Площа_міста = `(n * b + (n + 1) * a) * (m * b + (m + 1) * a)`

3.  **Сумарна площа всіх кварталів (без доріг):**
    Кількість кварталів: `n * m`
    Площа одного кварталу: `b * b`
    Сумарна площа кварталів = `n * m * b * b`

4.  **Сумарна площа всіх доріг:**
    Площа доріг = Площа міста - Сумарна площа кварталів
    Площа доріг = `(n * b + (n + 1) * a) * (m * b + (m + 1) * a) - n * m * b * b`

Перевіримо на&nbsp;прикладі: a=2, b=8, n=4, m=3.
Загальна ширина міста = `4 * 8 + (4 + 1) * 2 = 32 + 5 * 2 = 32 + 10 = 42`
Загальна висота міста = `3 * 8 + (3 + 1) * 2 = 24 + 4 * 2 = 24 + 8 = 32`
Площа міста = `42 * 32 = 1344`
Сумарна площа кварталів = `4 * 3 * 8 * 8 = 12 * 64 = 768`
Площа доріг = `1344 - 768 = 576`. Це&nbsp;збігається з&nbsp;прикладом.

Отже, вираз:
`(n * b + (n + 1) * a) * (m * b + (m + 1) * a) - n * m * b * b`

Альтернативний підхід (додавання площ горизонтальних та&nbsp;вертикальних доріг та&nbsp;віднімання площ перехресть, які пораховані двічі):
Кількість горизонтальних доріг: `m + 1`. Довжина кожної: `n * b + (n + 1) * a`. Ширина кожної: `a`.
Площа горизонтальних доріг: `(m + 1) * a * (n * b + (n + 1) * a)`

Кількість вертикальних доріг: `n + 1`. Довжина кожної: `m * b + (m + 1) * a`. Ширина кожної: `a`.
Площа вертикальних доріг: `(n + 1) * a * (m * b + (m + 1) * a)`

Кількість перехресть: `(n + 1) * (m + 1)`. Площа кожного перехрестя: `a * a`.
Площа перехресть: `(n + 1) * (m + 1) * a * a`

Сумарна площа доріг:
`(m + 1) * a * (n * b + (n + 1) * a) + (n + 1) * a * (m * b + (m + 1) * a) - (n + 1) * (m + 1) * a * a`
Обидва вирази є математично еквівалентними. Перший виглядає дещо простішим для запису.

Вираз:
```
(n * b + (n + 1) * a) * (m * b + (m + 1) * a) - n * m * b * b
```
