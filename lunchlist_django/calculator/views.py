# from django.shortcuts import render
# import calculator.secondprice
#
# from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from calculator import secondprice
from .forms import AddForm


def Total_Cost(first,second,itemcost,commission):
        total_cost = float(first)+float(second)+float(itemcost)+float(commission)
        return float(total_cost)

def First_Class_Cost(weight,fisrt_class_rate):
        fisrt_class_cost = weight*fisrt_class_rate
        return fisrt_class_cost

def Commission_Cost(price,commission_rate,exchange_rate):
        commission_cost = float(price)*commission_rate*exchange_rate
        return commission_cost

def Second_Class_Cost():
        pass

def Gross_Profit(price,total_cost,exchange_rate):
    gross_profit = float(price)*exchange_rate - float(total_cost)
    return gross_profit


def Profit_margins(profit,price,exchange_rate):
    profit_margins = (float(profit)/(float(price)*exchange_rate))*100
    return profit_margins

def No_Commission_Cost(total_cost,commission_cost):
    no_commission_cost = float(total_cost) - float(commission_cost)
    return no_commission_cost


def Weight_range_cn_us(weight):
    if   weight < 85 or weight == 85:
         second_class_cn_us = secondprice.cn_us[85]
    elif weight < 85 or weight < 171:
         second_class_cn_us = secondprice.cn_us[170]
    elif weight > 170 and weight < 256:
        second_class_cn_us = secondprice.cn_us[255]
    elif weight > 255 and weight < 454:
        second_class_cn_us = secondprice.cn_us[450]
    elif weight > 453 and weight < 908:
        second_class_cn_us = secondprice.cn_us[907]
    elif weight > 907 and weight < 1815:
        second_class_cn_us = secondprice.cn_us[1814]
    elif weight > 1814 and weight < 4082:
        second_class_cn_us = secondprice.cn_us[4082]
    else:
        second_class_cn_us = secondprice.cn_us[4082]

    return second_class_cn_us

def Weight_range_wini_us(weight):
    if   weight < 85 or weight == 85:
         second_class_wini_us = secondprice.wini_us[85]
    elif weight > 85 and weight < 114 :
        second_class_wini_us = secondprice.wini_us[113]
    elif weight > 113 and weight < 141:
        second_class_wini_us = secondprice.wini_us[141]
    elif weight > 140 and weight < 171:
        second_class_wini_us = secondprice.wini_us[170]
    elif weight > 170 and weight < 199:
        second_class_wini_us = secondprice.wini_us[198]
    elif weight > 198 and weight < 227:
        second_class_wini_us = secondprice.wini_us[226]
    elif weight > 226 and weight < 256:
        second_class_wini_us = secondprice.wini_us[255]
    elif weight >255 and weight < 284:
        second_class_wini_us = secondprice.wini_us[283]
    elif weight >283 and weight < 312:
        second_class_wini_us = secondprice.wini_us[311]
    elif weight >311 and weight < 341:
        second_class_wini_us = secondprice.wini_us[340]
    elif weight >340 and weight < 369:
        second_class_wini_us = secondprice.wini_us[368]
    elif weight >368 and weight < 397:
        second_class_wini_us = secondprice.wini_us[396]
    elif weight >396 and weight < 426:
        second_class_wini_us = secondprice.wini_us[425]
    elif weight >425 and weight < 453:
        second_class_wini_us = secondprice.wini_us[425]
    elif weight >453 and weight < 908:
        second_class_wini_us = secondprice.wini_us[907]
    elif weight >907 and weight < 1361:
        second_class_wini_us = secondprice.wini_us[1360]
    elif weight >1360 and weight < 1815:
        second_class_wini_us = secondprice.wini_us[1814]
    elif weight >1814 and weight < 2269:
        second_class_wini_us = secondprice.wini_us[2268]
    elif weight >2268 and weight < 2722:
        second_class_wini_us = secondprice.wini_us[2721]
    elif weight >2721 and weight < 3176:
        second_class_wini_us = secondprice.wini_us[3175]
    elif weight >3175 and weight < 3629:
        second_class_wini_us = secondprice.wini_us[3628]
    else:
        second_class_wini_us = secondprice.wini_us[4082]

    return second_class_wini_us


def Weight_range_mul_fba_us(weight):
    weight = float(weight)/453
    Order_Handling_per_order = secondprice.multichange_fba_us['Order_Handling_per_order']
    Pick_Pack_per_Unit = secondprice.multichange_fba_us['Pick_Pack_per_Unit']
    Weight_Handling_per_lb = secondprice.multichange_fba_us['Weight_Handling_per_lb']
    second_class_mulfba_us = Order_Handling_per_order+Pick_Pack_per_Unit+weight*Weight_Handling_per_lb
    return second_class_mulfba_us


def Weight_range_eub_us(weight):
    if weight <secondprice.eub_us['as_last_weight'] or weight == secondprice.eub_us['as_last_weight']:
        eub_us = float(secondprice.eub_us['weight_rate_below_200']*secondprice.eub_us['discount']*secondprice.eub_us['as_last_weight']+secondprice.eub_us['Order Handling'])
    elif weight >secondprice.eub_us['as_last_weight'] and weight < 200:
        eub_us = float(secondprice.eub_us['weight_rate_below_200']*weight*secondprice.eub_us['discount']+secondprice.eub_us['Order Handling'])
    else:
        eub_us = float(secondprice.eub_us['weight_rate_up_200']*weight*secondprice.eub_us['discount']+secondprice.eub_us['Order Handling'])
    return eub_us

def Weight_range_gz_uk(weight):
    if weight < 20 or weight == 20:
        second_class_gz_uk = secondprice.gz_under_250_eds_a_uk['1-20']
    elif weight> 20 and weight < 31:
        second_class_gz_uk = secondprice.gz_under_250_eds_a_uk['21-30']
    elif weight >30 and weight< 41:
        second_class_gz_uk = secondprice.gz_under_250_eds_a_uk['31-40']
    elif weight> 40 and weight < 51:
        second_class_gz_uk = secondprice.gz_under_250_eds_a_uk['41-50']
    elif weight>50 and weight < 101:
        second_class_gz_uk = secondprice.gz_under_250_eds_b_uk['51-100']*weight
    elif weight>100 and weight < 301:
        second_class_gz_uk = secondprice.gz_under_250_eds_b_uk['101-300']*weight
    else:
        second_class_gz_uk = secondprice.gz_over_250_4px_track_uk['weight_per_32_kg']*weight+secondprice.gz_over_250_4px_track_uk['Order Handling']
    return second_class_gz_uk


def Weight_range_gz_de(weight):
    if weight <20 or weight ==20:
        second_class_gz_de = secondprice.gz_under_250_eds_a_de['1-20']
    elif weight> 20 and weight < 31:
        second_class_gz_de = secondprice.gz_under_250_eds_a_de['21-30']
    elif weight >30 and weight< 41:
        second_class_gz_de = secondprice.gz_under_250_eds_a_de['31-40']
    elif weight> 40 and weight < 51:
        second_class_gz_de = secondprice.gz_under_250_eds_a_de['41-50']
    elif weight>50 and weight < 101:
        second_class_gz_de = secondprice.gz_under_250_eds_b_de['51-100']*weight
    elif weight>100 and weight < 251:
        second_class_gz_de = secondprice.gz_under_250_eds_b_de['101-250']*weight
    elif weight >250 and weight <1001:
        second_class_gz_de = secondprice.gz_between_250_1000_YanWen_de['250-1000']*weight+secondprice.gz_between_250_1000_YanWen_de['Order Handling']
    else:
        second_class_gz_de = secondprice.gz_between_1kg_2kg_4px_track_de['packet_51_per_kg']*weight+secondprice.gz_between_1kg_2kg_4px_track_de['Order Handling']
    return second_class_gz_de


def Weight_range_gz_au(weight):
    second_class_gz_au = secondprice.gz_au['package_per_kg']*weight+secondprice.gz_au['Order Handling']
    return second_class_gz_au

def Weight_range_wini_uk(weight):
    second_class_wini_uk = secondprice.wini_uk['Yodel Home Mini']
    return  second_class_wini_uk

def Weight_range_wini_de(weight):
    if weight <1001:
        second_class_wini_de = secondprice.wini_dhl_de['0-1000']
    else:
        second_class_wini_de = secondprice.wini_dhl_de['1000-all']
    return second_class_wini_de


def Weight_range_wini_au(weight):
    if weight <501:
        second_class_wini_au = secondprice.wini_AUPOST_au['<=500']
    elif weight>500 and weight<1001:
        second_class_wini_au = secondprice.wini_AUPOST_au['500-1000']
    else:
        second_class_wini_au = secondprice.wini_AUPOST_au['>1000']

    return second_class_wini_au


def Sea_fee(volume,fee):
    sea_fee = volume*fee
    return sea_fee




def air(request):
    if request.method == 'POST':

        form = AddForm(request.POST)

        if form.is_valid():
            price = round(form.cleaned_data['price'],1)
            weight = form.cleaned_data['weight']
            purchase_price = form.cleaned_data['purchase_price']
            volume = form.cleaned_data['volume']


            first_class_rate_us = 0.030
            first_class_rate_uk = 0.034
            first_class_rate_de = 0.035
            first_class_rate_au = 0.027
            exchange_rate_us = 6.60
            exchange_rate_uk= 8.26
            exchange_rate_de = 7.05
            exchange_rate_au = 5.00

            second_class_wini_us = round(Weight_range_wini_us(weight),1)
            second_class_wini_uk = round(Weight_range_wini_uk(weight),1)
            second_class_wini_de = round(Weight_range_wini_de(weight)/exchange_rate_de,1)
            second_class_wini_au = round(Weight_range_wini_au(weight)/exchange_rate_au,1)

            second_class_cn_us = round(Weight_range_cn_us(weight),1)
            second_class_mulfba_us = round(Weight_range_mul_fba_us(weight),1)
            second_class_eub_us = round(Weight_range_eub_us(weight)/exchange_rate_us,1)
            second_class_gz_uk = round(Weight_range_gz_uk(weight)/exchange_rate_uk,1)
            second_class_gz_de = round(Weight_range_gz_de(weight)/exchange_rate_de,1)
            second_class_gz_au = round(Weight_range_gz_au(weight)/exchange_rate_au,1)

            second_class_wini_us_rmb = round(Weight_range_wini_us(weight)*exchange_rate_us,1)
            second_class_cn_us_rmb = round(Weight_range_cn_us(weight)*exchange_rate_us,1)
            second_class_mulfba_us_rmb = round(Weight_range_mul_fba_us(weight)*exchange_rate_us,1)
            second_class_eub_us_rmb = round(Weight_range_eub_us(weight),1)
            second_class_gz_uk_rmb = round(Weight_range_gz_uk(weight),1)
            second_class_gz_de_rmb = round(Weight_range_gz_de(weight),1)
            second_class_gz_au_rmb = round(Weight_range_gz_au(weight),1)
            second_class_wini_uk_rmb = round(Weight_range_wini_uk(weight)*exchange_rate_uk,1)
            second_class_wini_au_rmb = round(Weight_range_wini_au(weight),1)
            second_class_wini_de_rmb = round(Weight_range_wini_de(weight),1)


            commission_rate = 0.18




            first_class_cost_wini_us = round(float(First_Class_Cost(weight,first_class_rate_us)),1)
            first_class_cost_wini_sea_us = round(float(Sea_fee(volume,secondprice.sea['us_fee'])),1)
            second_class_wini_us = second_class_wini_us
            commission_cost_us = round(Commission_Cost(price,commission_rate,exchange_rate_us),1)
            total_cost_wini_us = round(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_us)),
                                            second_class_wini_us*exchange_rate_us,
                                            purchase_price,
                                            commission_cost_us,
                                             )),1)
            total_cost_wini_sea_us = round(float(Total_Cost(first_class_cost_wini_sea_us,
                                            second_class_wini_us*exchange_rate_us,
                                            purchase_price,
                                            commission_cost_us,
                                             )),1)

            no_commission_cost_wini_sea_us = No_Commission_Cost(total_cost_wini_sea_us,commission_cost_us)
            gross_profit_wini_sea_us = round(Gross_Profit(price,total_cost_wini_sea_us,exchange_rate_us),1)
            profit_margins_wini_sea_us = round(Profit_margins(gross_profit_wini_sea_us,price,exchange_rate_us),1)
            zero_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/exchange_rate_us/0.82,1)
            five_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/0.77/exchange_rate_us,1)
            ten_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/0.72/exchange_rate_us,1)
            fifteen_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/0.67/exchange_rate_us,1)
            twenty_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/0.62/exchange_rate_us,1)
            twentyfive_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/0.57/exchange_rate_us,1)
            thirty_sale_price_wini_sea_us = round(no_commission_cost_wini_sea_us/0.52/exchange_rate_us,1)

            no_commission_cost_wini_us = No_Commission_Cost(total_cost_wini_us,commission_cost_us)
            gross_profit_wini_us = round(Gross_Profit(price,total_cost_wini_us,exchange_rate_us),1)
            profit_margins_wini_us = round(Profit_margins(gross_profit_wini_us,price,exchange_rate_us),1)
            zero_sale_price_wini_us = round(no_commission_cost_wini_us/exchange_rate_us/0.82,1)
            five_sale_price_wini_us = round(no_commission_cost_wini_us/0.77/exchange_rate_us,1)
            ten_sale_price_wini_us = round(no_commission_cost_wini_us/0.72/exchange_rate_us,1)
            fifteen_sale_price_wini_us = round(no_commission_cost_wini_us/0.67/exchange_rate_us,1)
            twenty_sale_price_wini_us = round(no_commission_cost_wini_us/0.62/exchange_rate_us,1)
            twentyfive_sale_price_wini_us = round(no_commission_cost_wini_us/0.57/exchange_rate_us,1)
            thirty_sale_price_wini_us = round(no_commission_cost_wini_us/0.52/exchange_rate_us,1)

            first_class_cost_cn_us = round(float(First_Class_Cost(weight,first_class_rate_us)),1)
            second_class_cn_us = round(float(second_class_cn_us),1)
            commission_cost_us = round(Commission_Cost(price,commission_rate,exchange_rate_us),1)
            total_cost_cn_us = round(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_us)),
                                            float(second_class_cn_us)*exchange_rate_us,
                                            purchase_price,
                                            commission_cost_us,
                                             )),1)
            no_commission_cost_cn_us = No_Commission_Cost(total_cost_cn_us,commission_cost_us)
            gross_profit_cn_us = round(Gross_Profit(price,total_cost_cn_us,exchange_rate_us),1)
            profit_margins_cn_us = round(Profit_margins(gross_profit_cn_us,price,exchange_rate_us),1)
            zero_sale_price_cn_us = round(no_commission_cost_cn_us/exchange_rate_us/0.82,1)
            five_sale_price_cn_us = round(no_commission_cost_cn_us/0.77/exchange_rate_us,1)
            ten_sale_price_cn_us = round(no_commission_cost_cn_us/0.72/exchange_rate_us,1)
            fifteen_sale_price_cn_us = round(no_commission_cost_cn_us/0.67/exchange_rate_us,1)
            twenty_sale_price_cn_us = round(no_commission_cost_cn_us/0.62/exchange_rate_us,1)
            twentyfive_sale_price_cn_us = round(no_commission_cost_cn_us/0.57/exchange_rate_us,1)
            thirty_sale_price_cn_us = round(no_commission_cost_cn_us/0.52/exchange_rate_us,1)



            first_class_cost_mulfba_us = round(float(First_Class_Cost(weight,first_class_rate_us)),1)
            second_class_mulfba_us = round(float(second_class_mulfba_us),1)
            commission_cost_us = round(Commission_Cost(price,commission_rate,exchange_rate_us),1)
            total_cost_mulfba_us = round(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_us)),
                                            float(second_class_mulfba_us)*exchange_rate_us,
                                            purchase_price,
                                            commission_cost_us,
                                             )),1)
            no_commission_cost_mulfba_us = No_Commission_Cost(total_cost_mulfba_us,commission_cost_us)
            gross_profit_mulfba_us = round(Gross_Profit(price,total_cost_mulfba_us,exchange_rate_us),1)
            profit_margins_mulfba_us = round(Profit_margins(gross_profit_mulfba_us,price,exchange_rate_us),1)
            zero_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/exchange_rate_us/0.82,1)
            five_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/0.77/exchange_rate_us,1)
            ten_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/0.72/exchange_rate_us,1)
            fifteen_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/0.67/exchange_rate_us,1)
            twenty_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/0.62/exchange_rate_us,1)
            twentyfive_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/0.57/exchange_rate_us,1)
            thirty_sale_price_mulfba_us = round(no_commission_cost_mulfba_us/0.52/exchange_rate_us,1)






            first_class_cost_eub_us = 0
            second_class_eub_us = round(float(second_class_eub_us),1)
            commission_cost_us = round(Commission_Cost(price,commission_rate,exchange_rate_us),1)
            total_cost_eub_us = round(float(Total_Cost(first_class_cost_eub_us,
                                            float(second_class_eub_us)*exchange_rate_us,
                                            purchase_price,
                                            commission_cost_us,
                                             )),1)
            no_commission_cost_eub_us = No_Commission_Cost(total_cost_eub_us,commission_cost_us)
            gross_profit_eub_us = round(Gross_Profit(price,total_cost_eub_us,exchange_rate_us),1)
            profit_margins_eub_us = round(Profit_margins(gross_profit_eub_us,price,exchange_rate_us),1)
            zero_sale_price_eub_us = round(no_commission_cost_eub_us/exchange_rate_us/0.82,1)
            five_sale_price_eub_us = round(no_commission_cost_eub_us/0.77/exchange_rate_us,1)
            ten_sale_price_eub_us = round(no_commission_cost_eub_us/0.72/exchange_rate_us,1)
            fifteen_sale_price_eub_us = round(no_commission_cost_eub_us/0.67/exchange_rate_us,1)
            twenty_sale_price_eub_us = round(no_commission_cost_eub_us/0.62/exchange_rate_us,1)
            twentyfive_sale_price_eub_us = round(no_commission_cost_eub_us/0.57/exchange_rate_us,1)
            thirty_sale_price_eub_us = round(no_commission_cost_eub_us/0.52/exchange_rate_us,1)


            first_class_cost_gz_uk = 0
            second_class_gz_uk = round(float(second_class_gz_uk),1)
            commission_cost_uk = round(Commission_Cost(price,commission_rate,exchange_rate_uk),1)
            total_cost_gz_uk = round(float(Total_Cost(first_class_cost_gz_uk,
                                            float(second_class_gz_uk)*exchange_rate_uk,
                                            purchase_price,
                                            commission_cost_uk,
                                             )),1)
            no_commission_cost_gz_uk = No_Commission_Cost(total_cost_gz_uk,commission_cost_uk)
            gross_profit_gz_uk = round(Gross_Profit(price,total_cost_gz_uk,exchange_rate_uk),1)
            profit_margins_gz_uk = round(Profit_margins(gross_profit_gz_uk,price,exchange_rate_uk),1)
            zero_sale_price_gz_uk = round((no_commission_cost_gz_uk/exchange_rate_uk/0.82),1)
            five_sale_price_gz_uk = round((no_commission_cost_gz_uk/0.77/exchange_rate_uk),1)
            ten_sale_price_gz_uk = round((no_commission_cost_gz_uk/0.72/exchange_rate_uk),1)
            fifteen_sale_price_gz_uk = round((no_commission_cost_gz_uk/0.67/exchange_rate_uk),1)
            twenty_sale_price_gz_uk = round((no_commission_cost_gz_uk/0.62/exchange_rate_uk),1)
            twentyfive_sale_price_gz_uk = round((no_commission_cost_gz_uk/0.57/exchange_rate_uk),1)
            thirty_sale_price_gz_uk = round((no_commission_cost_gz_uk/0.52/exchange_rate_uk),1)

            first_class_cost_gz_de = 0
            second_class_gz_de = round(float(second_class_gz_de),1)
            commission_cost_de = round(Commission_Cost(price,commission_rate,exchange_rate_de),1)
            total_cost_gz_de = round(float(Total_Cost(first_class_cost_gz_de,
                                            float(second_class_gz_de)*exchange_rate_de,
                                            purchase_price,
                                            commission_cost_de,
                                             )),1)
            no_commission_cost_gz_de = No_Commission_Cost(total_cost_gz_de,commission_cost_de)
            gross_profit_gz_de = round(Gross_Profit(price,total_cost_gz_de,exchange_rate_de),1)
            profit_margins_gz_de = round(Profit_margins(gross_profit_gz_de,price,exchange_rate_de),1)
            zero_sale_price_gz_de = round((no_commission_cost_gz_de/exchange_rate_de/0.82),1)
            five_sale_price_gz_de = round((no_commission_cost_gz_de/0.77/exchange_rate_de),1)
            ten_sale_price_gz_de = round((no_commission_cost_gz_de/0.72/exchange_rate_de),1)
            fifteen_sale_price_gz_de = round((no_commission_cost_gz_de/0.67/exchange_rate_de),1)
            twenty_sale_price_gz_de = round((no_commission_cost_gz_de/0.62/exchange_rate_de),1)
            twentyfive_sale_price_gz_de = round((no_commission_cost_gz_de/0.57/exchange_rate_de),1)
            thirty_sale_price_gz_de = round((no_commission_cost_gz_de/0.52/exchange_rate_de),1)



            first_class_cost_gz_au = 0
            second_class_gz_au = round(float(second_class_gz_au),1)
            commission_cost_au = round(Commission_Cost(price,commission_rate,exchange_rate_au),1)
            total_cost_gz_au = round(float(Total_Cost(first_class_cost_gz_au,
                                            float(second_class_gz_au)*exchange_rate_au,
                                            purchase_price,
                                            commission_cost_au,
                                             )),1)
            no_commission_cost_gz_au = No_Commission_Cost(total_cost_gz_au,commission_cost_au)
            gross_profit_gz_au = round(Gross_Profit(price,total_cost_gz_au,exchange_rate_au),1)
            profit_margins_gz_au = round(Profit_margins(gross_profit_gz_au,price,exchange_rate_au),1)
            zero_sale_price_gz_au = round((no_commission_cost_gz_au/exchange_rate_au/0.82),1)
            five_sale_price_gz_au = round((no_commission_cost_gz_au/0.77/exchange_rate_au),1)
            ten_sale_price_gz_au = round((no_commission_cost_gz_au/0.72/exchange_rate_au),1)
            fifteen_sale_price_gz_au = round((no_commission_cost_gz_au/0.67/exchange_rate_au),1)
            twenty_sale_price_gz_au = round((no_commission_cost_gz_au/0.62/exchange_rate_au),1)
            twentyfive_sale_price_gz_au = round((no_commission_cost_gz_au/0.57/exchange_rate_au),1)
            thirty_sale_price_gz_au = round((no_commission_cost_gz_au/0.52/exchange_rate_au),1)

            first_class_cost_wini_uk = round(float(First_Class_Cost(weight,first_class_rate_uk)),1)
            first_class_cost_wini_sea_uk = round(float(Sea_fee(volume,secondprice.sea['uk_fee'])),1)
            second_class_wini_uk = second_class_wini_uk
            commission_cost_uk = round(Commission_Cost(price,commission_rate,exchange_rate_uk),1)
            total_cost_wini_uk = round(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_uk)),
                                            second_class_wini_uk*exchange_rate_uk,
                                            purchase_price,
                                            commission_cost_uk,
                                             )),1)
            total_cost_wini_sea_uk = round(float(Total_Cost(first_class_cost_wini_sea_uk,
                                            second_class_wini_uk*exchange_rate_uk,
                                            purchase_price,
                                            commission_cost_uk,
                                             )),1)
            no_commission_cost_wini_uk = No_Commission_Cost(total_cost_wini_uk,commission_cost_uk)
            no_commission_cost_wini_sea_uk = No_Commission_Cost(total_cost_wini_sea_uk,commission_cost_uk)
            gross_profit_wini_uk = round(Gross_Profit(price,total_cost_wini_uk,exchange_rate_uk),1)
            gross_profit_wini_sea_uk = round(Gross_Profit(price,total_cost_wini_sea_uk,exchange_rate_uk),1)
            profit_margins_wini_sea_uk = round(Profit_margins(gross_profit_wini_sea_uk,price,exchange_rate_uk),1)
            zero_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/exchange_rate_uk/0.82,1)
            five_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/0.77/exchange_rate_uk,1)
            ten_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/0.72/exchange_rate_uk,1)
            fifteen_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/0.67/exchange_rate_uk,1)
            twenty_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/0.62/exchange_rate_uk,1)
            twentyfive_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/0.57/exchange_rate_uk,1)
            thirty_sale_price_wini_sea_uk = round(no_commission_cost_wini_sea_uk/0.52/exchange_rate_uk,1)
            profit_margins_wini_uk = round(Profit_margins(gross_profit_wini_uk,price,exchange_rate_uk),1)
            zero_sale_price_wini_uk = round(no_commission_cost_wini_uk/exchange_rate_uk/0.82,1)
            five_sale_price_wini_uk = round(no_commission_cost_wini_uk/0.77/exchange_rate_uk,1)
            ten_sale_price_wini_uk = round(no_commission_cost_wini_uk/0.72/exchange_rate_uk,1)
            fifteen_sale_price_wini_uk = round(no_commission_cost_wini_uk/0.67/exchange_rate_uk,1)
            twenty_sale_price_wini_uk = round(no_commission_cost_wini_uk/0.62/exchange_rate_uk,1)
            twentyfive_sale_price_wini_uk = round(no_commission_cost_wini_uk/0.57/exchange_rate_uk,1)
            thirty_sale_price_wini_uk = round(no_commission_cost_wini_uk/0.52/exchange_rate_uk,1)


            first_class_cost_wini_au = round(float(First_Class_Cost(weight,first_class_rate_au)),1)
            second_class_wini_au = second_class_wini_au
            commission_cost_au = round(Commission_Cost(price,commission_rate,exchange_rate_au),1)
            total_cost_wini_au = round(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_au)),
                                            second_class_wini_au*exchange_rate_au,
                                            purchase_price,
                                            commission_cost_au,
                                             )),1)
            no_commission_cost_wini_au = No_Commission_Cost(total_cost_wini_au,commission_cost_au)
            gross_profit_wini_au = round(Gross_Profit(price,total_cost_wini_au,exchange_rate_au),1)
            profit_margins_wini_au = round(Profit_margins(gross_profit_wini_au,price,exchange_rate_au),1)
            zero_sale_price_wini_au = round(no_commission_cost_wini_au/exchange_rate_au/0.82,1)
            five_sale_price_wini_au = round(no_commission_cost_wini_au/0.77/exchange_rate_au,1)
            ten_sale_price_wini_au = round(no_commission_cost_wini_au/0.72/exchange_rate_au,1)
            fifteen_sale_price_wini_au = round(no_commission_cost_wini_au/0.67/exchange_rate_au,1)
            twenty_sale_price_wini_au = round(no_commission_cost_wini_au/0.62/exchange_rate_au,1)
            twentyfive_sale_price_wini_au = round(no_commission_cost_wini_au/0.57/exchange_rate_au,1)
            thirty_sale_price_wini_au = round(no_commission_cost_wini_au/0.52/exchange_rate_au,1)

            first_class_cost_wini_de = round(float(First_Class_Cost(weight,first_class_rate_de)),1)
            first_class_cost_wini_sea_de = round(float(Sea_fee(volume,secondprice.sea['de_fee'])),1)
            second_class_wini_de = second_class_wini_de
            commission_cost_de = round(Commission_Cost(price,commission_rate,exchange_rate_de),1)
            total_cost_wini_de = round(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_de)),
                                            second_class_wini_de*exchange_rate_de,
                                            purchase_price,
                                            commission_cost_de,
                                             )),1)
            total_cost_wini_sea_de = round(float(Total_Cost(first_class_cost_wini_sea_de,
                                            second_class_wini_de*exchange_rate_de,
                                            purchase_price,
                                            commission_cost_de,
                                             )),1)
            no_commission_cost_wini_de = No_Commission_Cost(total_cost_wini_de,commission_cost_de)
            gross_profit_wini_de = round(Gross_Profit(price,total_cost_wini_de,exchange_rate_de),1)
            profit_margins_wini_de = round(Profit_margins(gross_profit_wini_de,price,exchange_rate_de),1)
            zero_sale_price_wini_de = round(no_commission_cost_wini_de/exchange_rate_de/0.82,1)
            five_sale_price_wini_de = round(no_commission_cost_wini_de/0.77/exchange_rate_de,1)
            ten_sale_price_wini_de = round(no_commission_cost_wini_de/0.72/exchange_rate_de,1)
            fifteen_sale_price_wini_de = round(no_commission_cost_wini_de/0.67/exchange_rate_de,1)
            twenty_sale_price_wini_de = round(no_commission_cost_wini_de/0.62/exchange_rate_de,1)
            twentyfive_sale_price_wini_de = round(no_commission_cost_wini_de/0.57/exchange_rate_de,1)
            thirty_sale_price_wini_de = round(no_commission_cost_wini_de/0.52/exchange_rate_de,1)
            no_commission_cost_wini_sea_de = No_Commission_Cost(total_cost_wini_sea_de,commission_cost_de)
            gross_profit_wini_sea_de = round(Gross_Profit(price,total_cost_wini_sea_de,exchange_rate_de),1)
            profit_margins_wini_sea_de = round(Profit_margins(gross_profit_wini_sea_de,price,exchange_rate_de),1)
            zero_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/exchange_rate_de/0.82,1)
            five_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/0.77/exchange_rate_de,1)
            ten_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/0.72/exchange_rate_de,1)
            fifteen_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/0.67/exchange_rate_de,1)
            twenty_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/0.62/exchange_rate_de,1)
            twentyfive_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/0.57/exchange_rate_de,1)
            thirty_sale_price_wini_sea_de = round(no_commission_cost_wini_sea_de/0.52/exchange_rate_de,1)

            result_list= {
                'price':price,
                'weight':weight,
                'purchase_price':purchase_price,
                'commission_cost_us' : commission_cost_us,
                'commission_cost_uk': commission_cost_uk,
                'commission_cost_de': commission_cost_de,
                'commission_cost_au': commission_cost_au,

                'total_cost_wini_us':total_cost_wini_us,
                'second_class_wini_us':second_class_wini_us,
                'second_class_wini_us_rmb': second_class_wini_us_rmb,
                'first_class_cost_wini_us':  first_class_cost_wini_us,
                'gross_profit_wini_us': gross_profit_wini_us,
                'profit_margins_wini_us':profit_margins_wini_us,
                'zero_sale_price_wini_us' :zero_sale_price_wini_us,
                'five_sale_price_wini_us':five_sale_price_wini_us,
                'ten_sale_price_wini_us':ten_sale_price_wini_us,
                'fifteen_sale_price_wini_us':fifteen_sale_price_wini_us,
                'twenty_sale_price_wini_us':twenty_sale_price_wini_us,
                'twentyfive_sale_price_wini_us':twentyfive_sale_price_wini_us,
                'thirty_sale_price_wini_us':thirty_sale_price_wini_us,

                'total_cost_cn_us':total_cost_cn_us,
                'second_class_cn_us':second_class_cn_us,
                'second_class_cn_us_rmb': second_class_cn_us_rmb,
                'first_class_cost_cn_us':  first_class_cost_cn_us,
                'gross_profit_cn_us': gross_profit_cn_us,
                'profit_margins_cn_us':profit_margins_cn_us,
                'zero_sale_price_cn_us' :zero_sale_price_cn_us,
                'five_sale_price_cn_us':five_sale_price_cn_us,
                'ten_sale_price_cn_us':ten_sale_price_cn_us,
                'fifteen_sale_price_cn_us':fifteen_sale_price_cn_us,
                'twenty_sale_price_cn_us':twenty_sale_price_cn_us,
                'twentyfive_sale_price_cn_us':twentyfive_sale_price_cn_us,
                'thirty_sale_price_cn_us':thirty_sale_price_cn_us,

                'total_cost_mulfba_us':total_cost_mulfba_us,
                'second_class_mulfba_us':second_class_mulfba_us,
                'second_class_mulfba_us_rmb':second_class_mulfba_us_rmb,
                'first_class_cost_mulfba_us':  first_class_cost_mulfba_us,
                'gross_profit_mulfba_us': gross_profit_mulfba_us,
                'profit_margins_mulfba_us':profit_margins_mulfba_us,
                'zero_sale_price_mulfba_us' :zero_sale_price_mulfba_us,
                'five_sale_price_mulfba_us':five_sale_price_mulfba_us,
                'ten_sale_price_mulfba_us':ten_sale_price_mulfba_us,
                'fifteen_sale_price_mulfba_us':fifteen_sale_price_mulfba_us,
                'twenty_sale_price_mulfba_us':twenty_sale_price_mulfba_us,
                'twentyfive_sale_price_mulfba_us':twentyfive_sale_price_mulfba_us,
                'thirty_sale_price_mulfba_us':thirty_sale_price_mulfba_us,


                'total_cost_eub_us':total_cost_eub_us,
                'second_class_eub_us':second_class_eub_us,
                'second_class_eub_us_rmb':second_class_eub_us_rmb,
                'first_class_cost_eub_us':  first_class_cost_eub_us,
                'gross_profit_eub_us': gross_profit_eub_us,
                'profit_margins_eub_us':profit_margins_eub_us,
                'zero_sale_price_eub_us' :zero_sale_price_eub_us,
                'five_sale_price_eub_us':five_sale_price_eub_us,
                'ten_sale_price_eub_us':ten_sale_price_eub_us,
                'fifteen_sale_price_eub_us':fifteen_sale_price_eub_us,
                'twenty_sale_price_eub_us':twenty_sale_price_eub_us,
                'twentyfive_sale_price_eub_us':twentyfive_sale_price_eub_us,
                'thirty_sale_price_eub_us':thirty_sale_price_eub_us,

                'total_cost_gz_uk':total_cost_gz_uk,
                'second_class_gz_uk':second_class_gz_uk,
                'second_class_gz_uk_rmb':second_class_gz_uk_rmb,
                'first_class_cost_gz_uk':  first_class_cost_gz_uk,
                'gross_profit_gz_uk': gross_profit_gz_uk,
                'profit_margins_gz_uk':profit_margins_gz_uk,
                'zero_sale_price_gz_uk' :zero_sale_price_gz_uk,
                'five_sale_price_gz_uk':five_sale_price_gz_uk,
                'ten_sale_price_gz_uk':ten_sale_price_gz_uk,
                'fifteen_sale_price_gz_uk':fifteen_sale_price_gz_uk,
                'twenty_sale_price_gz_uk':twenty_sale_price_gz_uk,
                'twentyfive_sale_price_gz_uk':twentyfive_sale_price_gz_uk,
                'thirty_sale_price_gz_uk':thirty_sale_price_gz_uk,

                'total_cost_gz_de':total_cost_gz_de,
                'second_class_gz_de':second_class_gz_de,
                'second_class_gz_de_rmb':second_class_gz_de_rmb,
                'first_class_cost_gz_de':  first_class_cost_gz_de,
                'gross_profit_gz_de': gross_profit_gz_de,
                'profit_margins_gz_de':profit_margins_gz_de,
                'zero_sale_price_gz_de' :zero_sale_price_gz_de,
                'five_sale_price_gz_de':five_sale_price_gz_de,
                'ten_sale_price_gz_de':ten_sale_price_gz_de,
                'fifteen_sale_price_gz_de':fifteen_sale_price_gz_de,
                'twenty_sale_price_gz_de':twenty_sale_price_gz_de,
                'twentyfive_sale_price_gz_de':twentyfive_sale_price_gz_de,
                'thirty_sale_price_gz_de':thirty_sale_price_gz_de,


                'total_cost_gz_au':total_cost_gz_au,
                'second_class_gz_au':second_class_gz_au,
                'second_class_gz_au_rmb':second_class_gz_au_rmb,
                'first_class_cost_gz_au':  first_class_cost_gz_au,
                'gross_profit_gz_au': gross_profit_gz_au,
                'profit_margins_gz_au':profit_margins_gz_au,
                'zero_sale_price_gz_au' :zero_sale_price_gz_au,
                'five_sale_price_gz_au':five_sale_price_gz_au,
                'ten_sale_price_gz_au':ten_sale_price_gz_au,
                'fifteen_sale_price_gz_au':fifteen_sale_price_gz_au,
                'twenty_sale_price_gz_au':twenty_sale_price_gz_au,
                'twentyfive_sale_price_gz_au':twentyfive_sale_price_gz_au,
                'thirty_sale_price_gz_au':thirty_sale_price_gz_au,

                'total_cost_wini_uk':total_cost_wini_uk,
                'second_class_wini_uk':second_class_wini_uk,
                'second_class_wini_uk_rmb': second_class_wini_uk_rmb,
                'first_class_cost_wini_uk':  first_class_cost_wini_uk,
                'first_class_cost_wini_sea_uk':first_class_cost_wini_sea_uk,
                'total_cost_wini_sea_uk':total_cost_wini_sea_uk,
                'gross_profit_wini_uk': gross_profit_wini_uk,
                'profit_margins_wini_uk':profit_margins_wini_uk,
                'zero_sale_price_wini_uk' :zero_sale_price_wini_uk,
                'five_sale_price_wini_uk':five_sale_price_wini_uk,
                'ten_sale_price_wini_uk':ten_sale_price_wini_uk,
                'fifteen_sale_price_wini_uk':fifteen_sale_price_wini_uk,
                'twenty_sale_price_wini_uk':twenty_sale_price_wini_uk,
                'twentyfive_sale_price_wini_uk':twentyfive_sale_price_wini_uk,
                'thirty_sale_price_wini_uk':thirty_sale_price_wini_uk,
                'gross_profit_wini_sea_uk': gross_profit_wini_sea_uk,
                'profit_margins_wini_sea_uk':profit_margins_wini_sea_uk,
                'zero_sale_price_wini_sea_uk' :zero_sale_price_wini_sea_uk,
                'five_sale_price_wini_sea_uk':five_sale_price_wini_sea_uk,
                'ten_sale_price_wini_sea_uk':ten_sale_price_wini_sea_uk,
                'fifteen_sale_price_wini_sea_uk':fifteen_sale_price_wini_sea_uk,
                'twenty_sale_price_wini_sea_uk':twenty_sale_price_wini_sea_uk,
                'twentyfive_sale_price_wini_sea_uk':twentyfive_sale_price_wini_sea_uk,
                'thirty_sale_price_wini_sea_uk':thirty_sale_price_wini_sea_uk,


                'total_cost_wini_au':total_cost_wini_au,
                'second_class_wini_au':second_class_wini_au,
                'second_class_wini_au_rmb': second_class_wini_au_rmb,
                'first_class_cost_wini_au':  first_class_cost_wini_au,
                'gross_profit_wini_au': gross_profit_wini_au,
                'profit_margins_wini_au':profit_margins_wini_au,
                'zero_sale_price_wini_au' :zero_sale_price_wini_au,
                'five_sale_price_wini_au':five_sale_price_wini_au,
                'ten_sale_price_wini_au':ten_sale_price_wini_au,
                'fifteen_sale_price_wini_au':fifteen_sale_price_wini_au,
                'twenty_sale_price_wini_au':twenty_sale_price_wini_au,
                'twentyfive_sale_price_wini_au':twentyfive_sale_price_wini_au,
                'thirty_sale_price_wini_au':thirty_sale_price_wini_au,

                'total_cost_wini_de':total_cost_wini_de,
                'second_class_wini_de':second_class_wini_de,
                'second_class_wini_de_rmb': second_class_wini_de_rmb,
                'first_class_cost_wini_de':  first_class_cost_wini_de,
                'gross_profit_wini_de': gross_profit_wini_de,
                'profit_margins_wini_de':profit_margins_wini_de,
                'zero_sale_price_wini_de' :zero_sale_price_wini_de,
                'five_sale_price_wini_de':five_sale_price_wini_de,
                'ten_sale_price_wini_de':ten_sale_price_wini_de,
                'fifteen_sale_price_wini_de':fifteen_sale_price_wini_de,
                'twenty_sale_price_wini_de':twenty_sale_price_wini_de,
                'twentyfive_sale_price_wini_de':twentyfive_sale_price_wini_de,
                'thirty_sale_price_wini_de':thirty_sale_price_wini_de,

                'total_cost_wini_sea_de':total_cost_wini_sea_de,
                'first_class_cost_wini_sea_de':  first_class_cost_wini_sea_de,
                'gross_profit_wini_sea_de': gross_profit_wini_sea_de,
                'profit_margins_wini_sea_de':profit_margins_wini_sea_de,
                'zero_sale_price_wini_sea_de' :zero_sale_price_wini_sea_de,
                'five_sale_price_wini_sea_de':five_sale_price_wini_sea_de,
                'ten_sale_price_wini_sea_de':ten_sale_price_wini_sea_de,
                'fifteen_sale_price_wini_sea_de':fifteen_sale_price_wini_sea_de,
                'twenty_sale_price_wini_sea_de':twenty_sale_price_wini_sea_de,
                'twentyfive_sale_price_wini_sea_de':twentyfive_sale_price_wini_sea_de,
                'thirty_sale_price_wini_sea_de':thirty_sale_price_wini_sea_de,

                'total_cost_wini_sea_us':total_cost_wini_sea_us,
                'first_class_cost_wini_sea_us':  first_class_cost_wini_sea_us,
                'gross_profit_wini_sea_us': gross_profit_wini_sea_us,
                'profit_margins_wini_sea_us':profit_margins_wini_sea_us,
                'zero_sale_price_wini_sea_us' :zero_sale_price_wini_sea_us,
                'five_sale_price_wini_sea_us':five_sale_price_wini_sea_us,
                'ten_sale_price_wini_sea_us':ten_sale_price_wini_sea_us,
                'fifteen_sale_price_wini_sea_us':fifteen_sale_price_wini_sea_us,
                'twenty_sale_price_wini_sea_us':twenty_sale_price_wini_sea_us,
                'twentyfive_sale_price_wini_sea_us':twentyfive_sale_price_wini_sea_us,
                'thirty_sale_price_wini_sea_us':thirty_sale_price_wini_sea_us,

                }


            return render(request, 'calculator/index.html', {'result_list':result_list})

    else:
        form = AddForm()
    return render(request, 'calculator/summit.html', {'form': form})








































