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

bach = ['1.02a', '1.02b', '1.03', '1.07', '1.08', '1.09', '1.11', '1.12', '1.15', '1.16', '2.02', '2.03', '2.05a', '2.05b']
design = ['1.04', '1.10', '1.13', '1.14', '2.01', '2.08', '2.09']
pageant = ['1.05', '1.06', '1.17', '1.18', '2.04', '2.06', '2.07a', '2.07b', '2.07c']


cast = {
    'Camille': ['M', 'T', 'Th', 'F'],
    'Isabel': ['M', 'Th', 'F'],
    'Roselyn': ['M', 'T', 'Th', 'F'],
    'Shandeigh': ['M', 'T'],
    'Jett': ['M', 'T', 'Th', 'F'],
    'Bryant': ['M', 'F'],
    'Zac': ['T', 'Th', 'F'],
    'Nate': ['M', 'T', 'Th', 'F'],
    'Megan': ['M', 'T', 'Th', 'F'],
    'Seth': ['M', 'T', 'Th', 'F'],
    'Zeya': ['M', 'T', 'Th'],
    'Rocco': ['M', 'Th', 'F'],
    'Josue': ['T', 'F'],
    'Caleb': [],
    'Figgy': ['M', 'T', 'Th', 'F'],
    'Isaiah': ['M', 'T', 'Th', 'F'],
    'Joy': ['M'],
    'Jessica': ['M', 'T', 'Th', 'F'],
    'Analisa': ['T', 'Th', 'F'],
    'Britney': [],
    'Jackie': ['T', 'Th', 'F'],
    'Andru': ['T', 'Th', 'F'],
    'Von': ['M', 'Th', 'F'],
    'Young Isabel': ['T', 'F'],
    'Michaela': ['M', 'F'],
    'Ethan': ['M', 'T', 'Th', 'F'],
    'Jehlia': ['M', 'T', 'Th', 'F'],
    'Natalie': ['M', 'F'],
    'Ally': ['M', 'F'],
    'Daisy': ['M', 'T', 'Th', 'F'],
    'Lea Michele': ['M', 'T', 'Th', 'F'],
    'Christina': ['M', 'T', 'Th'],
    'Autumn': ['F'],
    'Meesh': ['M', 'Th', 'F'],
    'Sharon': [],
    'Kimiko': ['M', 'F']
}

def select_day():
    while True:
        day = input('Select a day (M/T/Th/F): ')
        if (day=='M' or day=='T' or day=='Th' or day=='F'):
            return day
        else:
            print('Select a specified day')

def all_scenes_exist(line):
    invalid_scenes = []
    # validate each scene in input
    for s in line.split():
        if not (s in scenes):
            print(s + " is not a valid scene")
            invalid_scenes.append(s)
    # return True if all scenes valid, False otherwise
    if len(invalid_scenes)>0: return False
    else: return True

def select_scenes():
    while True:
        line = input('Choose 1 or more scenes (separated by space): ')
        # add "bachelorette", "fashion", and "pageant" options to print all scene availabilities for that day
        if line=='all':
            return scenes.keys()
        elif line=='bach':
            return bach
        elif line=='design':
            return design
        elif line=='pageant':
            return pageant
        elif all_scenes_exist(line):
            return line.split()

def print_availabilities(scene, available, unavailable):
    print("\nScene " + scene)
    print("  available: " + ", ".join(available))
    print("  unavailable: " + ", ".join(unavailable))

def verify_one(scene, day):
    available = []
    unavailable = []
    # populate available and unavailable ppl lists for that day
    for a in scenes[scene]:
        if day in cast[a]:
            available.append(a)
        else: unavailable.append(a)
    # prints results
    print_availabilities(scene, available, unavailable)

def verify_all():
    day = select_day()
    selected_scenes = select_scenes()
    # print availabilities for each scene
    for s in selected_scenes:
        verify_one(s, day)
    print()

if __name__ == '__main__':
    verify_all()