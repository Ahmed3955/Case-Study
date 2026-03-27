# 1. Closure for discount
def make_discount(discount_pct):
    def apply_discount(price):
        return price - (price * discount_pct / 100)
    return apply_discount


gold_discount = make_discount(30)
silver_discount = make_discount(20)
regular_discount = make_discount(5)


prices = [1000, 2000, 3000, 4000, 5000]

print("Original vs Discounted Prices:")
for p in prices:
    print(f"Price: {p}, Gold: {gold_discount(p)}, Silver: {silver_discount(p)}, Regular: {regular_discount(p)}")


def make_tax_calculator(tax_rate):
    def apply_tax(price):
        return price + (price * tax_rate / 100)
    return apply_tax

gst_18 = make_tax_calculator(18)



print("\nGold Discount + 18% GST:")
for p in prices:
    discounted = gold_discount(p)
    final_price = gst_18(discounted)
    print(f"Original: {p}, After Discount: {discounted}, Final with GST: {final_price}")

# print("\nSilver Discount + 18% GST:")
# for p in prices:
#     discounted = silver_discount(p)
#     final_price = gst_18(discounted)
#     print(f"Original: {p}, After Discount: {discounted}, Final with GST: {final_price}")

# print("\nRegular Discount + 18% GST:")
# for p in prices:
#     discounted = regular_discount(p)
#     final_price = gst_18(discounted)
#     print(f"Original: {p}, After Discount: {discounted}, Final with GST: {final_price}")