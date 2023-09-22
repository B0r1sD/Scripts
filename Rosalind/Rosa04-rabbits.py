#!/usr/bin/python3

n = int(input("Months: "))
k = int(input("rabbit pair litter: "))

def rabbit_pairs(months, litterpair):
    gen = 1
    total = 1
    counter = 1
    all_rabbits = {1:0}     #example after 6 months: repr_rabbits = {1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:1, 8:1}
    unrepr = 0
    repr = 0
    while gen < months + 1:
        if gen != 1:
            print(f"################# Gen {gen}, total {total} ################ ")
            for rabbit,value in list(all_rabbits.items()):
                if value == 0:
                    all_rabbits[rabbit] = 1
                    unrepr += 1
                    counter += 1
                if value == 1:
                    for i in range(1,k+1):
                        total += 1
                        all_rabbits[total]=0
                        repr += 1
                        counter += 1   
                    counter += 1
            #print(f"There are {unrepr} unrepr + {repr} repr = {unrepr+repr} rabbits in this generation")
            #print(f"There are {len(all_rabbits)} rabbits in the dictionary")
            #print(f"Counter says {counter}, total says {total}")
            #print(f"Resulting in {all_rabbits}")
            
            unrepr = 0
            gen += 1
        else:
            #print("#### First generation always has one unreproductive rabbit.### ")
            all_rabbits[1] = 1
            gen += 1
    return total

print(rabbit_pairs(n,k))