import json

def evaluate(predict_data, gold_data):
    correct_sys, all_sys = 0, 0
    correct_gt = 0

    for i in range(len(gold_data)):
        for j in range(len(gold_data[i]['relations'])):
            for id in gold_data[i]['relations'][j]["rid"]:
                if id != 36:
                    correct_gt += 1
                    if id in predict_data[i]['relations'][j]["rid"]:
                        correct_sys += 1
            for id in predict_data[i]['relations'][j]["rid"]:
                if id != 36:
                    all_sys += 1

    precision = correct_sys / all_sys if all_sys != 0 else 1
    recall = correct_sys / correct_gt if correct_gt != 0 else 0
    f_1 = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0

    return precision, recall, f_1

def readfile(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    gold_file="./data/test.json"
    predict_file="./data/test.json"

    gold_data=readfile(gold_file)
    predict_data=readfile(predict_file)
    print(evaluate(predict_data, gold_data))