import pandas as pd
import os
import stats

# class to save information on each text

# directory path where corpus files are located
directory_path = 'data/newsela-sample'

# save files to list
corpus_files = os.listdir(directory_path)

text_name_list = [] # list of text names
text_sent_count_list = [] #
text_word_count_list = []
text_sent_length_list = []
text_syllable_count_list = []
text_avg_syll_list = []
text_kfscore_list = []

for file in corpus_files:
    #load the text
    path = directory_path+'/'+file
    text = open(path,'r').read()

    # get statistics
    text_name_list.append(file)
    text_sent_count_list.append(stats.sentence_counter(text))
    text_word_count_list.append(stats.word_counter(text))
    text_sent_length_list.append(stats.avg_sent_length(text))
    text_syllable_count_list.append(stats.syllable_count(text))
    text_avg_syll_list.append(stats.avg_syllable_per_word(text))
    text_kfscore_list.append(stats.kf_score(text))

print('Finished Processing Data')
# create dataframe
column_names = ['File','N.sentences','N.words','N.syllables','Words.Per.Sentence', 'Syllables.Per.Word', 'Grade.Score']
df = pd.DataFrame(list(zip(text_name_list,text_sent_count_list,
                           text_word_count_list, text_syllable_count_list,
                           text_sent_length_list, text_avg_syll_list,
                           text_kfscore_list)), columns=column_names)

# save to csv
df.to_csv('results-task.csv', index=False)
print('CSV file saved!')