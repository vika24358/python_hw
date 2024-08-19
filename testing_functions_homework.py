def calculate_discount(price: int | float, discount_percent: int) -> int | float:
    if price < 0:
        raise ValueError('Too Low Price')
    if discount_percent > 100:
        raise ValueError('Too High Discount')
    if discount_percent < 0:
        raise ValueError('Too Low Discount')
    discount_amount = price * discount_percent / 100
    price_after_discount = price - discount_amount
    return price_after_discount

