#!/bin/bash

src="../model"
infile="output_v10_40_temp0.075_temp0.5"
outfile="00_${infile}_cleanyears"

grep -v "0" "${src}/${infile}.txt" > "${outfile}.tmp0.txt"
grep -v "1" "${outfile}.tmp0.txt" > "${outfile}.tmp1.txt"
grep -v "2" "${outfile}.tmp1.txt" > "${outfile}.tmp2.txt"
grep -v "3" "${outfile}.tmp2.txt" > "${outfile}.tmp3.txt"
grep -v "4" "${outfile}.tmp3.txt" > "${outfile}.tmp4.txt"
grep -v "5" "${outfile}.tmp4.txt" > "${outfile}.tmp5.txt"
grep -v "6" "${outfile}.tmp5.txt" > "${outfile}.tmp6.txt"
grep -v "7" "${outfile}.tmp6.txt" > "${outfile}.tmp7.txt"
grep -v "8" "${outfile}.tmp7.txt" > "${outfile}.tmp8.txt"
grep -v "9" "${outfile}.tmp8.txt" > "${outfile}.txt"


rm ${outfile}.tmp*.txt


