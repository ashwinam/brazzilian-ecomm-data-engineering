import pytest
import pandas as pd

@pytest.fixture
def sample_orders_df():
    data = {
        'order_id': [
            'e481f51cbdc54678b7cc49136f2d6af7', 
            '53cdb2fc8bc7dce0b6741e2150273451', 
            '47770eb9100c2d0c44946d9cf07ec65d',
            '949d5b44dbf5de918fe9c16f97b45f8a',
            'ad21c59c0840e6cb83a9ceb5573f8159'
            ],
        'customer_id': [
            '9ef432eb6251297304e76186b10a928d',
            'b0830fb4747a6c6d20dea0b8c802d7ef',
            '41ce2a54c0b03bf3443c3d931a367089',
            'f88197465ea7920adcdbec7375364d82',
            '8ab97904e6daea8866dbdbc4fb7aad2c'
        ],
        'order_status': [
            'delivered',
            'delivered',
            'delivered',
            'delivered',
            'delivered'
        ],
        'order_purchase_timestamp': [
            '2017-10-02 10:56:33',
            '2018-07-24 20:41:37',
            '2018-08-08 08:38:49',
            '2017-11-18 19:28:06',
            '2018-02-13 21:18:39'
        ],
        'order_approved_at': [
            '2017-10-02 11:07:15',
            '2018-07-26 03:24:27',
            '2018-08-08 08:55:23',
            '2017-11-18 19:45:59',
            '2018-02-13 22:20:29'
        ],
        'order_delivered_carrier_date': [
            '2017-10-04 19:55:00',
            '2018-07-26 14:31:00',
            '2018-08-08 13:50:00',
            '2017-11-22 13:39:59',
            '2018-02-14 19:46:34'
        ],
        'order_delivered_customer_date': [
            '2017-10-10 21:25:13',
            '2018-08-07 15:27:45',
            '2018-08-17 18:06:29',
            '2017-12-02 00:28:42',
            '2018-02-16 18:17:02'
        ],
        'order_estimated_delivery_date': [
            '2017-10-18 00:00:00',
            '2018-08-13 00:00:00',
            '2018-09-04 00:00:00',
            '2017-12-15 00:00:00',
            '2018-02-26 00:00:00'
        ]
    }
    sample_df = pd.DataFrame(data)
    return sample_df

@pytest.fixture
def sample_missing_timestamp_orders_df():
    data = {
        'order_id': [
            'e481f51cbdc54678b7cc49136f2d6af7', 
            '53cdb2fc8bc7dce0b6741e2150273451', 
            '47770eb9100c2d0c44946d9cf07ec65d',
            '949d5b44dbf5de918fe9c16f97b45f8a',
            'ad21c59c0840e6cb83a9ceb5573f8159'
            ],
        'customer_id': [
            '9ef432eb6251297304e76186b10a928d',
            'b0830fb4747a6c6d20dea0b8c802d7ef',
            '41ce2a54c0b03bf3443c3d931a367089',
            'f88197465ea7920adcdbec7375364d82',
            '8ab97904e6daea8866dbdbc4fb7aad2c'
        ],
        'order_status': [
            'delivered',
            'delivered',
            'delivered',
            'delivered',
            'delivered'
        ],
        'order_purchase_timestamp': [
            '2017-10-02 10:56:33',
            '2018-07-24 20:41:37',
            '2018-08-08 08:38:49',
            None,
            '2018-02-13 21:18:39'
        ],
        'order_approved_at': [
            '2017-10-02 11:07:15',
            '2018-07-26 03:24:27',
            None,
            '2017-11-18 19:45:59',
            '2018-02-13 22:20:29'
        ],
        'order_delivered_carrier_date': [
            '2017-10-04 19:55:00',
            '2018-07-26 14:31:00',
            '2018-08-08 13:50:00',
            '2017-11-22 13:39:59',
            '2018-02-14 19:46:34'
        ],
        'order_delivered_customer_date': [
            '2017-10-10 21:25:13',
            '2018-08-07 15:27:45',
            '2018-08-17 18:06:29',
            None,
            None
        ],
        'order_estimated_delivery_date': [
            '2017-10-18 00:00:00',
            None,
            None,
            '2017-12-15 00:00:00',
            '2018-02-26 00:00:00'
        ]
    }
    sample_missing_timestamp_df = pd.DataFrame(data)
    return sample_missing_timestamp_df