USE GG;

CREATE TABLE transactions (
    id      INT PRIMARY KEY,
    cashier VARCHAR(50) NOT NULL,
    `type`  VARCHAR(10) NOT NULL,
    amount  DECIMAL(10,2) NULL,
    `hour`  TINYINT NOT NULL
);

INSERT INTO transactions (id, cashier, `type`, amount, `hour`) VALUES
(1,  'Ann', 'refund',  50.00, 10),
(2,  'Bob', 'refund', 200.00, 23),
(3,  'Cat', 'sale',    40.00, 11),
(4,  'Bob', 'refund', 250.00, 22),
(5,  'Ann', 'sale',    60.00, 12),
(6,  'Bob', 'refund', 300.00, 23),
(7,  'Cat', 'sale',    45.00, 13),
(8,  'Bob', 'refund', 280.00, 22),
(9,  'Ann', 'sale',    55.00, 14),
(10, 'Bob', 'sale',    70.00, 15),
(11, 'Cat', 'refund',  NULL,  16),
(12, 'Bob', 'refund', 320.00, 23);