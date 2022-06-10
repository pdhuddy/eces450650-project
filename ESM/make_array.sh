#!/bin/bash
#SBATCH --mail-user=amb688@drexel.edu
#SBATCH --nodes=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=1500GB
#SBATCH --partition=bm

module load python/anaconda3

pip install --user torch
pip install --user os
pip install --user numpy
pip install --user tempfile

python make_array.py
