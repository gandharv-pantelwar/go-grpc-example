numberOfIngredients = int(raw_input(""))
# print(numberOfIngredients)

if numberOfIngredients < 1 or numberOfIngredients > 10000000:
    print("Provide number of ingredients 1 <= N <= 1000000")
    exit(0)


ingredientsRequired = list(map(int, raw_input().split()))[:numberOfIngredients]
# print(ingredientsRequired)

ingredientsAvailable = list(map(int, raw_input().split()))[
    :numberOfIngredients]
# print(ingredientsAvailable)


if len(ingredientsRequired) != numberOfIngredients or len(ingredientsAvailable) != numberOfIngredients:
    print("Invalid numbers")
    exit(0)


tempArray = []
for i in range(numberOfIngredients):
    if ingredientsRequired[i] == 0:
        val = 0
    else:
        val = ingredientsAvailable[i]/ingredientsRequired[i]
    tempArray.append(val)


print(min(tempArray))