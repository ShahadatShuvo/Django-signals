buyers: user -> buyer, post_save
cars: car -> buyer, post_save vs pre_save, pre_save vs save
orders: order, m2m_changed, order->sale, post_save
#sales: sale -> order, pre_delete