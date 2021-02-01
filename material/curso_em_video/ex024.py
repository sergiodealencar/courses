city = input('Diga o nome de uma cidade: ')
city_s = city.split()
print(city_s)
print('Essa cidade começa com a palavra "Santo"?')
print('Santo' in city_s[0])


#print(city.find('Santo'))
