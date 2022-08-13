import re

with open("actual_data.txt") as file:
    pattern = r"[0-9]+"
    SumNum = list()
    total_sum = 0
    for line in file:
        data = line.rstrip()
        Nums = re.findall(pattern, data)
        for i in Nums:
            total_sum = total_sum + int(i)
        SumNum.append(total_sum)

    for i in SumNum:
        total_sum = total_sum + int(i)

    print(i)    # 234426