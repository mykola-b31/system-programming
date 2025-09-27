#!/bin/bash
files_in_etc=$(find /etc -maxdepth 1 -type f | wc -l)
files_in_subdirs=$(find /etc -mindepth 2 -type f | wc -l)
total_files=$((files_in_etc + files_in_subdirs))
echo "Number of files in /etc: $files_in_etc"
echo "Number of files in subdirs: $files_in_subdirs"
echo "Total files in /etc: $total_files"
