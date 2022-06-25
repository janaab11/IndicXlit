# -*- coding: utf-8 -*-
"""Clean_urdu

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V5o9UhjejjwS-KM5YELBUzuSDbLIiI-S
"""

import csv
import sys
csv.field_size_limit(sys.maxsize)

import urduhack
import re
from urduhack.tokenization import sentence_tokenizer
from urduhack.preprocessing import preprocess
from urduhack import normalize
from collections import Counter

# Urdu
pattern = u'['u'\U00000000-\U00000620'u'\U00000623-\U00000626'u'\U00000629-\U00000629'u'\U0000063B-\U00000640'u'\U00000643-\U00000643'u'\U00000647-\U00000647'u'\U00000649-\U00000678'u'\U0000067A-\U0000067D'u'\U0000067F-\U00000685'u'\U00000687-\U00000687'u'\U00000689-\U00000690'u'\U00000692-\U00000697'u'\U00000699-\U000006A8'u'\U000006AA-\U000006AE'u'\U000006B0-\U000006BD'u'\U000006BF-\U000006C0'u'\U000006C2-\U000006CB'u'\U000006CD-\U0010FFFF]+'

# Kashmiri
# pattern = u'['u'\U00000000-\U0000061F'u'\U00000625-\U00000626'u'\U00000629-\U00000629'u'\U0000063B-\U00000640'u'\U00000643-\U00000643'u'\U00000647-\U00000647'u'\U00000649-\U00000652'u'\U00000655-\U00000671'u'\U00000673-\U00000678'u'\U0000067A-\U0000067D'u'\U0000067F-\U00000685'u'\U00000687-\U00000687'u'\U00000689-\U00000690'u'\U00000692-\U00000697'u'\U00000699-\U000006A8'u'\U000006AA-\U000006AE'u'\U000006B0-\U000006B9'u'\U000006BB-\U000006BD'u'\U000006BF-\U000006C0'u'\U000006C2-\U000006C3'u'\U000006C5-\U000006C5'u'\U000006C7-\U000006CB'u'\U000006CE-\U0010FFFF]+'

C = Counter()
with open (f'/content/drive/MyDrive/Colab_Notebooks/indicnlp-crawls-v4_final_ur.filtered', 'r') as f1:
  r1 = csv.reader(x.replace('\0', '') for x in f1)
  lines =  [line for line in r1 if line]
  print(len(lines))
  for i, row in enumerate(lines):
    print(i)
    try:
      if row == None:
        continue
      sentences = sentence_tokenizer(*row)
    except:
      continue
    for text in sentences:
      pre_process_text = preprocess(text)
      normalized_text = normalize(pre_process_text)
      split_text = filter(None, re.split(pattern, normalized_text))
      token = Counter(split_text)
      C += token
      # print(len(C))
C = C.most_common()
# print(C)
with open(f'/content/drive/MyDrive/Colab_Notebooks/IC2_ur.csv', 'w', encoding = "utf-8") as w1:
  w = csv.writer(w1)
  for i,v in C:
    # if v == 1:
    #   break
    w.writerow([i,v])