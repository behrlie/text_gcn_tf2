#!/usr/bin/python
#-*-coding:utf-8-*-

from sklearn.model_selection import train_test_split

with open('data/WOS11967/X.txt', 'r') as f:
    sentences = f.readlines()
with open('data/WOS11967/Y.txt', 'r') as f:
    labels = f.readlines()

sentences = [s.replace('\n', '') for s in sentences]
labels_int = [int(l.strip()) for l in labels]

train_sentences, test_sentences, train_labels, test_labels = train_test_split(
    sentences, labels_int, test_size=0.2, random_state=42, stratify=labels_int)

mapping = {10: 'Person-perception', 1: 'Machine-learning', 29: 'Cell-biology', 16: 'Machine-design', 18: 'Ambient-Intelligence', 6: 'Electrical-circuits', 15: 'Manufacturing-engineering', 13: 'computer-aided-design', 11: 'Nonverbal-communication', 7: 'Digital-control', 28: 'Molecular-biology', 24: 'Allergies', 31: 'Immunology', 26: 'Ankylosing-Spondylitis', 22: 'Water-Pollution', 12: 'Prosocial-behavior', 17: 'Fluid-mechanics', 0: 'Computer-vision', 9: 'Social-cognition', 25: "Alzheimer's-Disease", 8: 'Prejudice', 3: 'Cryptography', 32: 'Genetics', 19: 'Geotextile', 2: 'network-security', 30: 'Human-Metabolism', 5: 'Electricity', 20: 'Remote-Sensing', 27: 'Anxiety', 21: 'Rainwater-Harvesting', 14: 'Hydraulics', 23: 'Addiction', 4: 'Operating-systems'}

train_or_test_list = []
labels = []
sentences = []
for i in range(len(train_labels)):
    labels.append(mapping[train_labels[i]])
    sentences.append(train_sentences[i])
    train_or_test_list.append('train')
for i in range(len(test_labels)):
    labels.append(mapping[test_labels[i]])
    sentences.append(test_sentences[i])
    train_or_test_list.append('test')

dataset_name = 'WOS11967'
# sentences = ['Would you like a plain sweater or something else?​', 'Great. We have some very nice wool slacks over here. Would you like to take a look?']
# labels = ['Yes' , 'No' ]
# train_or_test_list = ['train', 'test']


meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)

f = open('data/' + dataset_name + '.txt', 'w')
f.write(meta_data_str)
f.close()

corpus_str = '\n'.join(sentences)

f = open('data/corpus/' + dataset_name + '.txt', 'w')
f.write(corpus_str)
f.close()