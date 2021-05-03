month = str(input('What is your birthmonth? ')).lower()
day = str(input('What is your birthday? '))

birthmonth = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
              'novembro', 'dezembro']
primaryType = ['ELETRIC', 'FAIRY', 'WATER', 'DARK', 'BUG',
               'GROUND', 'POISON', 'NORMAL', 'FIRE', 'FIGHT', 'GHOST', 'ICE']
birthday = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
secundaryType = ['DARK', 'FLYING', 'FIGHT', 'FAIRY', 'FIRE', 'NORMAL', 'ROCK', 'PSYCHC', 'ICE', 'DRAGON', 'PSYCHC',
                 'FAIRY', 'ICE', 'ROCK', 'WATER', 'GHOST', 'NORMAL', 'ELECTR', 'DRAGON', 'BUG', 'POISON', 'STEEL',
                 'GROUND', 'BUG', 'GRASS', 'FLYING', 'POISON', 'WATER', 'FAIRY', 'ROCK', 'FIGHT']

# Função que percorre a lista do mês e encontra o tipo primario
for i in range(len(birthmonth)):
    if birthmonth[i] == month:
        posMonth = i
# print(primaryType[posMonth])

# Função que percorre a lista do dia e encontra o tipo secundario

for x in range(len(birthday)):
    if birthday[x] == day:
        posDay = x
# print(secundaryType[posDay])


print('Your primary type of pokémon is {} and secundary is {}'.format(
    primaryType[posMonth], secundaryType[posDay]))
