'''
도둑은 보물들이 있는 창고에 침입하였다.
도둑은 최대 30kg까지 짐을 담아갈 수 있다.

물건의 개수 N 그리고 물건 별 무게(W)와 가격(P)가 주어질 때, 
어떤 물건을 담아야 도둑이 최대 이득을 볼 수 있을 지 구하라


물건 1 : 무게 = 5kg, 값 = 50만원
물건 2 : 무게 = 10kg, 값 = 60만원
물건 3 : 무게 = 20kg, 값 = 140만원
'''




n = 3
target = 30     # kanpsack 30 kg
things = [(5, 50), (10, 60), (20, 140)]
# kg당 가격으로 내림차순 정렬
things.sort(key=lambda x:(x[1]/x[0]), reverse=True)

sum = 0

for kg, price in things:
    per_price = price / kg
    if target < kg:
        sum += target * per_price
        break
    sum += price
    target -= kg
print(int(sum))