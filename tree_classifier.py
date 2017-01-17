inputs = [
    'hotkey01',
    'hotkey82',
    'hotkey30',
    's',
    'hotkey21',
    'hotkey00',
    'hotkey60',
    'hotkey41',
    'hotkey80',
    'hotkey90',
    'sMineral',
    'hotkey10',
    'hotkey91',
    'hotkey71',
    'hotkey81',
    'hotkey40',
    'hotkey31',
    'hotkey12',
    'sBase',
    'hotkey62',
    'hotkey42',
    'hotkey11',
    'hotkey02',
    'hotkey50',
    'hotkey61',
    'hotkey70',
    'hotkey22',
    'hotkey52',
    'hotkey20',
    'hotkey72',
    'hotkey32',
    'hotkey92',
    'hotkey51'
]

players = [
    '/YongHwa/',
    '/ParalyzE/',
    '/INnoVation/',
    '/LiquidTLO/',
    '/PartinG/',
    '/Lilbow/',
    '/sOs/',
    '/WhiteRa/',
    '/Super/',
    '/Symbol/',
    '/ByuL/',
    '/iGJim/',
    '/Stardust/',
    '/FanTaSy/',
    '/Soulkey/',
    'Life/',
    '/Leenock/',
    '/Kane/',
    '/Stats/',
    '/soO/',
    '/DRG/',
    '/MaNa/',
    '/Rain/',
    '/Bbyong/',
    '/Rogue/',
    '/Dream/',
    '/yoeFWSan/',
    '/Zest/',
    '/viOLet/',
    '/Hydra/',
    '/TYTY/',
    '/MǂForGG/',
    '/Classic/',
    '/Bunny/',
    '/Life/',
    '/CMStormPolt/',
    '/ForGG/',
    '/Sen/',
    '/LiquidSnute/',
    '/Polt/',
    '/Pigbaby/',
    '/True/',
    '/Curious/',
    '/VortiX/',
    '/YoDa/',
    '/HuK/',
    '/Welmu/',
    '/Nerchio/',
    '/hydra/',
    '/Happy/',
    '/Dear/',
    '/LiquidBunny/',
    '/MyuNgSiK/',
    '/FireCake/',
    '/JJAKJI/',
    '/Cure/',
    '/Maru/',
    '/AxHeart/',
    '/Solar/',
    '/iaguz/',
    '/Trap/',
    '/herO/',
    '/MMA/',
    '/Golden/',
    '/Stork/',
    '/MinChul/',
    '/ShoWTimE/',
    '/LiquidTaeJa/',
    '/Dark/',
    '/Bomber/',
    '/iGXiGua/',
    '/HyuN/'
]

races = ['Terran', 'Protoss', 'Zerg']

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

train_size = 4099
test_size = 1025

le = LabelEncoder()
le.fit(races)

X = []
y = []


for line in open('train.csv', 'r'):
    train = line.split(',')
    [player, race] = train[0].split(';')
    if race == 'Terran\n':
        race = 'Terran'
    feature = [0 for i in range(len(inputs))]
    for i in range(1, len(train), 2):
        feature[inputs.index(train[i])] += 1

    normalize_term = sum(feature)
    if normalize_term != 0:
        feature = [x/normalize_term for x in feature]
    feature.append(le.transform([race])[0])
    X.append(feature)
    y.append(train[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

print(dtc.score(X_test, y_test))

#print(X_train[0])
#print(Y_train[0])
