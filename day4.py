def calculate_fee(course_fee,discount):
    discount_1=(course_fee*discount)/100
    final_fee =(course_fee-discount_1)

    return final_fee
result=calculate_fee(5000,10)
print(result)

