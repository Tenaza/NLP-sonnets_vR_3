#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------

from silabizer import *
from check import *
import pandas as pd


def read_source(infile):
    with open(infile+".txt") as f:
        lines = f.readlines()
    return lines

def verses_by_line(lines, city):
    s = silabizer()
    d = dict_silabas_one_word(city, s)
    print(d)
    verses = []
    for l in lines:
        words = l.split()
        verses = createverses(silabas=12-d[city], line = l, verses= verses)
    new_verses = []
    for v in verses:
        verse_more_city = (str(city)+' '+ str(v)).replace('[', '').replace(']','')
        new_verses.append(verse_more_city)
        print(new_verses)
    return new_verses

def export_verses(verses, outfile):
    pd.DataFrame(verses, columns=['endecasílabo']).to_csv(outfile+".csv")


