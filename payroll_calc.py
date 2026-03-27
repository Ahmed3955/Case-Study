def cal_gross_pay(hours_worked,hourly_rate):
    if hours_worked <=40:
        return hours_worked*hourly_rate
    else:
        regular=40*hourly_rate
        overtime=(hours_worked - 40) *hourly_rate*1.5
        return regular+overtime
    
def tax(gross):
    if gross<=20000:
        return 0
    elif gross>20000 and gross<=50000:
        return gross*0.10
    else:
        return gross*0.20
    
def pf(gross):
    if gross>=15000:
        return gross*0.12
    else:
        return 0
    

def pay_slip(emp_name,worked,rate):
    gross= cal_gross_pay(worked,rate)
    tax_pay=tax(gross)
    pf_pay=pf(gross)
    net=gross-tax_pay-pf_pay


    print(f"---Pay slip for {emp_name} ---")
    print(f"Hours worked: {worked}")
    print(f"Houlry Rate:{rate}")
    print(f"Gross Pay:{gross:.2f}")
    print(f"tax Deduction:{tax_pay:.2f}")
    print(f"pf Contribution:{pf_pay:.2f}")
    print(f"Net Pay:{net:.2f}")
    print("-------------------------\n")



pay_slip("ahmed",56,500)



