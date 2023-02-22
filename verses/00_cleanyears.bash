#!/bin/bash

src="../model"
infile="output_v8_20"
outfile="00_${infile}_cleanyears"

grep -v "18" "${src}/${infile}.txt" > "${outfile}.tmp0.txt"
grep -v "19" "${outfile}.tmp0.txt" > "${outfile}.tmp1.txt"
grep -v "20" "${outfile}.tmp0.txt" > "${outfile}.txt"
rm ${outfile}.tmp*.txt


