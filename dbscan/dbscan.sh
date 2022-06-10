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
### select number of cpus per task (you need to tweak this when you run a multi- thread program)
#SBATCH --cpus-per-task=1
### request 15 minutes of wall clock time (if you request less time, you can wait for less time to get your job run by the system, you need to have a good estimation of the run time though).
#SBATCH --time=18:00:00
### memory size required per node (this is important, you also need to estimate a upper bound)
#SBATCH --mem=128GB
### select the partition "def" (this is the default partition but you can change according to your application)
#SBATCH --partition=def

module load python/anaconda3

#python3 dbscan.py
#python3 labels.py
python3 results.py
