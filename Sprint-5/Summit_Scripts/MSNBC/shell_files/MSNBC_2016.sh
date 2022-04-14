#!/bin/bash
#SBATCH --job-name MSNBC_2016
#SBATCH --qos normal
#SBATCH --partition=shas
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time 00:15:00
#SBATCH --mail-type=all
#SBATCH --account=ucb-general

module purge

module load python/3.5.1
echo "== This is the scripting step! =="
python3 /projects/sebr8260/Summit_Scripts/MSNBC/scripts/MSNBC_2016.py
echo "== End of Job =="
