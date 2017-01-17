import csv
from sklearn import tree

features = []
players = []

def extractFeatures(actions):
    countSelection = 0
    for elt in actions:
        if elt == 's':
            countSelection += 1

    features_player = [countSelection, len(actions)]
    return features_player

#TRAINING
with open('data/train.csv', 'r') as csvfile:
    for row in csvfile:
        row = row.split(';')
        player = row[0]
        actions = row[1].split(',')

        features_player = extractFeatures(actions)

        features.append(features_player)
        players.append(player)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, players)

#TEST
predict_features = []
row_num = []

with open('data/test.csv', 'r') as csvfile:
    for row in csvfile:
        row = row.split(';')
        actions = row[1].split(',')

        features_player = extractFeatures(actions)
        predict_features.append(features_player)
        row_num.append(row[0])

predictions = clf.predict(predict_features)

#OUTPUT
with open('output.csv', 'w') as csvfile:
    text_to_write = 'row ID,battleneturl\n'

    for i in range(len(row_num)):
        text_to_write += '{},{}\n'.format(row_num[i], predictions[i])

    csvfile.write(text_to_write)
