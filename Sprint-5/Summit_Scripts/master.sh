#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:05:00
#SBATCH --partition=shas-testing
#SBATCH --output=sample-%j.out

module purge

module load python/3.5.1

echo "== This is the scripting step! =="
python3 /projects/sebr8260/Summit_Scripts/master.py
echo "== End of Job =="

