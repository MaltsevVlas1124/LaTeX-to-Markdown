﻿Найлегше, мабуть, відняти з площі всього міста (доріг та кварталів) площу кварталів. Розмір міста "по горизонталі" (зі сходу на захід) становить `(n+1)*a+n*b`, бо кварталів ~n~, вулиць ~(n+1)~ (між усіма сусідніми кварталами та *по обидва боки*). Аналогічно, розмір "по вертикалі" становить `(m+1)*a+m*b`. Кварталів же `m*n` штук, кожен площею `b*b`.
Що дає формулу ~((n+1)*a + n*b) * ((m+1)*a + m*b) - n*m*b*b~.

Є й інші відповіді, як-то ~n*m*a*b*2 + (n+m)*a*b + (n+1)*(m+1)*a*a~ чи ~(n*(a+b)+a) * (m*(a+b)+a) - n*m*b*b~.
Зараховується будь-яка правильна.