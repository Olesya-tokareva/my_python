s = "У лукоморья 123 дуб зеленый 456"
print(s.index('я'))
print(s.count('у'))
p=str(s.isalpha())
if p=='False':
    print(s.upper())
d=len(s)
if d>4:
    print(s.lower())
print(s.replace(str(s[0]),'О'))

