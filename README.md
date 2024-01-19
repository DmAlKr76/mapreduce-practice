> # Задание

Подготовка:
- Создать S3 бакет в Object Storage.
- Скопировать данные желтого такси за 2020 год в созданный s3 бакет.


Необходимо написать map-reduce приложение, использующее скопированные на Object storage данные и вычисляющее отчет на каждый месяц 2020 года вида:

Month    |Payment type  | Tips average amount
---------|--------------|-------------------
2020-01  |Credit card   | 999.99

Требования к отчету:
- Количество файлов — 1
- Формат — csv
- Сортировка — не требуется
- Month считаем по полю tpep_pickup_datetime
- Payment type считаем по полю payment_type
- Tips average amount вычисляем по полю tip_amount

Маппинг типов оплат:

```
mapping = {
        1: 'Credit card',
        2: 'Cash',
        3: 'No charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided trip'
    }
```