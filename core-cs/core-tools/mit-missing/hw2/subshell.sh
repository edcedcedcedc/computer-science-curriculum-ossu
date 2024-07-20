#!/bin/bash

(
  echo "Inside subshell: $BASH_SUBSHELL"
  inner_var="Hello"
  echo "Inner variable: $inner_var"
)

echo "Outside subshell: $BASH_SUBSHELL"
echo "Outer variable: $inner_var" 
