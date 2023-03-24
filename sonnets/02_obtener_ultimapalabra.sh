#!/bin/bash

# VERSE MODEL
src_model="../verses/verses_model"
infile_src="00_output_v10_40_temp0.075_temp0.5_cleanyears_verses_potenciales_con_terminacion"
outfile="02_ultimapalabra_versos"

infile=${infile_src}
awk 'BEGIN{FS=","}{print $2}' "${src_model}/${infile}.csv" > "${infile}.tmp0.csv"
awk 'BEGIN{FS=" "}{print $NF}' "${infile}.tmp0.csv" > "${outfile}.csv"
sed -i "1d" "${outfile}.csv"
sed -i "1i ultimapalabra" "${outfile}.csv"
echo -e "\nVERSOS MODEL: Se ha creado el archivo ${outfile}.csv"

rm ${infile}.tmp*.csv


# TERMINACIONES BY CITY
rm -r "02_ultimapalabra_by_city"
mkdir "02_ultimapalabra_by_city"
city_filename="../cities/00_ciudades_unicas.csv"

if [[ -f "$city_filename" ]]; then
    while IFS= read -r city
    do
        mkdir "02_ultimapalabra_by_city/${city}"
        src_city="../verses/verses_cities/${city}"
        infile="${infile_src}_${city}"
        outfile="02_ultimapalabra_${city}"

        awk 'BEGIN{FS=","}{print $2}' "${src_city}/${infile}.csv" > "02_ultimapalabra_by_city/${city}/${infile}.tmp0.csv"
        awk 'BEGIN{FS=" "}{print $NF}' "02_ultimapalabra_by_city/${city}/${infile}.tmp0.csv" > "02_ultimapalabra_by_city/${city}/${outfile}.csv"
        sed -i "1d" "02_ultimapalabra_by_city/${city}/${outfile}.csv"
        sed -i "1i ultimapalabra" "02_ultimapalabra_by_city/${city}/${outfile}.csv"
        rm "02_ultimapalabra_by_city/${city}/${infile}.tmp0.csv"

    done < $city_filename
fi
echo -e "VERSOS CITY: Se ha creado la carpeta 02_ultimapalabra_by_city"


# TERMINACIONES APOCALIPSIS
src_apoc="../verses/verses_apoc"
infile="versos_apocalipsis_con_terminacion"
outfile="02_ultimapalabra_versos_apocalipsis"

awk 'BEGIN{FS=","}{print $2}' "${src_apoc}/${infile}.csv" > "${infile}.tmp0.csv"
awk 'BEGIN{FS=" "}{print $NF}' "${infile}.tmp0.csv" > "${outfile}.csv"
sed -i "1d" "${outfile}.csv"
sed -i "1i ultimapalabra" "${outfile}.csv"

echo -e "VERSOS APOC: Se ha creado el archivo ${outfile}.csv"


rm ${infile}.tmp*.csv

