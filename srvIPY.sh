#!/bin/sh 
#
# ------------------
#$ -N srvIPY
#$ -S /bin/sh
##$ -o .out
##$ -e qsub.log
#$ -m es
#$ -l bigmem
#$ -l h_vmem=50g
# ---------------------------
#
# Execute the job from  the  current  working  directory
#$ -cwd
#$ -V
# All resources are defined here
#
# Choose your queue
#
##$ -q <queuename>
#
# Job priority
#
#$ -p 0
#
# ---------------------------
#
# Put compilations here
#
# ---------------------------
#
# Execution
#
python serve_ipython.py 8510 8511
