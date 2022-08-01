# 원화(₩)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000   # 1,000원 당 1달러


# 달러($)에서 엔화(¥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd / 8 * 1000


# 원화(₩) 리스트 및 출력
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

usd_prices = []
jpy_prices = []
start = 0

while start < len(prices):
    usd_prices.append(krw_to_usd(prices[start]))
    jpy_prices.append(usd_to_jpy(usd_prices[start]))
    start += 1

print("미국 화페: " + str(usd_prices))
print("일본 화폐: " + str(jpy_prices))
