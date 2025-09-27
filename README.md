# File Counter Script

This repository contains a simple Bash script that counts the number of files in the `/etc` directory.

## Script Description

The script calculates:

* The number of files located directly in `/etc`
* The number of files inside its subdirectories
* The total number of files

## Usage

Make the script executable and run it:

```bash
chmod +x count_files.sh
sudo ./count_files.sh
```

> ⚠️ **Important:** Run the script with sudo to ensure access to all directories inside `/etc`. Without sudo, the script may show fewer files due to restricted access in some subdirectories.
