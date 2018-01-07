#!/bin/bash

[ -f random_input.txt ] && rm random_input.txt
touch random_input.txt

while true; do
  read -p "Would you like to run decreasing? " yn
  case $yn in
    [Yy]* ) alg=../first_fit_decreasing;;
    [Nn]* ) alg=../first_fit;;
    * ) "Please answer yes or no";;
  esac
done

cnt=0
objects=0

while [ $cnt -le 30 ]; do
  while [ $objects -le 499 ]; do
    n=$(python -c "import random; print random.uniform(0.01,0.99)")
    echo $n >> random_input.txt
    ((objects++))
  done
  objects=0
  python $alg random_input.txt
  ((cnt++))
done
