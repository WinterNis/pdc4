from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

"""
Create the histogramme of possible actions, then make a decision tree
"""

list_actions = set()
features = []
players = []

le = preprocessing.LabelEncoder()
le.fit(['Terran', 'Protoss', 'Zerg'])

def extractFeatures(actions, list_actions):
    actions_histo = {}
    real_actions = actions[1::2]

    for action in list_actions:
        actions_histo[action] = 0

    # we create the histogramme
    for action in real_actions:
        actions_histo[action] += 1

    race = le.transform([actions[0]])

    #now we transform action to a vector
    features_player = [race]
    for key,value in actions_histo.items():
        features_player.append(value/len(actions))

    #we add the apm
    apm = len(real_actions)/int(actions[len(actions)-1])*30*60
    features_player.append(apm)
    return features_player

def write_output(list_actions):
    predict_features = []
    row_num = []

    with open('data/test.csv', 'r') as csvfile:
        for row in csvfile:
            row = row.split(';')
            actions = row[1].split(',')

            features_player = extractFeatures(actions, list_actions)
            predict_features.append(features_player)
            row_num.append(row[0])

    predictions = clf.predict(predict_features)

    #OUTPUT
    with open('output.csv', 'w') as csvfile:
        text_to_write = 'row ID,battleneturl\n'

        for i in range(len(row_num)):
            text_to_write += '{},{}\n'.format(row_num[i], predictions[i])

        csvfile.write(text_to_write)

def list_all_actions(list_actions):
    with open('data/train.csv', 'r') as csvfile:
        # we add all possible actions to list_actions
        for row in csvfile:
            row = row.split(';')
            actions = row[1].split(',')

            for i in range(1,len(actions),2):
                list_actions.add(actions[i])


#TRAINING
list_all_actions(list_actions)

with open('data/train.csv', 'r') as csvfile:
    for row in csvfile:
        row = row.split(';')
        player = row[0]
        actions = row[1].split(',')

        features_player = extractFeatures(actions, list_actions)

        features.append(features_player)
        players.append(player)

clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, players)

scores = cross_val_score(clf, features, players, cv=10)
print(scores)

#TEST
#write_output()
