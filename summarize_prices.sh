#!/bin/bash
awk -F, 'NR>1 {sum+=$2} END {print "Total price:", sum}' prices.csv