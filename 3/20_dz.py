k = 'ноутбук'
eng = "aeioulnstrdgbcmpfhvwykjxqz"
rus = "авеинорстдклмпубгёьяйыжзхцчшэюфщъ"
list_eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
result = 0
if k[0].lower() in eng:
    for letter in k:
        for key, value in list_eng.items():
            if letter.upper() in value:
                result += key
elif k[0].lower() in rus:
    for letter in k:
        for key, value in list_rus.items():
            if letter.upper() in value:
                result += key
print(result)