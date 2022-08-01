UNMI_2016 = 1_100_000_000
bank_rate = 0.12
prize = 50_000_000
started_year = 1988
count = 1

while started_year < 2016:
    prize = prize * (1 + bank_rate)
    started_year += 1

if prize > UNMI_2016:
    print("{}원 차이로 동일 아저씨 말이 맞습니다.".format(int(prize - UNMI_2016)))
else:
    print("{}원 차이로 미란 아주머니 말이 맞습니다.".format(int(UNMI_2016 - prize)))