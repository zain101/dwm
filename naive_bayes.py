import pandas as pd
data = None
class_attr = None
priori = {}
cp = {}

def calculate_priori():
    class_values = list(set(data[class_attr]))
    global priori
    class_data = list(data[class_attr])
    for i in class_values:
        priori[i] = class_data.count(i) / float(len(class_data))


def get_cp(attr, attr_type, class_value):
    data_attr = list(data[attr])
    class_data = list(data[class_attr])
    total = 0
    for i in range(0, len(data_attr)):
        if class_data[i] == class_value and data_attr[i] == attr_type:
            total += 1
    return (total+1) / float(class_data.count(class_value))


def calculate_conditional_probabilities(hypothesis):
    global priori
    global cp
    for i in priori:
        cp[i] = {}
        for j in hypothesis:
            cp[i].update({hypothesis[j]: get_cp(j, hypothesis[j], i)})


def classify():
    for i in cp:
        print i, " ==> ", reduce(lambda x, y: x * y, cp[i].values()) * priori[i]

if __name__ == '__main__':
    data = pd.read_csv('new_dataset.csv', sep=',', header=(0))
    class_attr = 'Buys_Computer'
    calculate_priori()
    hypothesis = {"Age": '<=30', "Income": "medium", "Student": 'yes', "Creadit_Rating": 'fair'}
    # hypothesis = {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Weak'}
    calculate_conditional_probabilities(hypothesis)
    print "Given dataset: \n", data
    print "Given hypothesis: \n", hypothesis
    print "Selected Class Attribute: \n", class_attr
    print "Results  "
    classify()
