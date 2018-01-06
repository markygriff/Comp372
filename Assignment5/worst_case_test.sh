#!/bin/bash

[ -f worst_input.txt ] && rm worst_input.txt
touch worst_input.txt

cnt=0
objects=0
while [ $cnt -le 40 ]; do
  while [ $objects -le 500 ]; do
    echo 0.9 >> worst_input.txt
    ((objects++))
  done
  objects=0
  python first_fit.py test_input.txt
  ((cnt++))
done
