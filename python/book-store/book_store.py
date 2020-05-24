def total(basket):
    if len(basket) == len(unique_list(basket)):
        if len(basket) == 0:
            return 0
        if len(basket) == 1:
            checkout_price = sum(800 * 1.00 for i in basket)
        if len(basket) == 2:
            checkout_price = sum(800 * 0.95 for i in basket)
        if len(basket) == 3:
            checkout_price = sum(800 * 0.90 for i in basket)
        if len(basket) == 4:
            checkout_price = sum(800 * 0.80 for i in basket)
        if len(basket) == 5:
            checkout_price = sum(800 * 0.75 for i in basket)
    else:
        checkout_price = sum(800 for i in basket)
    return checkout_price



def unique_list(basket):
    list_set = set(basket)
    return list(list_set)