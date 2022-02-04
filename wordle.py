#!/usr/bin/env python
# coding: utf-8

# In[2]:


# !pip install english_words
from english_words import english_words_set


# In[3]:


'carer' in english_words_set #??


# # preprocessing words from en dict

# In[5]:


#select 4 or 5 letter words
init_words_list = [x for x in  english_words_set if (len(x) == 4) or (len(x) == 5)]
print(len(init_words_list))

# remove punctuation from en dict ex. wasn't
PUNCT_TO_REMOVE = ['\'','.','&']
words_list = []
for w in init_words_list:
    j = 0
    for p in PUNCT_TO_REMOVE:
        if p in w:
            j = 1
            break
    if j == 0:    
        words_list.append(w)

#letter to lowercase
lower_word_list = [x.lower() for x in words_list]
print(lower_word_list[:10])


# In[8]:


count_dict = {}
for word in lower_word_list:
    for _letter in word:
        if _letter not in count_dict:
            count_dict[_letter] = 0
        else:
            count_dict[_letter] += 1
            
#most freq letter
{k: v for k, v in sorted(count_dict.items() , key=lambda item: item[1], reverse = True)}
#recommend guess: reals(check if is single or plural) > point > ducky


# # check word length

# In[22]:


word_length = 5 #some words are plural ex. words
confirm_letter = 'aict'
wrong_letter = 'relsponduky'
wrong_pos = {
#     0: 'r',
    2: 'a',
    2: 'i',
#     3: 'c',
    4: 't'
}

correct_pos = {
#     0: 'p',
#     1: 'e',
#     2: 'a',
    2: 'c',
#     4: 't'
}


# In[23]:


word_list = [x for x in lower_word_list if len(x) == word_length]

print('==========================================================================================')
print('check target word length... ')
print('total remained words:', len(word_list))
print('==========================================================================================')
confirmed_letter_res = []
confirm_letter_len = len(confirm_letter)

for _word in word_list:
    test_count = 0
    for confirm in confirm_letter:
        if confirm in _word:
            test_count += 1
    if test_count == confirm_letter_len:
        confirmed_letter_res.append(_word)
print('==========================================================================================')
print('check confirmed letter... ')
print('total found: ', len(confirmed_letter_res))
print(confirmed_letter_res)
print('==========================================================================================')

rm_wrong_res = []
for _word in confirmed_letter_res:
    is_target = 1
    for letter in wrong_letter:
        if letter in _word:
            is_target = 0
            break
    if is_target == 1:
        rm_wrong_res.append(_word)
print('==========================================================================================')
print('remove wrong letter... ')
print('total found: ', len(rm_wrong_res))
print(rm_wrong_res)
print('==========================================================================================')

rm_wrong_pos_res = []
wrong_pos_len = len(wrong_pos)

for _word in rm_wrong_res:
    _count = 0
    for condition in wrong_pos.items():
        if _word[condition[0]] != condition[1]:
            _count += 1
    if _count == len(wrong_pos):
        rm_wrong_pos_res.append(_word)
print('==========================================================================================')
print('remove wrong position letter... ')
print('total found: ', len(rm_wrong_pos_res))
print(rm_wrong_pos_res)
print('==========================================================================================')

correct_pos_res = []
correct_pos_len = len(correct_pos)

for _word in rm_wrong_pos_res:
    _count = 0
    for condition in correct_pos.items():
        if _word[condition[0]] == condition[1]:
            _count += 1
    if _count == len(correct_pos):
        correct_pos_res.append(_word)
print('==========================================================================================')
print('select correct position letter... ')
print('total found: ', len(correct_pos_res))
print(correct_pos_res)
print('==========================================================================================')


# In[ ]:




