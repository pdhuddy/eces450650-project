#!/bin/bash
#SBATCH --mail-user=amb688@drexel.edu
#SBATCH --nodes=1
#SBATCH --cpus-per-task=48
#SBATCH --time=12:00:00
#SBATCH --partition=bm

module load python/anaconda3

python cleanup_parser.py > output.fasta
