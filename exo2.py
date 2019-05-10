# Assign spell power lists to variables

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

# Assign 0 to each variable that stores the victories

# Execution of spell clashes


# We check who has won, do not forget the possibility of a draw.
# Print the result based on the winner.

for i in range(len(gandalf)):
    if gandalf[i] > saruman [i]:
        print('Gandalf wins')
    if gandalf[i] < saruman [i]:
        print('Saruman wins')
    if gandalf[i] == saruman [i]:
        print('Tie')

# 1. Spells now have a name and there is a dictionary that relates that name to a power.
# variables

POWER = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

# Assign spell power lists to variables
gandalf_power = []
saruman_power = []
for item in gandalf:
    gandalf_power.append(POWER[item])
for item in saruman:
    saruman_power.append(POWER[item])

# 2. A sorcerer wins if he succeeds in winning 3 spell clashes in a row.
# Execution of spell clashes
spell_clash = []
for i in range(len(gandalf_power)):
    if gandalf_power[i] > saruman_power[i]:
        spell_clash.append('Gandalf')
    if gandalf_power[i] < saruman_power[i]:
        spell_clash.append('Sarumen')
    if gandalf[i] == saruman [i]:
        spell_clash.append('Tie')
# check for 3 wins in a row
winner = 'no one'
for counter in range(len(spell_clash)):
    if counter > len(spell_clash)-2:
        break
    elif spell_clash[counter] == spell_clash[counter+1] == spell_clash[counter+2]:
        winner = spell_clash[counter]
        break

#check the winner
print(winner)

# 3. Average of each of the spell lists.
mean_gandalf_power = sum(gandalf_power)/len(gandalf_power)
mean_saruman_power = sum(saruman_power)/len(saruman_power)

# 4. Standard deviation of each of the spell lists.
import statistics
statistics.stdev(gandalf_power)
statistics.stdev(saruman_power)
