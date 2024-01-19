#!/usr/bin/env python

import sys


mapping = {
    '1': 'Credit card',
    '2': 'Cash',
    '3': 'No charge',
    '4': 'Dispute',
    '5': 'Unknown',
    '6': 'Voided trip'
    }


def perform_reduce():
    current_key = None
    sum = 0
    count = 0

    for line in sys.stdin:
        key, value = line.split('\t')
        
        if key != current_key:
            if current_key:
                avg = sum / count
                month, payment_type = current_key.split(',')
                print('{0},{1},{2:.2f}'.format(month, mapping[payment_type], avg))
            current_key = key

            sum = 0
            count = 0

        sum += float(value)
        count += 1

    if current_key:
        avg = sum / count
        month, payment_type = current_key.split(',')
        print('{0},{1},{2:.2f}'.format(month, mapping[payment_type], avg))


if __name__ == '__main__':
    perform_reduce()
