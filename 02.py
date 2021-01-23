# temp = float(input("enter temperature ('C) : "))
# F = temp * 9 / 5 + 32
# print( F , "℉")


# x= 0
# while x < 10:
#     print("x<10")
#     # x+=1
    # break #中斷loop



# control minecraft
#teach "https://www.instructables.com/id/Python-coding-for-Minecraft/"

# from mine import *
import time

# mc = Minecraft()
# while True: 
#     pos = mc.player.getPos()
#     mc.setBlock(pos.x, pos.y, pos.z, 46, 1)
#     time.sleep(1)


passw = input("set your password: ")
print("your password is set")
times = 3
while times > 0:
    repass = input("please enter your password: ")
    if repass == passw:
        print("login successful")
        times=3
        break
    else:
        times-=1
        if times != 0:
            print("password is wrong, please enter again")
            print("you remain ",times, " times")
        else:
            print("account is locked, you can't enter anymore")
    time.sleep(0.5)
