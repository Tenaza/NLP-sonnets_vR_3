#!/bin/bash

# TERMINACIONES MODELO
src_model="../verses/verses_model"
infile="00_output_v8_20_cleanyears_verses_potenciales_con_terminacion"
outfile="01_terminaciones_versos"

awk 'BEGIN{FS="\""}{print $2}' "${src_model}/${infile}.csv" > "${infile}.tmp0.csv"
awk 'BEGIN{FS=","}{print $NF}' "${infile}.tmp0.csv" > "${infile}.tmp1.csv"
awk 'BEGIN{FS="'\''"}{print $2}' "${infile}.tmp1.csv" > "${outfile}.csv"
echo -e "\nVERSOS MODEL: Se ha crado el archivo ${outfile}.csv"

rm ${infile}.tmp*.csv


# TERMINACIONES CITY
rm -r "01_terminaciones_by_city"
mkdir "01_terminaciones_by_city"
city_filename="../cities/00_ciudades_unicas.csv"

if [[ -f "$city_filename" ]]; then
    while IFS= read -r city
    do
        mkdir "01_terminaciones_by_city/${city}"
        src_city="../verses/verses_cities/${city}"
        infile="00_output_v8_20_cleanyears_verses_potenciales_con_terminacion_${city}"
        outfile="01_terminaciones_${city}"

        awk 'BEGIN{FS="\""}{print $2}' "${src_city}/${infile}.csv" > "01_terminaciones_by_city/${city}/${infile}.tmp0.csv"
        awk 'BEGIN{FS=","}{print $NF}' "01_terminaciones_by_city/${city}/${infile}.tmp0.csv" > "01_terminaciones_by_city/${city}/${infile}.tmp1.csv"
        awk 'BEGIN{FS="'\''"}{print $2}' "01_terminaciones_by_city/${city}/${infile}.tmp1.csv" > "01_terminaciones_by_city/${city}/${outfile}.csv"

        rm "01_terminaciones_by_city/${city}/${infile}.tmp0.csv"
        rm "01_terminaciones_by_city/${city}/${infile}.tmp1.csv"

    done < $city_filename
fi
echo -e "VERSOS CITY: Se ha creado la carpeta 01_terminaciones_by_city"


# TERMINACIONES APOCALIPSIS
src_apoc="../verses/verses_apoc"
infile="versos_apocalipsis_con_terminacion"
outfile="01_terminaciones_versos_apocalipsis"

awk 'BEGIN{FS="\""}{print $2}' "${src_apoc}/${infile}.csv" > "${infile}.tmp0.csv"
awk 'BEGIN{FS=","}{print $NF}' "${infile}.tmp0.csv" > "${infile}.tmp1.csv"
awk 'BEGIN{FS="'\''"}{print $2}' "${infile}.tmp1.csv" > "${outfile}.csv"
echo -e "VERSOS APOC: Se ha creado el archivo ${outfile}.csv"

rm ${infile}.tmp*.csv


