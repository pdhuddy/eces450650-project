#!/bin/bash
#SBATCH --mail-user=zas37@drexel.edu
#SBATCH --nodes=1
#SBATCH --cpus-per-task=48
#SBATCH --time=12:00:00
#SBATCH --mem=1500GB
#SBATCH --partition=bm

module load python/anaconda3

python seqvec_embedder.py -i /ifs/groups/eces450650Grp/data/incremental_data/engineered/ -o /ifs/groups/eces450650Grp/ECES450650_SP22/projectE --model /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/model
