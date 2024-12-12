import pandas as pd
import os
import stats


# directory path where corpus files are located
directory_path = 'data/newsela-sample'

# save files to list
corpus_files = os.listdir(directory_path)

# create a dataframe to share analytics in
column_names = ['File','N.sentences','N.words','N.syllables','Words.Per.Sentence', 'Syllables.Per.Word', 'Grade.Score']
results_df = pd.DataFrame(columns=column_names)

for file in corpus_files:
    #load the text
    path = directory_path+'/'+file
    text = open(path,'r').read()

    # get statistics
    sent_count = stats.sentence_counter(text)
    word_count = stats.word_counter(text)
    syll_count = stats.syllable_count(text)
    avg_sent_len = stats.avg_sent_length(text)
    avg_syllable_per_word = stats.avg_syllable_per_word(text)
    score = stats.kf_score(text)

    # add to dataframe






# save to csv