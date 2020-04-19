numberOfTestCases = int(raw_input(""))
# print(numberOfIngredients)

if numberOfTestCases < 1 or numberOfTestCases > 100000:
    print("Provide number of cases 1 <= T <= 100000")
    exit(0)

team2map = {}
array = []

def arrangeTeam(team1, team2):
    global team2map
    orderedTeam = team1[:]
    # found = False
    team1 = sorted(team1)
    team2 = sorted(team2)
    print(team1)
    print(team2)
    print("\n")
    # return orderedTeam
    for i in range(len(team2)):
        # found = False
        # potential = (i, team1[i])
        print(team1)
        print(team2)
        print("\n")
    
        for j in range(i, len(team1)):
            if team2[i] < team1[j]:
                # if team2[i] >= potential[1] and potential[1] <= team1[j]:
                    temp = team1[i]
                    team1[i] = team1[j]# team1[j]
                    team1[j] = temp
                    break
            # print(team2[i], team1[j], potential[1])
        
        # print("\n")
        # print("potential old", potential[0], i)
        # if potential[0] == i: # nothing found
        #     for j in range(i, len(team1)):
        #         if team2[i] > team1[j] and team1[j] < potential[1]:
        #             potential = (j, team1[j])
        # print("potential new", potential[0], i)
        # temp = team1[i]
        # team1[i] = potential[1]# team1[j]
        # team1[potential[0]] = temp
        # print("\n")
        # print(team1)
        # print(team2)
        # break 
    print("\n")
    print(team1)
    print(team2)
    count = 0
    for i in range(len(team1)):
        if team1[i] > team2[i]:
            count+=1

    return (count)
    # for p1 in team1:
    #     max = 0
    #     for p2 in team2:
    #         if p1 > p2:
    #             found = True
    #             temp
    #             orderedTeam[team2.index(p2)] = p1
    #         if found:
    #             break
    #     if found:
    #         break

for i in range(numberOfTestCases):
    numberOfPlayers = int(raw_input(""))
    # print(numberOfIngredients)
    if numberOfPlayers < 1 or numberOfPlayers > 100000:
        print("Provide number of players 1 <= N <= 100000")
        exit(0)

    team1 = list(map(int, raw_input().split()))[:numberOfPlayers]
    team2 = list(map(int, raw_input().split()))[:numberOfPlayers]

    if len(team1) != numberOfPlayers or len(team2) != numberOfPlayers:
        print("Invalid numbers")
        exit(0)

    for i in range(len(team2)):
        team2map[i] = team2[i]

    orderTeam1 = arrangeTeam(team1, team2)
    # print("orderTeamCount", orderTeam1)
    array.append(orderTeam1)

for val in array:
    print (val)