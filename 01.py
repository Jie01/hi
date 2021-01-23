# height = float(input("enter your height(m):"))
# weight = float(input("enter your weight(kg):"))

# def BMI():
#     value = weight/(height*height)
#     print(value)
# BMI()

data = []
count = 0
with open('reviews.txt' , "r") as f:
    for line in f:
        data.append(line)
        count+=1
        # if count % 1000 == 0: #1000 的倍數才print
        #     print(len(data))


# 資料平均長度
# lsum = 0
# for d in data:
#     lsum += len(d)
# lsum =  lsum/len(data)
# print(lsum)