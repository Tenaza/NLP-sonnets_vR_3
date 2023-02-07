#!/bin/bash

src="../model"
infile="output_v6_20"
outfile="00_output_v6_20_cleanyears"

grep -v "18" "${src}/${infile}.txt" > "${outfile}.tmp0.txt"
grep -v "19" "${outfile}.tmp0.txt" > "${outfile}.tmp1.txt"
grep -v "20" "${outfile}.tmp0.txt" > "${outfile}.txt"
rm ${outfile}.tmp*.txt


