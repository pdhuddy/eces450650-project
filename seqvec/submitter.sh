#!/bin/bash
#
### !!! CHANGE !!! the email address to your drexel email
#SBATCH --mail-user=pdh46@drexel.edu
### !!! CHANGE !!! the account - you need to consult with the professor
#SBATCH --account=eces450650Prj
### select number of nodes (usually you need only 1 node)
#SBATCH --nodes=1
### select number of tasks per node
#SBATCH --ntasks=1
### select number of cpus per task (you need to tweak this when you run a multi-thread program)
#SBATCH --cpus-per-task=32
### request 48 hours of wall clock time (if you request less time, you can wait for less time to get your job run by the system, you need to have a good esitmation of the run time though).
#SBATCH --time=12:00:00
### memory size required per node (this is important, you also need to estimate a upper bound)
#SBATCH --mem=128GB
### select the partition "def" (this is the default partition but you can change according to your application)
#SBATCH --partition=def

module load python/anaconda3

# phil added this stuff to see if it would work
pip install --user torch
pip install --user 'allennlp==0.9.0'
pip uninstall overrides 
pip install --user 'overrides==3.1.0'


python seqvec_embedder.py -i /ifs/groups/eces450650Grp/data/incremental_data/engineered/batch-0.fasta -o /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/seqvec.npz --model /ifs/groups/eces450650Grp/ECES450650_SP22/projectE/model

### optionally, capture logs
#mkdir LOGS_${SLURM_JOB_ID}
#cp $TMP/qiime2*.log LOGS_${SLURM_JOB_ID}

