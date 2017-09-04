import sys
# ulaz su dvije datoteke dohvacene iz baze podataka
# prva datoteka ima popis svih prijavljenih te timove slozene po prioritetima
    # OBLIK: ime,prezime,tim1,tim2,tim3 - PRETPOSTAVKA da tako izgleda

# druga datoteka su timovi
    # OBLIK: tim,broj clanova,popis_svih_prijavljenih_ljudi # razmisliti o boljem nacinu
    # mozda koristiti id umisto imena? izbjegli bi problem sa dva imena/dva prezimena i situaciju kada se osobe isto zovu ?
    # izbjegli bi problem typo-a od strane voditelja - napravili bi dohvat id-a iz baze i odmah vidjeli gdje se potkrala greska
    # izbjegli bi problem velikog i malog slova
RESULTS = {
    'IT':[],
    'LJP':[],
    'IC':[]
}

candidates = {}
priority_of_teams = []
teams_priority = {}
number_of_members = {}


with open(sys.argv[1]) as kandidati:
    for line in kandidati:

        name = line.strip().split(',')[0]
        lname = line.strip().split(',')[1] # sta ako osoba ima 2 imena ili 2 prezimena?
        priority_of_teams = line.strip().split(',')[2:]
        candidates[name + '_' + lname] = priority_of_teams

with open(sys.argv[2]) as timovi:
    for line in timovi:

        team = line.strip().split(',')[0]
        limit_members = line.strip().split(',')[1]
        priority_of_members = line.strip().split(',')[2:]

        teams_priority[team] = priority_of_members
        number_of_members[team] = limit_members


#print(candidates)

added = False
priority = 0
number_of_loops = 0

while priority < 4: # prioritet ide od 0 do 2, 0 je najvisi prioritet
    added = False
    for candidate in candidates.keys():
        number_of_loops +=1
        print(number_of_loops)
        try:
            team = candidates[candidate][priority]
            limit = number_of_members[team]
        except IndexError:
            continue
        if candidate in teams_priority[team][0:int(limit)]:
            RESULTS[team].append(candidate)
            number_of_members[team] = str(int(number_of_members[team]) -1)

            #makni kandidata iz lista svih timova!
            for team in teams_priority:
                if candidate in teams_priority[team]:
                    teams_priority[team].remove(candidate)
            added = True

    if added is False:
        if priority == 2:
            break
        else:
            priority += 1
            print(priority)

    #added = False

print(RESULTS)
