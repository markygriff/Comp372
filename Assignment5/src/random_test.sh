#!/bin/bash
#
# Mark Griffith
#
# this script automates the testing of both the first-fit
# and first-fit-decreasing heuristic using random input data
#

[ -f random_input.txt ] && rm random_input.txt
touch random_input.txt

if [ "$#" -ne 1 ]; then
  echo usage: random_test.sh num_tests
  exit 1
fi

if [ $1 -le 0 ]; then
  echo please choose a positive number of tests to run.
  exit 1
fi

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
while [ $cnt -le $(($1-1)) ]; do
  while [ $objects -le 499 ]; do # 500 objects by default
    # append object sizes to the input file
    n=$(python -c "import random; print random.uniform(0.01,0.99)")
    echo $n >> random_input.txt
    ((objects++))
  done
  objects=0
  # run the chosen algorithm on the current input data
  python $alg random_input.txt
  ((cnt++))
done
