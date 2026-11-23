import pytest
import pandas as pd

# Orders
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

# Order Items
@pytest.fixture
def sample_order_items_df():
    data = {
        'order_id': [
            '00404fa7a687c8c44ca69d42695aae73',
            '00a870c6c06346e85335524935c600c0',
            '011c899816ea29773525bd3322dbb6aa',
            '012b3f6ab7776a8ab3443a4ad7bef2e6',
            '012b3f6ab7776a8ab3443a4ad7bef2e6'
        ],
        'order_item_id': [
            1, 1, 1, 1, 2
        ], 
        'product_id': [
            '53b36df67ebb7c41585e8d54d6772e08',
            'aca2eb7d00ea1a7b8ebd4e68314663af',
            '53b36df67ebb7c41585e8d54d6772e08',
            '422879e10f46682990de24d770e7f83d',
            '422879e10f46682990de24d770e7f83d'
        ],
        'seller_id': [
            '7d13fca15225358621be4086e1eb0964',
            '955fee9216a65b617aa5c0531780ce60',
            '7d13fca15225358621be4086e1eb0964',
            '1f50f920176fa81dab994f9023523100',
            '1f50f920176fa81dab994f9023523100'
        ],
        'shipping_limit_date': [
            '2018-05-15 04:31:26',
            '2018-05-14 00:14:29',
            '2018-05-07 05:30:45',
            '2018-05-09 21:30:50',
            '2018-05-09 21:30:50'
        ],
        'price': [
            99.9, 69.9, 99.9, 53.9, 53.9
        ],
        'freight_value': [
            0.0, 0.0, 0.0, 0.0, 0.0
        ]
    }

    order_items_df = pd.DataFrame(data)
    return order_items_df

@pytest.fixture
def sample_missing_timestamps_order_items_df():
    data = {
        'order_id': [
            '00404fa7a687c8c44ca69d42695aae73',
            '00a870c6c06346e85335524935c600c0',
            '011c899816ea29773525bd3322dbb6aa',
            '012b3f6ab7776a8ab3443a4ad7bef2e6',
            '012b3f6ab7776a8ab3443a4ad7bef2e6'
        ],
        'order_item_id': [
            1, 1, 1, 1, 2
        ], 
        'product_id': [
            '53b36df67ebb7c41585e8d54d6772e08',
            'aca2eb7d00ea1a7b8ebd4e68314663af',
            '53b36df67ebb7c41585e8d54d6772e08',
            '422879e10f46682990de24d770e7f83d',
            '422879e10f46682990de24d770e7f83d'
        ],
        'seller_id': [
            '7d13fca15225358621be4086e1eb0964',
            '955fee9216a65b617aa5c0531780ce60',
            '7d13fca15225358621be4086e1eb0964',
            '1f50f920176fa81dab994f9023523100',
            '1f50f920176fa81dab994f9023523100'
        ],
        'shipping_limit_date': [
            '2018-05-15 04:31:26',
            '2018-05-14 00:14:29',
            None,
            None,
            '2018-05-09 21:30:50'
        ],
        'price': [
            99.9, 69.9, 99.9, 53.9, 53.9
        ],
        'freight_value': [
            0.0, 0.0, 0.0, 0.0, 0.0
        ]
    }

    order_items_df = pd.DataFrame(data)
    return order_items_df

# Reviews
@pytest.fixture
def sample_review_df():
    data = {
        'review_id': [
            '7bc2406110b926393aa56f80a40eba40',
            '80e641a11e56f04c1ad469d5645fdfde',
            '228ce5500dc1d8e020d8d1322874b6f0',
            'e64fb393e7b32834bb789ff8bb30750e',
            'f7c4243c7fe1938f181bec41a392bdeb'
        ],
        'order_id': [
            '73fc7af87114b39712e6da79b0a377eb',
            'a548910a1c6147796b98fdf73dbeba33',
            'f9e4b658b201a9f2ecdecbb34bed034b',
            '658677c97b385a9be170737859d3511b',
            '8e6bfb81e283fa7e4f11123a3fb894f1'
        ],
        'review_score': [
            4, 5, 5, 5, 5
        ],
        'review_comment_title': [
            None, None, None, None, None
        ],
        'review_comment_message': [
            None, None, None, 
            'Recebi bem antes do prazo estipulado.',
            'Parabéns lojas lannister adorei comprar pela I...'
        ],
        'review_creation_date': [
            '2018-01-18 00:00:00',
            '2018-03-10 00:00:00',
            '2018-02-17 00:00:00',
            '2017-04-21 00:00:00',
            '2018-03-01 00:00:00'
        ],
        'review_answer_timestamp': [
            '2018-01-18 21:46:59',
            '2018-03-11 03:05:13',
            '2018-02-18 14:36:24',
            '2017-04-21 22:02:06',
            '2018-03-02 10:26:53'
        ]
    }

    sample_df = pd.DataFrame(data)

    return sample_df

@pytest.fixture
def sample_missing_timestamp_review_df():
    data = {
        'review_id': [
            '7bc2406110b926393aa56f80a40eba40',
            '80e641a11e56f04c1ad469d5645fdfde',
            '228ce5500dc1d8e020d8d1322874b6f0',
            'e64fb393e7b32834bb789ff8bb30750e',
            'f7c4243c7fe1938f181bec41a392bdeb'
        ],
        'order_id': [
            '73fc7af87114b39712e6da79b0a377eb',
            'a548910a1c6147796b98fdf73dbeba33',
            'f9e4b658b201a9f2ecdecbb34bed034b',
            '658677c97b385a9be170737859d3511b',
            '8e6bfb81e283fa7e4f11123a3fb894f1'
        ],
        'review_score': [
            4, 5, 5, 5, 5
        ],
        'review_comment_title': [
            None, None, None, None, None
        ],
        'review_comment_message': [
            None, None, None, 
            'Recebi bem antes do prazo estipulado.',
            'Parabéns lojas lannister adorei comprar pela I...'
        ],
        'review_creation_date': [
            '2018-01-18 00:00:00',
            None,
            '2018-02-17 00:00:00',
            '2017-04-21 00:00:00',
            '2018-03-01 00:00:00'
        ],
        'review_answer_timestamp': [
            '2018-01-18 21:46:59',
            '2018-03-11 03:05:13',
            '2018-02-18 14:36:24',
            None,
            None
        ]
    }

    sample_df = pd.DataFrame(data)

    return sample_df

# Validating Orders
@pytest.fixture
def sample_orders_df_for_duplicate_orders():
    data = {
        'order_id': [
            'e481f51cbdc54678b7cc49136f2d6af7', 
            '53cdb2fc8bc7dce0b6741e2150273451', 
            '53cdb2fc8bc7dce0b6741e2150273451',
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
def sample_orders_df_for_missing_order_and_customer():
    data = {
        'order_id': [
            'e481f51cbdc54678b7cc49136f2d6af7', 
            '53cdb2fc8bc7dce0b6741e2150273451', 
            '47770eb9100c2d0c44946d9cf07ec65d',
            None,
            'ad21c59c0840e6cb83a9ceb5573f8159'
            ],
        'customer_id': [
            '9ef432eb6251297304e76186b10a928d',
            'b0830fb4747a6c6d20dea0b8c802d7ef',
            None,
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
def sample_orders_df_for_missing_order_status():
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
            None,
            'delivered',
            None,
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