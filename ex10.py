# Write a program that reads how much money a person has in their wallet and shows how many dollars they can buy. Assume the exchange rate is US$1.00 = R$3.27.

exchange_rate = 3.27


amount_in_reais = float(input("Enter the amount of money in your wallet (in R$): "))


amount_in_dollars = amount_in_reais / exchange_rate


print(f"With R${amount_in_reais:.2f}, you can buy US${amount_in_dollars:.2f}.")