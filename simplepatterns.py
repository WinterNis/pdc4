from collections import Counter
from collections import OrderedDict

from sklearn.model_selection import train_test_split

player_reference = {}
pattern_reference = OrderedDict()

# data generation
print("Data generation")
x_train = []
x_test = []
y_train = []
y_test = []

with open('data/trainlight.csv', 'r') as file:
    next(file)
    x = []
    y = []
    for line in file:
        line = line.split(';')
        player_name = line[0].strip(' \t\n\r')
        y.append(player_name)
        x.append(line[1].split(','))

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

################


def histogram_compararator(g1, g2):
    score = 0
    for pattern in (set(g1.keys()) | set(g2.keys())):
        score = score + abs(g1.get(pattern, 0) - g2.get(pattern, 0))
    return score/len(pattern)


def actions_to_patterns(game):
    patterns = []
    # for current_p_size in range(3, int(len(actions)/100)):
    for current_p_size in range(2, 7):
        for i in range(len(actions)-current_p_size+1):
            patterns.append(tuple(actions[i:i+current_p_size]))
    return patterns

# Training
print("Training")
for player_index in range(len(y_train)):
    player_name = y_train[player_index]
    game = x_train[player_index]
    if player_name not in player_reference:
        player_reference[player_name] = {}
    race = game[0].strip(' \t\n\r')
    actions = game[1::2]
    temp = Counter(actions_to_patterns(actions))
    player_reference[player_name].update(temp)

for player in list(player_reference.keys()):
    sorted_patterns = sorted(player_reference[player].items(), key=lambda x: x[1])
    player_reference[player] = dict(sorted_patterns[:15])
    s = sum(player_reference[player].values())
    player_reference[player] = {k: v/s for k, v in player_reference[player].items()}

# Test
print("test " + str(len(y_test)))
accuracy = 0
total = len(x_test)
for test_index in range(len(x_test)):
    print(str(test_index))
    player_test = y_test[test_index]
    game_test = x_test[test_index]
    if player_test not in player_reference.keys():
        print('not in')
        total -= 1
        break
    test_pattern = game_test[1::2]
    best_fit = {'score': 2**10000, 'player': ''}
    game_test_patterns = Counter(actions_to_patterns(game))
    sorted_patterns = sorted(game_test_patterns.items(), key=lambda x: x[1])
    game_test_patterns = dict(sorted_patterns[:15])
    s = sum(game_test_patterns.values())
    game_test_patterns = {k: v/s for k, v in game_test_patterns.items()}
    for player, player_patterns in player_reference.items():
        score = histogram_compararator(game_test_patterns, player_patterns)
        if score <= best_fit['score']:
            best_fit['score'] = score
            best_fit['player'] = player
    if best_fit['player'] == player_test:
        print('match')
        accuracy += 1

print(accuracy/total*100)
