coffee_price = 3.50
muffin_price = 2.10
water_price = 1.05
coffee_qty=2
muffin_qty=3
water_qty=4

#CALCULATE
coffee_total=coffee_price * coffee_qty
muffin_total=muffin_price * muffin_qty
water_total=water_price * water_qty

sub_total=coffee_total + muffin_total + water_total
tax=sub_total * 0.06
total=sub_total + tax

print("========== RECEIPT ==========\n"
      "item\tprice\tqty\ttotal\n"
      f"Coffee\t{coffee_price}\t{coffee_qty}\t{coffee_total}\n"
      f"Muffin\t{muffin_price}\t{muffin_qty}\t{muffin_total}\n"
      f"Water\t{water_price}\t{water_qty}\t{water_total}\n"
      f"sub_total\t\t\t{sub_total}\n"
      f"Tax (6%)\t\t\t{tax}\n"
      f"Total\t\t\t\t{total}\n"
      "======================"
)
