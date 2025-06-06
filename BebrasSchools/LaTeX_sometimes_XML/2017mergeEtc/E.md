# Сума

Є ***гарантовано відсортована*** за&nbsp;строгим зростанням послідовність з&nbsp;~n~ цілих чисел та&nbsp;число `SUM_NEED`. («Строге» зростання означає, що&nbsp;кожен наступний строго більший за&nbsp;попередні, тобто не&nbsp;буває різних елементів з&nbsp;однаковим значенням.) Скільки є різних способів задати це число&nbsp;як&nbsp;суму ~a[i]+a[k]~? (Тобто,&nbsp;як&nbsp;суму з&nbsp;рівно двох доданків; допускається, якщо так виходить потрібна сума, щоб це був двічі взятий один елемент; способи ~a[i]+a[k]~ та&nbsp;~a[k]+a[i]~ (при&nbsp;~i \ne k~) вважаються різними.

## Вхідні дані
Перший рядок містить кількість елементів послідовності ~n~ (~1 \le n \le 123456~). Другий рядок містить ~n~ чисел - самі елементи. Третій рядок містить потрібну суму `SUM_NEED`.

## Вихідні дані
Єдине число - кількість способів отримати `SUM_NEED`&nbsp;як&nbsp;~a[i]+a[k]~.

## Приклади:
**Вхідні дані:**
```
7
2 3 5 7 11 13 17
22
```

**Вихідні дані:**
```
3
```

## Примітка
Цими трьома способами є:
1. ~5 + 17~;
2. ~11 + 11~;
3. ~17 + 5~.
