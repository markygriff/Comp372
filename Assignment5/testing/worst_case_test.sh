#!/bin/bash

[ -f worst_input.txt ] && rm worst_input.txt
touch worst_input.txt

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
    echo 0.9 >> worst_input.txt
    ((objects++))
  done
  objects=0
  python $alg worst_input.txt
  ((cnt++))
done
