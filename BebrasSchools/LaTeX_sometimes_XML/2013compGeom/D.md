# Яка частина прямої у&nbsp;крузі?

Є коло (задане радіусом і&nbsp;координатами центра) і&nbsp;пряма (задана координатами двох своїх точок).

Якої довжини відрізок прямої лежить у&nbsp;крузі (всередині кола)?

## Вхідні дані
Слід прочитати зі&nbsp;стандартного вводу (клавіатури). У&nbsp;першому рядку задано три чи́сла: спочатку радіус кола ~R~, потім координати його центра ~Cx Cy~. У&nbsp;другому та&nbsp;третьому задано по&nbsp;два чи́сла — ~x~-&nbsp;та&nbsp;~y~-координати точок (гарантовано двох різних), через які проходить пряма. Всі чи́сла цілі, за&nbsp;абсолютним значенням не&nbsp;перевищують 10000.

## Вихідні дані
Вивести єдине число́: якщо пряма і&nbsp;коло мають хоча&nbsp;б&nbsp;одну спільну точку — довжину відрізка цієї прямої, що&nbsp;лежить у&nbsp;крузі (всередині кола); якщо не&nbsp;мають жодної спільної точки — замість цієї довжини вивести число́ `-1`.

У&nbsp;випадку торкання прямої до&nbsp;кола, спільна точка є, але відрізка ненульової довжини нема; отже, при торканні слід виводити `0`.

Результат при виведенні *не&nbsp;можна* заокруглювати (а&nbsp;виводити в&nbsp;експоненційній формі, як-то `6.0000000000000000E+0000` замість `6`, можна).

## Приклади
**Вхідні дані:**
```
5 0 0
4 1
4 2
```

**Вихідні дані:**
```
6
```
