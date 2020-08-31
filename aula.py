from collections import Counter
from collections import defaultdict
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}

]

# lista = [1, 2, 3, 4, 5]
# lista[2] = 7
# lista = [1, 2]


# tupla = (1, 2, 3, 4, 5)
# print (tupla[2])
# tupla[2] = 3
# tupla = (9, 9, 1)

# tupla = 2

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5),
    (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []


for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

# print(users)

# int numero (int a, int b){
#  return a + b;
# }


# def soma(a, b):
#     c = a + b


# resultado = soma (2, 3)

# print(soma(2, 3))


def number_of_friends(user):
    return len(user['friends'])
#print(number_of_friends(users[0]))

total_connections = sum(number_of_friends(u) for u in users)
#print (total_connections)

num_users = len(users)
avg_connections = total_connections / num_users
#print (avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
#print (num_friends_by_id)

lista_ordenada = sorted (num_friends_by_id, key = lambda num_friends: num_friends[1], reverse = True)

#print (lista_ordenada)

def friends_of_friends_ids_bad (user):
    return[
        foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]
    ]

def not_the_same (user, other_user):
    return user["id"] != other_user["id"]

def not_friends (user, other_user):
    return all(not_the_same (friend, other_user) for friend in user["friends"])

#print (not_friends(users[0], users[9]))

def friends_of_friends_ids (user):
    return set([
        foaf["id"]
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same (user, foaf)
        and not_friends (user, foaf)
    ])

#print (friends_of_friends_ids(users[0]))

#teste = [1, 2, 5, 4, 3, 2, 1, 2, 3, 2, 1]
#c = Counter (teste)

#print (c)
def friends_of_friends_ids_frequency (user):
    return Counter([
        foaf["id"]
        for friend in user ["friends"]
        for foaf in friend ["friends"]
        if not_the_same (user, foaf)
        and not_friends (user, foaf)
    ])


#print (friends_of_friends_ids_frequency(users[4]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"), (0, "GraphQL")
]

def data_scientists_who_like (target_interest):
    return [
        user_id for user_id, interest in interests if interest == target_interest
    ]

#print (data_scientists_who_like ("Big Data"))

#def f ():
    return 5

#d = defaultdict (list)

#d["Big Data"].append (2)
#print (d["teste"])


#(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (1, "Java"),
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

user_id_by_interest = defaultdict (list)
for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)

#print ("Interesses por usuário")
#print (interests_by_user_id)
#print ("Usuários por interesse")
#print (user_id_by_interest)

def user_with_common_interest_with (user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_id_by_interest[interest]
        if interested_user_id != user ["id"]
    ])

#print (user_with_common_interest_with (users[0]))

def most_common_interests_with (user):
    return Counter (
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_id_by_interest [interest]
        if interested_user_id != user["id"]
    )

#print (most_common_interests_with(users[0]))

salario_e_experiencia = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

salario_por_experiencia = defaultdict (list)
for salario, experiencia in salario_e_experiencia:
    salario_por_experiencia[experiencia].append(salario)

#print(salario_por_experiencia)
salario_medio_por_experiencia = {
    experiencia: sum (salarios) / len (salarios)
    for experiencia, salarios in salario_por_experiencia.items()
}

#print (salario_medio_por_experiencia)

def rotulo_por_experiencia (experiencia):
    if experiencia < 2:
        return "(0,2)"
    elif experiencia < 5:
        return "[2,5)"
    else:
        return "[5,...)"

salario_por_rotulo = defaultdict(list)
for salario, experiencia in salario_e_experiencia:
    salario_por_rotulo[rotulo_por_experiencia(experiencia)].append(salario)

#print (salario_por_rotulo)

salario_medio_por_rotulo = {
    rotulo: sum(salarios) / len(salarios)
    for rotulo, salarios in salario_por_rotulo.items()
}

#print (salario_medio_por_rotulo)

experiencia_e_tipo_de_conta = [
    (0.7, 'paga'),
    (1.9, 'gratuita'),
    (2.5, 'paga'),
    (4.2, 'gratuita'),
    (6, 'gratuita'),
    (6.5, 'gratuita'),
    (7.5, 'gratuita'),
    (8.1, 'gratuita'),
    (8.7, 'paga'),
    (10, 'paga')
]

def classificar_como_paga_ou_gratuita (experiencia):
    if experiencia < 3:
        return 'paga'
    elif experiencia < 8.5:
        return 'gratuita'
    else:
        return 'paga'

print (classificar_como_paga_ou_gratuita (1.9))