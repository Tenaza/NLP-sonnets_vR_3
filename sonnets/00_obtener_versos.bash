#!/bin/bash


# VERSES MODEL
src_model="../verses/verses_model"
infile="00_output_v6_20_cleanyears_verses_potenciales_con_terminacion"
outfile="00_versos_predicted"

awk 'BEGIN{FS=","}{print $2}' "${src_model}/${infile}.csv" > "${outfile}.csv"


# VERSES BY CITY
mkdir "00_versos_by_city"
city_filename="../cities/00_ciudades_unicas.tmp.csv"

if [[ -f "$city_filename" ]]; then
    while IFS= read -r city
    do
        mkdir "00_versos_by_city/${city}"
        src_city="../verses/verses_cities/${city}"
        infile="00_output_v6_20_cleanyears_verses_potenciales_con_terminacion_${city}"
        outfile="00_versos_predicted_${city}"

        awk 'BEGIN{FS=","}{print $2}' "${src_city}/${infile}.csv" > "00_versos_by_city/${city}/${outfile}.csv"

    done < $city_filename
fi


# VERSES APOCALIPSIS
src_apoc="../verses/verses_apoc/"
infile="versos_apocalipsis_con_terminacion"
outfile="00_versos_apocalipsis"

awk 'BEGIN{FS=","}{print $2}' "${src_apoc}/${infile}.csv" > "${outfile}.csv"


