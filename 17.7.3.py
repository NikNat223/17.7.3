per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете внести:"))
deposit = []
deposit.append(int(per_cent['ТКБ'] * money / 100))
deposit.append(int(per_cent['СКБ'] * money / 100))
deposit.append(int(per_cent['ВТБ'] * money / 100))
deposit.append(int(per_cent['СБЕР'] * money / 100))
print("Проценты, которые вы можете заработать:"+str(deposit))
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать:"+str(max_deposit))










