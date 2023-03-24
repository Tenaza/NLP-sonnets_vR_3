#src_model="../verses/verses_model"
#infile_src="00_output_v10_15_temp075_temp75_cleanyears_verses_potenciales_con_terminacion"
#outfile="01_terminaciones_versos"

# TERMINACIONES MODELO
src_model="../verses/verses_model"
infile_src="00_output_v10_40_temp0.075_temp0.5_cleanyears_verses_potenciales_con_terminacion"
outfile="01_terminaciones_versos"

infile=${infile_src}
sed "1d" "${src_model}/${infile}.csv" > "${infile}_v2.tmp0.csv"
sed -i "1i terminacion2\" terminacion1" "${infile}_v2.tmp0.csv"

awk '{FS="\""}{print $2}' "${infile}_v2.tmp0.csv" > "${infile}_v2.tmp1.csv"
awk '{FS=","}{print $(NF-1), $NF}' "${infile}_v2.tmp1.csv" > "${infile}_v2.tmp2.csv"
awk '{FS="'\''"}{print $2$4}' "${infile}_v2.tmp2.csv" > "${outfile}_v2.csv"

sed -i "1d" "${outfile}_v2.csv"
sed -i "1i terminacion" "${outfile}_v2.csv"
echo -e "\nVERSOS MODEL: Se ha crado el archivo ${outfile}_v2.csv"

rm ${infile}_v2.tmp0.csv
rm ${infile}_v2.tmp1.csv
rm ${infile}_v2.tmp2.csv


# TERMINACIONES CITY
rm -r "01_terminaciones_by_city_v2"
mkdir "01_terminaciones_by_city_v2"
city_filename="../cities/00_ciudades_unicas.csv"

if [[ -f "$city_filename" ]]; then
    while IFS= read -r city
    do
        mkdir "01_terminaciones_by_city_v2/${city}"
        src_city="../verses/verses_cities/${city}"
        infile="${infile_src}_${city}"
        outfile="01_terminaciones_${city}"

        sed "1d" "${src_city}/${infile}.csv" > "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp0.csv"
        sed -i "1i terminacion2\" terminacion1" "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp0.csv"

        awk 'BEGIN{FS="\""}{print $2}' "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp0.csv" > "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp1.csv"
        awk '{FS=","}{print $(NF-1), $NF}' "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp1.csv" > "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp2.csv"
        awk '{FS="'\''"}{print $2$4}' "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp2.csv" > "01_terminaciones_by_city_v2/${city}/${outfile}_v2.csv"

        sed -i "1d" "01_terminaciones_by_city_v2/${city}/${outfile}_v2.csv"
        sed -i "1i terminacion" "01_terminaciones_by_city_v2/${city}/${outfile}_v2.csv"

        rm "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp0.csv"
        rm "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp1.csv"
        rm "01_terminaciones_by_city_v2/${city}/${infile}_v2.tmp2.csv"

    done < $city_filename
fi
echo -e "VERSOS CITY: Se ha creado la carpeta 01_terminaciones_by_city"


# TERMINACIONES APOCALIPSIS
src_apoc="../verses/verses_apoc"
infile="versos_apocalipsis_con_terminacion"
outfile="01_terminaciones_versos_apocalipsis"

sed "1d" "${src_apoc}/${infile}.csv" > "${infile}_v2.tmp0.csv"
sed -i "1i terminacion2\" terminacion1" "${infile}_v2.tmp0.csv"

awk '{FS="\""}{print $2}' "${infile}_v2.tmp0.csv" > "${infile}_v2.tmp1.csv"
awk '{FS=","}{print $(NF-1), $NF}' "${infile}_v2.tmp1.csv" > "${infile}_v2.tmp2.csv"
awk '{FS="'\''"}{print $2$4}' "${infile}_v2.tmp2.csv" > "${outfile}_v2.csv"

sed -i "1d" "${outfile}_v2.csv"
sed -i "1i terminacion" "${outfile}_v2.csv"

echo -e "VERSOS APOC: Se ha creado el archivo ${outfile}.csv"

rm ${infile}_v2.tmp*.csv

