scenes = {
    '1.01': ['Isabel', 'Shandeigh', 'Jett', 'Roselyn', 'Camille'],
    '1.02a': ['Camille', 'Bryant', 'Megan', 'Jett'],
    '1.02b': ['Jett', 'Camille'],
    '1.03': ['Zac', 'Bryant'],
    '1.04': ['Isabel', 'Isaiah', 'Jett', 'Shandeigh'],
    '1.05': ['Isabel', 'Roselyn'],
    '1.06': ['Roselyn', 'Camille', 'Isabel'],
    '1.07': ['Caleb', 'Josue', 'Camille', 'Nate', 'Rocco'],
    '1.08': ['Camille', 'Josue', 'Figgy'],
    '1.09': ['Bryant', 'Camille'],
    '1.10': ['Isabel', 'Isaiah', 'Jessica', 'Joy', 'Analisa', 'Britney', 'Jackie', 'Andru', 'Von'],
    '1.11': ['Caleb', 'Nate', 'Seth', 'Zeya'],
    '1.12': ['Camille', 'Roselyn', 'Isabel', 'Bryant'],
    '1.13': ['Isabel', 'Isaiah'],
    '1.14': ['Isaiah', 'Isabel', 'Young Isabel', 'Shandeigh', 'Jett'],
    '1.15': ['Shandeigh', 'Nate', 'Camille', 'Jett', 'Bryant'],
    '1.16': ['Camille', 'Bryant'],
    '1.17': ['Roselyn', 'Shandeigh', 'Jett'],
    '1.18': ['Roselyn'],
    '2.01': ['Isaiah', 'Isabel', 'Joy', 'Jessica', 'Analisa', 'Britney', 'Jackie', 'Jett', 'Shandeigh'],
    '2.02': ['Isabel', 'Roselyn', 'Bryant'],
    '2.03': ['Roselyn', 'Bryant', 'Jett', 'Shandeigh', 'Isabel'],
    '2.04': ['Roselyn', 'Camille', 'Isabel', 'Bryant'],
    '2.05a': ['Camille', 'Isabel', 'Roselyn', 'Bryant'],
    '2.05b': ['Zac', 'Bryant'],
    '2.06': ['Roselyn', 'Camille', 'Isabel', 'Bryant', 'Shandeigh', 'Jett'],
    '2.07a': ['Christina', 'Autumn', 'Natalie', 'Ally', 'Daisy', 'Lea Michele', 'Meesh', 'Sharon', 'Kimiko', 'Roselyn', 'Michaela', 'Ethan', 'Jehlia'],
    '2.07b': ['Isabel', 'Rocco', 'Camille'],
    '2.07c': ['Ethan', 'Michaela', 'Jehlia', 'Shandeigh', 'Roselyn', 'Camille', 'Isabel', 'Jett', 'Bryant', 'Rocco', 'Natalie'],
    '2.08': ['Isabel', 'Rocco', 'Natalie', 'Camille', 'Roselyn', 'Jett', 'Shandeigh'],
    '2.09': ['Isabel', 'Camille', 'Shandeigh', 'Jett', 'Roselyn']
}

def select_day():
    while True:
        day = input('Select a day (M/T/Th/F): ')
        if (day=='M' or day=='T' or day=='Th' or day=='F'):
            return day
        else:
            print('Select a specified day')

def select_scenes():
    line = input('Choose 1 or more scenes (separated by space): ')
    for s in line.split():
        if s


def verify():
    day = select_day()
    scenes = select_scenes()

if __name__ == '__main__':
    verify()