import os
from numpy import vectorize
from numpy import round as rd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import itertools
import threading
import time
import sys

done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
    print()

#function to transform texts into vectorized_txt
def vectorize(text):
    return TfidfVectorizer().fit_transform(text).toarray()

#function to check cosine similarity between 2 docs
def cos_sim(doc1, doc2):
    similarity= rd((cosine_similarity([doc1, doc2])*100),2)
    return similarity

#plagiarism checker
def check_plagiarism(texts_and_vs):
    # creates a set object for the results
    results = set()
    #iterate through text and vectorized contents list
    for sample_a, text_vector_a in texts_and_vs:
        #copy textnames and vectorized content list
        vectors_cp= textname_and_vectors.copy()
        #get index of 
        current_index = vectors_cp.index((sample_a, text_vector_a))
        #deletes the current index from copied list so it doesn't compare with itself
        del vectors_cp[current_index]
        #iterates through copy list
        for sample_b, text_vector_b in vectors_cp:
            #compare vector similarity
            sim_score = cos_sim(text_vector_a,text_vector_b)[0][1]
            #sort to avoid rsult repetition
            sample_pair =sorted((sample_a,sample_b))
            #join results
            score= sample_pair[0],sample_pair[1], sim_score
            # add results to set
            results.add(score)
    #sort results based on similar percentage
    sorted_results= sorted(results, key=lambda tup: tup[2], reverse= True)
    return sorted_results

if main == '__main__':
    t = threading.Thread(target=animate)
    t.start()


    #path to files
    path= "britney_lyrics/"

    #get a list of all the texts in the directory
    text_names = [doc for doc in os.listdir(path) if doc.endswith('.txt')]
    #store the text files' contents
    text_contents = [open(os.path.join(path, File)).read() for File in text_names]
    #vectorize the texts' contents
    vectorized_txts = vectorize(text_contents)
    # join texts and their vectorized contents
    textname_and_vectors = list(zip(text_names, vectorized_txts))

    #print plagiarism levels
    print()
    for results in check_plagiarism(textname_and_vectors):
        print(results[0], "and",results[1],"are:", results[2], "% similar")
    done = True
