# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#What is the total of all the name scores in the file?

with open('resources/p022_names.txt') as f:
    content = f.read()
    names = content.split(',')
    names.sort()
    total = 0
    for i,name in enumerate(names):
        name = name.strip('"')
        namevalue = 0
        for c in name:
            namevalue += ord(c) - ord('A') + 1
        total += namevalue * (i+1)
        print(name, ',', str(namevalue), ' * ', str(i+1), ' = ', str(namevalue * (i+1)), ',', str(total))
    print(total)