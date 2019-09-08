market = {"dairy": ["yogurt", "cheese"], "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
print(market)

market["candies"] = ["mars", 'kinder', 'twix']




fr=set(market["fruits"])
market["fruits"]=list(fr)
market["fruits"].sort()
print(market)
