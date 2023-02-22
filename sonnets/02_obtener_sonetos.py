# /usr/bin/env python3

from collections import defaultdict
import random
import json
import os
import pandas as pd


def read_source(filename_syls):
    with open(filename_syls+".csv", "r") as data_file:
        text_syls = data_file.readlines()

    return text_syls


def final_syls_to_array(text):
    final_syls = []
    for line in text:
        # Quitar salto de linea
        tmp = len(line)
        tmp -= 1
        final_syls.append(line[:tmp])

    return final_syls


def final_syls_counter(dict_verses):

    counter_final_syls = {}

    for syl in dict_verses:
        counter_final_syls[syl] = len(dict_verses[syl])

    return counter_final_syls


def verses_by_final_syls(filename_verses, final_syls):

    text_verses = pd.read_csv(filename_verses+".csv")
    dict_verses = defaultdict(list)
    dict_verses_filter = {}

    i = 0
    for syl in final_syls[1:]:

        if syl in dict_verses.keys():
            dict_verses[syl].append(text_verses.iloc[i].verse)
        else:
            dict_verses[syl].append(text_verses.iloc[i].verse)
        i += 1

    dict_verses_filter = filter_by_num_verses(dict_verses)
    return dict_verses_filter


def filter_by_num_verses(dict_verses):

    filter_dict_verses = {}
    for syl in dict_verses:
        if (len(dict_verses[syl]) > 5):
            filter_dict_verses[syl] = dict_verses[syl]

    return filter_dict_verses



def to_json(name_datafile, name_datastructure):

    with open(name_datafile+".json", "w") as outfile:
        json.dump(name_datastructure, outfile)

    return 0


def homologous_final_syls(dict_verses, dict_verses_):

    hom_final_syls = []
    for syl in dict_verses:

        if ((syl in dict_verses.keys()) and (syl in dict_verses_.keys()) and (syl not in hom_final_syls)):
            hom_final_syls.append(syl)

    for syl_ in dict_verses_:

        if ((syl_ in dict_verses.keys()) and (syl_ in dict_verses_.keys()) and (syl_ not in hom_final_syls)):
            hom_final_syls.append(syl_)

    return hom_final_syls


def to_text(src_dir_cities, id_sonnet, city, sonnet):
    with open(src_dir_cities+"/"+city+"/"+str(id_sonnet)+".txt", "w") as sonnet_file:
        sonnet_file.write(sonnet)

    return 0


def add_punctuation():
    # 2 puntos
    # 4 comas
    # 2 espacios
    punctuation=[".", ".", ",", ",", ",", ",","", ""]
    sign = random.choice(punctuation)

    return sign


def create_sonnets(dict_verses, dict_verses_city, dict_verses_apoc, city, src_dir_cities):

    n_sonnets=50
    for id_sonnet in range(1,(n_sonnets+1)):


        # Choose de final syllabe to build the sonnets
        hom_final_syls_city = homologous_final_syls(dict_verses, dict_verses_city)
        final_syls_verse_A = random.choice(hom_final_syls_city)

        final_syls_verse_B = random.choice(list(dict_verses.keys()))

        final_syls_verse_C = random.choice(list(dict_verses.keys()))

        hom_final_syls_apoc = homologous_final_syls(dict_verses, dict_verses_apoc)
        final_syls_verse_D = random.choice(hom_final_syls_apoc)

        # Core sonnets built
        # falta verificar que no se repitan los versos
        verse_A_city = random.choices(list(dict_verses_city[final_syls_verse_A]), k=1)
        verses_A = random.choices(list(dict_verses[final_syls_verse_A]), k=3)

        verses_B = random.choices(list(dict_verses[final_syls_verse_B]), k=4)

        verses_C = random.choices(list(dict_verses[final_syls_verse_C]), k=3)

        verses_D = random.choices(list(dict_verses[final_syls_verse_D]), k=2)
        verse_D_apoc = random.choices(list(dict_verses_apoc[final_syls_verse_D]), k=1)

        sonnet = " "+verse_A_city[0]+str(add_punctuation())+"\n"+verses_B[0]+str(add_punctuation())+"\n"+verses_B[1]+str(add_punctuation())+"\n"+verses_A[0]+"."+"\n\n"+verses_A[1]+str(add_punctuation())+"\n"+verses_B[2]+str(add_punctuation())+"\n"+verses_B[3]+str(add_punctuation())+"\n"+verses_A[2]+"."+"\n\n"+verses_C[0]+str(add_punctuation())+"\n"+verses_D[0]+str(add_punctuation())+"\n"+verses_C[1]+"."+"\n\n"+verses_D[1]+str(add_punctuation())+"\n"+verses_C[2]+str(add_punctuation())+"\n "+verse_D_apoc[0]+"."+"\n"

        print ("\n\nXXXXXXXXXXX["+city+" "+str(id_sonnet)+"]XXXXXXXXXXXXXXXXX\n")
        #print (sonnet)

        to_text(src_dir_cities, id_sonnet, city, sonnet)
        #counter_city = "2"
        #with open("verses/"+city+"/"+str(counter_city)+".txt", "w") as sonnet_file:
        #    sonnet_file.write(sonnet)

    return sonnet


def main():

    filename_verses = "00_versos_predicted"
    filename_syls = "01_terminaciones_versos"
    text_syls = read_source(filename_syls)
    final_syls = final_syls_to_array(text_syls)
    dict_verses = verses_by_final_syls(filename_verses, final_syls)
    counter_syls = final_syls_counter(dict_verses)

    filename_verses_apoc = "00_versos_apocalipsis"
    filename_syls_apoc = "01_terminaciones_versos_apocalipsis"
    text_syls_apoc = read_source(filename_syls_apoc)
    final_syls_apoc = final_syls_to_array(text_syls_apoc)
    dict_verses_apoc = verses_by_final_syls(filename_verses_apoc, final_syls_apoc)
    counter_syls_apoc = final_syls_counter(dict_verses_apoc)


    src_dir_cities = "02_sonetos_by_city"
    os.system("rm -r " + src_dir_cities)
    os.system("mkdir " + src_dir_cities)
    os.system("bash setup.bash")

    for city in os.listdir(src_dir_cities):
        if os.path.isdir(src_dir_cities+"/"+city):

            try:
                filename_verses_city = "00_versos_by_city/"+city+"/00_versos_predicted_"+city
                filename_syls_city = "01_terminaciones_by_city/"+city+"/01_terminaciones_"+city

                text_syls_city = read_source(filename_syls_city)
                final_syls_city = final_syls_to_array(text_syls_city)
                dict_verses_city = verses_by_final_syls(filename_verses_city, final_syls_city)
                counter_syls_city = final_syls_counter(dict_verses_city)

                create_sonnets(dict_verses, dict_verses_city, dict_verses_apoc, city, src_dir_cities)
            except Exception as e:
                print ("ERROR: Sonnets don't created to city: "+city+". "+str(e))

        else:
            print ("ERROR: No dictories found.")


    return 0


if __name__ == "__main__":
    main()

