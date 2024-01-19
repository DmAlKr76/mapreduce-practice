#!/usr/bin/env python

from datetime import datetime
import sys


def perform_map():
    for line in sys.stdin:
        line = line.strip()
        data = line.split(',')
        
        if data[0] != 'VendorID':
            tpep_pickup_datetime = datetime.strptime(data[1], '%Y-%m-%d %H:%M:%S')
            payment_type = data[9]
            tip_amount = float(data[13])
            
            if tpep_pickup_datetime.year == 2020 and payment_type:
                month = tpep_pickup_datetime.strftime('%Y-%m')
                print('{0},{1}\t{2}'.format(month, payment_type, tip_amount))


if __name__ == '__main__':
    perform_map()
