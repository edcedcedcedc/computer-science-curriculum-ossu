#!/usr/bin/env bash

num=0
touch ex3report
echo $(date) >> ex3report
while true
do
 ((num++))
 n=$(( RANDOM % 100 ))	
 if [[ n -eq 42 ]]; then
   echo "Something went wrong" >> ex3report
   >&2 echo "The error was using magic numbers" >> ex3report
   echo $num >> ex3report
   exit 1
 fi

 echo "Everything went according to plan" >> ex3report
done

