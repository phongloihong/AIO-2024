import numpy as np


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    play_tennis = train_data[:, -1]
    sample_len = len(play_tennis)

    prior_probability[0] = np.sum(play_tennis == y_unique[0]) / sample_len
    prior_probability[1] = np.sum(play_tennis == y_unique[1]) / sample_len

    return prior_probability


# P(a|c) = P(a and c) / P(c)
def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for c in range(len(y_unique)):
            for x in range(len(x_unique)):

                x_conditional_probability[c, x] = len(np.where(
                    (train_data[:, i] == x_unique[x]) &
                    (train_data[:, 4] == y_unique[c])
                )[0]) / len(np.where(train_data[:, 4] == y_unique[c])[0])

        print(x_conditional_probability)
        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0]


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


def predict_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    p0 = 0
    p1 = 0

    p0 = prior_probability[0] *\
        conditional_probability[0][0, x1] *\
        conditional_probability[1][0, x2] *\
        conditional_probability[2][0, x3] *\
        conditional_probability[3][0, x4]
    p1 = prior_probability[1] *\
        conditional_probability[0][1, x1] *\
        conditional_probability[1][1, x2] *\
        conditional_probability[2][1, x3] *\
        conditional_probability[3][1, x4]

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


train_data = create_train_data()
prior_probability = compute_prior_probability(train_data)
print("P(play tennis = no):", prior_probability[0])
print("P(play tennis = yes):", prior_probability[1])

conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
print("x1 = ", list_x_name[0])
print("x1 = ", list_x_name[1])
print("x1 = ", list_x_name[2])
print("x1 = ", list_x_name[3])

outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)

x1 = get_index_from_value("Sunny", list_x_name[0])
print(x1)

print("P('Outlook'='Sunny'|Play Tennis'='Yes') = ", np.round(conditional_probability
                                                             [0][1, x1], 2))

print("P('Outlook'='Sunny'|Play Tennis'='No') = ", np.round(conditional_probability
                                                            [0][0, x1], 2))

X = ['Synny', 'Cool', 'High', 'Strong']
pred = predict_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print("Play Tennis: Yes")
else:
    print("Play Tennis: No")
