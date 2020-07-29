list_words=['Java','python','hello','redivider', 'deified', 'civic', 'radar', 'level', 'rotor', 'kayak', 'reviver', 'racecar', 'madam']

print(list(filter(lambda x: x==x[::-1],list_words)))