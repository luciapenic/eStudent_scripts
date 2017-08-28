import sys
# ulaz su dvije datoteke dohvacene iz baze podataka
# prva datoteka ima popis svih prijavljenih te timove slozene po prioritetima
    # OBLIK: ime,prezime,tim1,tim2,tim3 - PRETPOSTAVKA da tako izgleda

# druga datoteka su timovi
    # OBLIK: tim,broj clanova,popis_svih_prijavljenih_ljudi
RESULTS = {}
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
        members = line.strip().split(',')[1]
        priority_of_members = line.strip().split(',')[2:]

        teams_priority[team] = priority_of_members
        number_of_members[team] = members


print(candidates)

added = True

for priority in range(3): # prioritet ide od 0 do 2, 0 je najvisi prioritet
    for candidate in candidates.keys():
        team = candidates[candidate][priority]
        limit = number_of_members[team]
        if candidate in teams_priority[:limit]:
            RESULTS[team].append(candidate)
            number_of_members[team] -= 1
            for i in candidates[candidate]:
                if candidate in teams_priority[i]:
                    teams_priority[i].remove(candidate)
                    added = True

    if added is False:
        if priority == 2:
            continue
        else:
            priority += 1

    added = False
