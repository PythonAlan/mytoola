#!/usr/bin/env python3
#antuor:Alan

wini_us = {
    28:2.81,
    56:2.81,
    85:2.81,
    113:2.82,
    141:3.25,#<150
    170:3.30,
    198:3.31,
    226:3.36,
    255:4.02, #<255
    283:4.17,
    311:4.32,
    340:4.46,
    368:4.60,
    396:5.22,
    425:5.41,
    453:5.58,#<453
    907:7.42,#
    1360:8.16,#
    1814:8.85,#<1500
    2268:9.31,
    2721:9.43,
    3175:9.78,
    3628:10.16,
    4082:10.82,#<4082
}




cn_us = {
    28:21.87/6.6,
    56:21.87/6.6,
    85:21.87/6.6,
    113:23.35/6.6,
    141:23.82/6.6,#<150
    170:24.29/6.6,
    198:24.66/6.6,
    226:25.04/6.6,
    255:25.41/6.6, #<255
    283:26.54/6.6,
    311:27.19/6.6,
    340:28.13/6.6,
    368:28.6/6.6,
    396:28.97/6.6,
    450:29.44/6.6,
    453:50.79/6.6,
    907:50.79/6.6,
    1360:55.13/6.6,
    1814:59.07/6.6,
    2286:61.97/6.6,
    2721:62.35/6.6,
    3175:64.79/6.6,
    3628:67.04/6.6,
    4082:71.16/6.6,
}


multichange_fba_us = {                      #Standard-Size Non-Media
    'Order_Handling_per_order':4.75,
    'Pick_Pack_per_Unit':0.75,
    'Weight_Handling_per_lb':0.45,
}


multichange_mulfba_Oversize_us = {
    'Order Handling':7.0,
    'Pick_Pack_per_Unit':3.0,
    'Weight_Handling_per_lb':0.50,   #Oversize Media and Non-Media
}




eub_us = {
    'weight_rate_below_200':0.075,
    'weight_rate_up_200':0.075,
    'Order Handling':9.0,
    'as_last_weight':70,
    'discount':0.91,
}



gz_under_250_eds_a_uk = {
    '1-20':2.46,
    '21-30':3.03,
    '31-40':3.44,
    '41-50':3.91,

}

gz_under_250_eds_b_uk = {
    '51-100':0.086,
    '101-300':0.081,
}

gz_over_250_4px_track_uk = {
    'weight_per_32_kg':0.032,
    'Order Handling':18,

}



gz_under_250_eds_a_de = {
    '1-20':2.46,
    '21-30':3.12,
    '31-40':3.54,
    '41-50':4.01,

}

gz_under_250_eds_b_de = {
    '51-100':0.087,
    '101-250':0.083,
}



gz_between_250_1000_YanWen_de = {
    '250-1000':0.047,
    'Order Handling':11,
}
gz_between_1kg_2kg_4px_track_de = {
    'packet_51_per_kg':0.051,
    'Order Handling':20,
}


gz_au = {
    'package_per_kg':0.072,
    'Order Handling':5.72,
}


wini_uk = {
    'Yodel Home Mini':2.2,
}


wini_AUPOST_au ={
    '<=500':26,
    '500-1000':29,
    '>1000':31
}

wini_dhl_de = {
    '0-1000':26,
    '1000-all':27,

}


sea = {
    'uk_fee':3150,
    'de_fee':2800,
    'us_fee':1450,
}






