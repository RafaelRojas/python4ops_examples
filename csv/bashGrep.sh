#!/bin/bash

grep Mexico SalesRecords.csv | grep -v grep | wc -l