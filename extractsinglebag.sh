#!/bin/bash

file="$1"


mkdir -p ${file::-4}/
for topic in `rostopic list -b $file` ;
do rostopic echo -p -b $file $topic > ${file::-4}/${topic//\//_}.csv ;
echo "Iterating " $topic
done


