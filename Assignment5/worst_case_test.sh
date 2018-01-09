#!/bin/bash
#
# Mark Griffith
#
# this script automates the testing of both the first-fit
# and first-fit-decreasing heuristic using the worst case input data
#

[ -f worst_input.txt ] && rm worst_input.txt
touch worst_input.txt

while true; do
  read -p "Would you like to run decreasing? (y/n) " yn
  case $yn in
    [Yy]* ) alg="first_fit_decreasing.py"; break;;
    [Nn]* ) alg="first_fit.py"; break;;
    * ) "Please answer yes or no";;
  esac
done

cnt=0
objects=0
while [ $cnt -le 30 ]; do # 30 iterations by default
  while [ $objects -le 499 ]; do  # 500 objects by default
    # append object sizes to the input file
    echo 0.9 >> worst_input.txt
    ((objects++))
  done
  objects=0
  # run the chosen algorithm on the current input data
  python $alg worst_input.txt
  ((cnt++))
done
