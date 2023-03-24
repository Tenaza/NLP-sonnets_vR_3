# /usr/bin/env python3
# coding: utf-8

from collections import defaultdict
import random
import pyphen
import json
import os
import pandas as pd


def dividir_silabas(palabra):
    diccionario = pyphen.Pyphen(lang='es')
    silabas = diccionario.inserted(palabra).split('-')

    return silabas


def is_grave(palabra):
    palabra = dividir_silabas(palabra)
    number_of_silabas = len(palabra)
    counter = number_of_silabas
    sil_ton = None
    for s in palabra:
        for l in palabra[number_of_silabas-counter]:
            if l in 'áéíóú':
                sil_ton = counter
        counter = counter - 1

    if sil_ton == None and list(palabra[number_of_silabas-1])[-1] in 'nsaeiou':
        return 1
    elif sil_ton == None:
        return 0
    elif sil_ton == 1:
        return 0
    elif sil_ton == 2:
        return 1
    elif sil_ton > 2:
        return 0


def verses_graves_to_dictionary(text_verses, text_syls, text_ultpal):
    dict_verses = defaultdict(list)
    i = 0
    # Por cada terminacion se le agregan los versos correspondientes
    for syl in text_syls.terminacion:
        syl_tmp=syl[1:]
        #print(syl[1:])
        if (is_grave(text_ultpal.iloc[i].ultimapalabra) == 1):
            dict_verses[syl_tmp].append(text_verses.iloc[i].verse)
        i += 1

    return dict_verses


def filter_by_num_verses(dict_verses):
    dict_verses_filter_num = defaultdict(list)
    for syl in dict_verses:
        if (len(dict_verses[syl]) > 4):
            dict_verses_filter_num[syl] = dict_verses[syl]

    return dict_verses_filter_num


def obtain_last_word(verse):
    verse_split = verse.split(' ')
    verse_split_len = int(len(verse_split)-1)
    last_word = verse_split[verse_split_len]
    return last_word


def filter_by_last_word(dict_verses):
    dict_verses_filter_ter = defaultdict(list)
    for ter in dict_verses.keys():
        diff_words = []
        for verse in dict_verses[ter]:
            tmp_word = obtain_last_word(verse)
            if tmp_word not in diff_words:
                diff_words.append(tmp_word)
        if len(diff_words) >= 4:
            dict_verses_filter_ter[ter] = dict_verses[ter]

    return dict_verses_filter_ter


def verses_by_final_syls(filename_verses, filename_syls, filename_ultpal):
    text_verses = pd.read_csv(filename_verses+".csv")
    text_syls = pd.read_csv(filename_syls+".csv")
    text_ultpal = pd.read_csv(filename_ultpal+".csv")

    dict_verses = verses_graves_to_dictionary(text_verses, text_syls, text_ultpal)
    dict_verses_filter_num = filter_by_num_verses(dict_verses)
    dict_verses_filter_ter = filter_by_last_word(dict_verses_filter_num)

    return dict_verses_filter_ter


def create_sonnets(dict_verses, dict_verses_city, dict_verses_apoc, city, src_dir_cities):
    n_sonnets=51
    for id_sonnet in range(1,(n_sonnets)):

        # Choose de final syllabe to build the sonnets
        hom_final_syls_city = homologous_final_syls(dict_verses, dict_verses_city)
        #print(hom_final_syls_city)
        final_syls_verse_A = random.choice(hom_final_syls_city)
        final_syls_verse_B = random.choice(list(dict_verses.keys()))
        final_syls_verse_C = random.choice(list(dict_verses.keys()))
        hom_final_syls_apoc = homologous_final_syls(dict_verses, dict_verses_apoc)
        #print(hom_final_syls_apoc)
        final_syls_verse_D = random.choice(hom_final_syls_apoc)

        # Core sonnets built
        verses_A_used = []
        last_words_A_used = []
        verse_A_city = random.choices(list(dict_verses_city[final_syls_verse_A]), k=1)
        verse_A0 = delete_duplicity(list(dict_verses[final_syls_verse_A]), verses_A_used, last_words_A_used)
        verses_A_used.append(verse_A0[0])
        last_words_A_used.append(obtain_last_word(verse_A0[0]))
        verse_A1 = delete_duplicity(list(dict_verses[final_syls_verse_A]), verses_A_used, last_words_A_used)
        verses_A_used.append(verse_A1[0])
        last_words_A_used.append(obtain_last_word(verse_A1[0]))
        verse_A2 = delete_duplicity(list(dict_verses[final_syls_verse_A]), verses_A_used, last_words_A_used)
        verses_A_used.append(verse_A2[0])
        last_words_A_used.append(obtain_last_word(verse_A2[0]))

        verses_B_used = []
        last_words_B_used = []
        verse_B0 = delete_duplicity(list(dict_verses[final_syls_verse_B]), verses_B_used, last_words_B_used)
        verses_B_used.append(verse_B0[0])
        last_words_B_used.append(obtain_last_word(verse_B0[0]))
        verse_B1 = delete_duplicity(list(dict_verses[final_syls_verse_B]), verses_B_used, last_words_B_used)
        verses_B_used.append(verse_B1[0])
        last_words_B_used.append(obtain_last_word(verse_B1[0]))
        verse_B2 = delete_duplicity(list(dict_verses[final_syls_verse_B]), verses_B_used, last_words_B_used)
        verses_B_used.append(verse_B2[0])
        last_words_B_used.append(obtain_last_word(verse_B2[0]))
        verse_B3 = delete_duplicity(list(dict_verses[final_syls_verse_B]), verses_B_used, last_words_B_used)
        verses_B_used.append(verse_B3[0])
        last_words_B_used.append(obtain_last_word(verse_B3[0]))

        verses_C_used = []
        last_words_C_used = []
        verse_C0 = delete_duplicity(list(dict_verses[final_syls_verse_C]), verses_C_used, last_words_C_used)
        verses_C_used.append(verse_C0[0])
        last_words_C_used.append(obtain_last_word(verse_C0[0]))
        verse_C1 = delete_duplicity(list(dict_verses[final_syls_verse_C]), verses_C_used, last_words_C_used)
        verses_C_used.append(verse_C1[0])
        last_words_C_used.append(obtain_last_word(verse_C1[0]))
        verse_C2 = delete_duplicity(list(dict_verses[final_syls_verse_C]), verses_C_used, last_words_C_used)
        verses_C_used.append(verse_C2[0])
        last_words_C_used.append(obtain_last_word(verse_C2[0]))

        verses_D_used = []
        last_words_D_used = []
        verse_D0 = delete_duplicity(list(dict_verses[final_syls_verse_D]), verses_D_used, last_words_D_used)
        verses_D_used.append(verse_D0[0])
        last_words_D_used.append(obtain_last_word(verse_D0[0]))
        verse_D1 = delete_duplicity(list(dict_verses[final_syls_verse_D]), verses_D_used, last_words_D_used)
        verses_D_used.append(verse_D1[0])
        last_words_D_used.append(obtain_last_word(verse_D1[0]))
        verse_D_apoc = random.choices(list(dict_verses_apoc[final_syls_verse_D]), k=1)


        #print(" XXXXXXXXXX["+city+" "+str(id_sonnet)+"]XXXXXXXXXX\n")
        sonnet = " "+verse_A_city[0]+str(add_punctuation())+"\n"+verse_B0[0]+str(add_punctuation())+"\n"+verse_B1[0]+str(add_punctuation())+"\n"+verse_A0[0]+"."+"\n\n"+verse_A1[0]+str(add_punctuation())+"\n"+verse_B2[0]+str(add_punctuation())+"\n"+verse_B3[0]+str(add_punctuation())+"\n"+verse_A2[0]+"."+"\n\n"+verse_C0[0]+str(add_punctuation())+"\n"+verse_D0[0]+str(add_punctuation())+"\n"+verse_C1[0]+"."+"\n\n"+verse_D1[0]+str(add_punctuation())+"\n"+verse_C2[0]+str(add_punctuation())+"\n "+verse_D_apoc[0]+"."+"\n"

        to_text(src_dir_cities, id_sonnet, city, sonnet)

    return 0


def homologous_final_syls(dict_verses, dict_verses_):
    hom_final_syls = []
    for syl in dict_verses:
        #print("syl:",syl)
        #if ((syl in dict_verses.keys()) and (syl in dict_verses_.keys()) and (syl not in hom_final_syls)):
        if ((syl in dict_verses.keys()) and (syl in dict_verses_.keys())):
            hom_final_syls.append(syl)

    for syl_ in dict_verses_:
        #print("syl_:",syl_)
        #if ((syl_ in dict_verses.keys()) and (syl_ in dict_verses_.keys()) and (syl_ not in hom_final_syls)):
        if ((syl_ in dict_verses.keys()) and (syl_ in dict_verses_.keys())):
            hom_final_syls.append(syl_)

    return hom_final_syls


#def delete_duplicity(verses, verses_used_ref):
#    verses_eval = random.choices(verses, k=1)
#    while (verses_eval in verses_used_ref):
#        verses_eval = random.choices(verses, k=1)
#
#    return verses_eval


def delete_duplicity(verses, verses_used_ref, last_words_used_ref):

    verse_eval = random.choices(verses, k=1)
    last_word_verse = obtain_last_word(verse_eval[0])
    while ((verse_eval in verses_used_ref) or (last_word_verse in last_words_used_ref)):
        verse_eval = random.choices(verses, k=1)
        last_word_verse = obtain_last_word(verse_eval[0])

    return verse_eval

def add_punctuation():
    punctuation=[".", ".", ",", ",", ",", ",","", ""]
    sign = random.choice(punctuation)

    return sign


def to_text(src_dir_cities, id_sonnet, city, sonnet):
    with open(src_dir_cities+"/"+city+"/"+str(id_sonnet)+".txt", "w") as sonnet_file:
        sonnet_file.write(sonnet)

    return 0


def to_json(name_datafile, name_datastructure):
    with open(name_datafile+".json", "w") as outfile:
        json.dump(name_datastructure, outfile)

    return 0


def main():
    # SRC FOR MODEL
    filename_verses = "00_versos_predicted"
    filename_syls = "01_terminaciones_versos_v2"
    filename_ultpal = "02_ultimapalabra_versos"
    dict_verses = verses_by_final_syls(filename_verses, filename_syls, filename_ultpal)

    #for ter in dict_verses:
    #    print(ter+": "+str(dict_verses[ter])+"\n")

    # SRC FOR APOCALIPSIS
    filename_verses_apoc = "00_versos_apocalipsis"
    filename_syls_apoc = "01_terminaciones_versos_apocalipsis_v2"
    filename_ultpal_apoc = "02_ultimapalabra_versos_apocalipsis"
    dict_verses_apoc = verses_by_final_syls(filename_verses_apoc, filename_syls_apoc, filename_ultpal_apoc)
    #print(dict_verses_apoc)

    #print("\n\n\n\n")
    #for ter in dict_verses_apoc:
    #    print(ter+": "+str(dict_verses_apoc[ter])+"\n")

    # SRC FOR CITIES
    src_dir_cities = "03_sonetos_by_city"
    os.system("rm -r " + src_dir_cities)
    os.system("mkdir " + src_dir_cities)
    os.system("bash setup.bash")
    cont_city=1
    for city in os.listdir(src_dir_cities):
        if os.path.isdir(src_dir_cities+"/"+city):
            print("["+str(cont_city)+"] "+city)
            cont_city += 1
            #try:
            filename_verses_city = "00_versos_by_city/"+city+"/00_versos_predicted_"+city
            filename_syls_city = "01_terminaciones_by_city_v2/"+city+"/01_terminaciones_"+city+"_v2"
            filename_ultpal_apoc = "02_ultimapalabra_by_city/"+city+"/02_ultimapalabra_"+city
            dict_verses_city = verses_by_final_syls(filename_verses_city, filename_syls_city, filename_ultpal_apoc)

            create_sonnets(dict_verses, dict_verses_city, dict_verses_apoc, city, src_dir_cities)
            #except Exception as e:
            #    print ("ERROR: Sonnets don't created to city: "+city+". "+str(e))

        else:
            print ("ERROR: Directory 03_sonetos_by_city not found.")

    return 0


if __name__ == "__main__":
    main()

