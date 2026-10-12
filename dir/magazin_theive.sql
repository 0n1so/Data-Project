SELECT cashier, COUNT(*) AS cnt, SUM(amount) AS total
FROM transactions
WHERE `type` = 'refund' AND amount IS NOT NULL
GROUP BY cashier;

SELECT cashier,
       SUM(`type` = 'refund') / COUNT(`type`) AS share
FROM transactions
WHERE amount IS NOT NULL
GROUP BY cashier;

SELECT *
FROM (
    SELECT id, cashier, amount,
           (amount - AVG(amount) OVER ()) / STDDEV_POP(amount) OVER () AS z
    FROM transactions
    WHERE `type` = 'refund' AND amount IS NOT NULL
) t
WHERE z > 0.8;

SELECT cashier, COUNT(*) AS night_refunds
FROM transactions
WHERE `type` = 'refund'
  AND amount IS NOT NULL
  AND `hour` > 21
GROUP BY cashier
ORDER BY night_refunds DESC
LIMIT 1;

WITH refunds AS (
    SELECT id, cashier, amount, `hour`,
           (amount - AVG(amount) OVER ()) / STDDEV_POP(amount) OVER () AS z
    FROM transactions
    WHERE `type` = 'refund' AND amount IS NOT NULL
),
top_refunder AS (
    SELECT cashier FROM refunds
    GROUP BY cashier ORDER BY COUNT(*) DESC LIMIT 1
),
top_night AS (
    SELECT cashier FROM refunds
    WHERE `hour` > 21
    GROUP BY cashier ORDER BY COUNT(*) DESC LIMIT 1
),
top_anomaly AS (
    SELECT cashier FROM refunds
    WHERE z > 0.8
    GROUP BY cashier ORDER BY COUNT(*) DESC LIMIT 1
)
SELECT COALESCE(
    (SELECT r.cashier
     FROM top_refunder r
     JOIN top_night n   ON n.cashier = r.cashier
     JOIN top_anomaly a ON a.cashier = r.cashier),
    'не знайдено'
) AS suspect;