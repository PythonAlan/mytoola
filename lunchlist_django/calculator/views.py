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
    elif weight > 85 and weight < 171 :
        second_class_wini_us = secondprice.wini_us[170]
    elif weight > 170 and weight < 256:
        second_class_wini_us = secondprice.wini_us[255]
    elif weight > 256 and weight < 454:
        second_class_wini_us = secondprice.wini_us[453]
    elif weight > 453 and weight < 908:
        second_class_wini_us = secondprice.wini_us[907]
    elif weight > 907 and weight < 1815:
        second_class_wini_us = secondprice.wini_us[1814]
    elif weight > 1814 and weight < 4082:
        second_class_wini_us = secondprice.wini_us[4082]
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
        eub_us = float(secondprice.eub_us['weight_rate_below_200']*secondprice.eub_us['as_last_weight']+secondprice.eub_us['Order Handling'])
    elif weight >secondprice.eub_us['as_last_weight'] and weight < 200:
        eub_us = float(secondprice.eub_us['weight_rate_below_200']*weight+secondprice.eub_us['Order Handling'])
    else:
        eub_us = float(secondprice.eub_us['weight_rate_up_200']*weight+secondprice.eub_us['Order Handling'])
    return eub_us




def summit(request):
    if request.method == 'POST':

        form = AddForm(request.POST)

        if form.is_valid():
            price = format(form.cleaned_data['price'],'.1f')
            weight = form.cleaned_data['weight']
            purchase_price = form.cleaned_data['purchase_price']

            first_class_rate_us = 0.030
            first_class_rate_uk = 0.034
            first_class_rate_de = 0.035
            first_class_rate_au = 0.027
            exchange_rate_us = 6.60
            exchange_rate_uk= 8.62
            exchange_rate_de = 7.05
            exchange_rate_au = 5.03

            second_class_wini_us = Weight_range_wini_us(weight)
            second_class_wini_us_rmb = Weight_range_wini_us(weight)*exchange_rate_us
            second_class_wini_uk = 4
            second_class_wini_uk_rmb = 8
            second_class_wini_de = 4
            second_class_wini_de_rmb = 8
            second_class_wini_au = 4
            second_class_wini_au_rmb = 8
            second_class_cn_us = Weight_range_cn_us(weight)
            second_class_cn_us_rmb = Weight_range_cn_us(weight)*exchange_rate_us
            second_class_mulfba_us = Weight_range_mul_fba_us(weight)
            second_class_mulfba_us_rmb = Weight_range_mul_fba_us(weight)*exchange_rate_us
            second_class_eub_us = Weight_range_eub_us(weight)/exchange_rate_us
            second_class_eub_us_rmb = Weight_range_eub_us(weight)

            commission_rate = 0.18




            first_class_cost_wini_us = format(float(First_Class_Cost(weight,first_class_rate_us)),'.1f')
            second_class_wini_us = second_class_wini_us
            second_class_wini_us_rmb = second_class_wini_us_rmb
            commission_cost_us = format(Commission_Cost(price,commission_rate,exchange_rate_us),'.1f')
            total_cost_wini_us = format(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_us)),
                                            second_class_wini_us_rmb,
                                            purchase_price,
                                            commission_cost_us,
                                             )),'.1f')
            no_commission_cost = No_Commission_Cost(total_cost_wini_us,commission_cost_us)
            gross_profit_wini_us = format(Gross_Profit(price,total_cost_wini_us,exchange_rate_us),'.1f')
            profit_margins_wini_us = format(Profit_margins(gross_profit_wini_us,price,exchange_rate_us),'.1f')
            zero_sale_price_wini_us = format(no_commission_cost/exchange_rate_us/0.82,'.1f')
            five_sale_price_wini_us = format(no_commission_cost/0.77/exchange_rate_us,'.1f')
            ten_sale_price_wini_us = format(no_commission_cost/0.72/exchange_rate_us,'.1f')
            fifteen_sale_price_wini_us = format(no_commission_cost/0.67/exchange_rate_us,'.1f')
            twenty_sale_price_wini_us = format(no_commission_cost/0.62/exchange_rate_us,'.1f')
            twentyfive_sale_price_wini_us = format(no_commission_cost/0.57/exchange_rate_us,'.1f')
            thirty_sale_price_wini_us = format(no_commission_cost/0.52/exchange_rate_us,'.1f')


            first_class_cost_cn_us = format(float(First_Class_Cost(weight,first_class_rate_us)),'.1f')
            second_class_cn_us = format(float(second_class_cn_us),'.1f')
            second_class_cn_us_rmb = Weight_range_cn_us(weight)*exchange_rate_us
            commission_cost_us = format(Commission_Cost(price,commission_rate,exchange_rate_us),'.1f')
            total_cost_cn_us = format(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_us)),
                                            second_class_cn_us_rmb,
                                            purchase_price,
                                            commission_cost_us,
                                             )),'.1f')
            no_commission_cost = No_Commission_Cost(total_cost_cn_us,commission_cost_us)
            gross_profit_cn_us = format(Gross_Profit(price,total_cost_cn_us,exchange_rate_us),'.1f')
            profit_margins_cn_us = format(Profit_margins(gross_profit_cn_us,price,exchange_rate_us),'.1f')
            zero_sale_price_cn_us = format(no_commission_cost/exchange_rate_us/0.82,'.1f')
            five_sale_price_cn_us = format(no_commission_cost/0.77/exchange_rate_us,'.1f')
            ten_sale_price_cn_us = format(no_commission_cost/0.72/exchange_rate_us,'.1f')
            fifteen_sale_price_cn_us = format(no_commission_cost/0.67/exchange_rate_us,'.1f')
            twenty_sale_price_cn_us = format(no_commission_cost/0.62/exchange_rate_us,'.1f')
            twentyfive_sale_price_cn_us = format(no_commission_cost/0.57/exchange_rate_us,'.1f')
            thirty_sale_price_cn_us = format(no_commission_cost/0.52/exchange_rate_us,'.1f')



            first_class_cost_mulfba_us = format(float(First_Class_Cost(weight,first_class_rate_us)),'.1f')
            second_class_mulfba_us = format(float(second_class_mulfba_us),'.1f')
            second_class_mulfba_us_rmb = Weight_range_mul_fba_us(weight)*exchange_rate_us
            commission_cost_us = format(Commission_Cost(price,commission_rate,exchange_rate_us),'.1f')
            total_cost_mulfba_us = format(float(Total_Cost(float(First_Class_Cost(weight,first_class_rate_us)),
                                            second_class_mulfba_us_rmb,
                                            purchase_price,
                                            commission_cost_us,
                                             )),'.1f')
            no_commission_cost = No_Commission_Cost(total_cost_mulfba_us,commission_cost_us)
            gross_profit_mulfba_us = format(Gross_Profit(price,total_cost_mulfba_us,exchange_rate_us),'.1f')
            profit_margins_mulfba_us = format(Profit_margins(gross_profit_mulfba_us,price,exchange_rate_us),'.1f')
            zero_sale_price_mulfba_us = format(no_commission_cost/exchange_rate_us/0.82,'.1f')
            five_sale_price_mulfba_us = format(no_commission_cost/0.77/exchange_rate_us,'.1f')
            ten_sale_price_mulfba_us = format(no_commission_cost/0.72/exchange_rate_us,'.1f')
            fifteen_sale_price_mulfba_us = format(no_commission_cost/0.67/exchange_rate_us,'.1f')
            twenty_sale_price_mulfba_us = format(no_commission_cost/0.62/exchange_rate_us,'.1f')
            twentyfive_sale_price_mulfba_us = format(no_commission_cost/0.57/exchange_rate_us,'.1f')
            thirty_sale_price_mulfba_us = format(no_commission_cost/0.52/exchange_rate_us,'.1f')






            first_class_cost_eub_us = 0
            second_class_eub_us = format(float(second_class_eub_us),'.1f')
            second_class_eub_us_rmb = Weight_range_eub_us(weight)
            commission_cost_us = format(Commission_Cost(price,commission_rate,exchange_rate_us),'.1f')
            total_cost_eub_us = format(float(Total_Cost(first_class_cost_eub_us,
                                            second_class_eub_us_rmb,
                                            purchase_price,
                                            commission_cost_us,
                                             )),'.1f')
            no_commission_cost = No_Commission_Cost(total_cost_eub_us,commission_cost_us)
            gross_profit_eub_us = format(Gross_Profit(price,total_cost_eub_us,exchange_rate_us),'.1f')
            profit_margins_eub_us = format(Profit_margins(gross_profit_eub_us,price,exchange_rate_us),'.1f')
            zero_sale_price_eub_us = format(no_commission_cost/exchange_rate_us/0.82,'.1f')
            five_sale_price_eub_us = format(no_commission_cost/0.77/exchange_rate_us,'.1f')
            ten_sale_price_eub_us = format(no_commission_cost/0.72/exchange_rate_us,'.1f')
            fifteen_sale_price_eub_us = format(no_commission_cost/0.67/exchange_rate_us,'.1f')
            twenty_sale_price_eub_us = format(no_commission_cost/0.62/exchange_rate_us,'.1f')
            twentyfive_sale_price_eub_us = format(no_commission_cost/0.57/exchange_rate_us,'.1f')
            thirty_sale_price_eub_us = format(no_commission_cost/0.52/exchange_rate_us,'.1f')




            result_list= {
                'price':price,
                'weight':weight,
                'purchase_price':purchase_price,
                'commission_cost_us' : commission_cost_us,



                'total_cost_wini_us':total_cost_wini_us,
                'second_class_wini_us':second_class_wini_us,
                'second_class_wini_us_rmb':second_class_wini_us_rmb,
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
                'second_class_cn_us_rmb':second_class_cn_us_rmb,
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








            }


            return render(request, 'calculator/index.html', {'result_list':result_list})

    else:
        form = AddForm()
    return render(request, 'calculator/summit.html', {'form': form})







