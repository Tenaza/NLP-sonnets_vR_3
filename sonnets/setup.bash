#!/bin/bash


city_filename="../cities/00_ciudades_unicas.csv"

if [[ -f "$city_filename" ]]; then
    while IFS= read -r city
    do
        mkdir "03_sonetos_by_city/$city"
    done < $city_filename
else
    echo -e "ERROR: $city_filename don't found.\n"
fi

