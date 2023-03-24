#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------

from check import validate_verse
from readfile import *
from silabizer import *
from paste_ending import *
import pandas as pd
import os


def build_verses_decasyllabes(infile, city, outfile):

    text = read_source(infile)
    verses = verses_by_line(text, city)
    validated_verses = validate_verse(verses)
    export_verses(validated_verses, outfile)


def build_potencial_verses(infile, outfile):
    syllabes_termination_by_verse(infile, outfile)


def main():

    # 1: create VERSES MODEL
    # 2: create VERSES APOCALIPSIS
    # 3: create VERSES CITIES by dir

    option=3
    #infile_src="00_output_v10_40_temp0.075_temp0.5_cleanyears"
    infile_src="00_output_v10_40_temp0.075_temp0.5_cleanyears"

    if (option == 1):
        try:
            src_dir_model = "verses_model"
            os.system("rm -r " + src_dir_model)
            os.system("mkdir " + src_dir_model)

            city = ""
            infile = infile_src
            outfile = src_dir_model+"/"+infile+"_verses"
            build_verses_decasyllabes(infile, city, outfile)

            infile = outfile
            outfile = outfile+"_potenciales_con_terminacion"
            build_potencial_verses(infile, outfile)

        except Exception as e:
            print ("ERROR: Verses don't created to model. "+str(e))

    elif (option == 2):
        try:
            src_dir_apoc = "verses_apoc"
            os.system("rm -r " + src_dir_apoc)
            os.system("mkdir " + src_dir_apoc)
            os.system("cp ../apocalipsis/versos_apocalipsis_con_terminacion.csv " + src_dir_apoc)

        except Exception as e:
            print ("ERROR: Verses don't created to apocalipsis. "+str(e))

    else:
        cont_city = 1
        src_dir_cities = "verses_cities"
        os.system("rm -r " + src_dir_cities)
        os.system("mkdir " + src_dir_cities)
        os.system("bash setup.bash")

        for city in os.listdir("verses_cities/"):
            if os.path.isdir("verses_cities/"+city):
                try:
                    print(str(cont_city)+": "+city)
                    infile = infile_src
                    outfile = src_dir_cities+"/"+city+"/"+infile+"_verses"
                    build_verses_decasyllabes(infile, city, outfile)

                    infile = outfile
                    outfile = outfile+"_potenciales_con_terminacion_"+city
                    # paste_ending
                    build_potencial_verses(infile, outfile)
                    cont_city += 1

                except Exception as e:
                    print ("ERROR: Verses don't created to city: "+city+". "+str(e))

            else:
                print ("ERROR: No dictories found.")


if __name__ == "__main__":
    main()

