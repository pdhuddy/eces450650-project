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

#python esm1b_embed.py esm1b_t33_650M_UR50S /ifs/groups/eces450650Grp/data/incremental_data/engineered/batch-0.fasta /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/  \
#	 --truncate

#python esm1b_embed.py esm1b_t33_650M_UR50S /ifs/groups/eces450650Grp/data/incremental_data/engineered/batch-4-3.fasta /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/ \
#	--truncate

#python esm1b_embed.py esm1b_t33_650M_UR50S /ifs/groups/eces450650Grp/data/incremental_data/engineered/batch-4-4.fasta /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM \
#	--truncate

#python esm1b_embed.py esm1b_t33_650M_UR50S /ifs/groups/eces450650Grp/data/incremental_data/engineered/batch-4-2.fasta /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM \
#	--truncate

python esm1b_embed.py esm1b_t33_650M_UR50S /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/parsed-4-4.fasta /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/ESM/esm1b-0 \
       --include mean per_tok --truncate	
