def calculate_change(payment, cost):
    diff = payment - cost
    fifty_count = 0
    ten_count = 0
    five_count = 0
    one_count = 0

    fifty_count = diff // 50000
    diff -= fifty_count * 50000
    print("50000원 지폐: {}장".format(fifty_count))
    
    ten_count = diff // 10000
    diff -= ten_count * 10000
    print("10000원 지폐: {}장".format(ten_count))

    five_count = diff // 5000
    diff -= five_count * 5000
    print("5000원 지폐: {}장".format(five_count))

    one_count = diff // 1000
    print("1000원 지폐: {}장".format(one_count))

print(calculate_change(100000, 22000))
    
