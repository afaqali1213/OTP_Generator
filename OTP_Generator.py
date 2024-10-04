import random


def gen_otp(length=6):

    otp = ""

    for i in range(length):
        otp += str(random.randint(0,9))

    return otp


otp = gen_otp(6)
print("your OTP is ",otp)