#!/bin/bash
#SBATCH --mail-user=amb688@drexel.edu
#SBATCH --nodes=1
#SBATCH --cpus-per-task=48
#SBATCH --time=12:00:00
#SBATCH --mem=1500GB
#SBATCH --partition=bm

module load python/anaconda3

pip install --user torch
pip install --user fair-esm

python pretrained_esm1b.py > output.pt
