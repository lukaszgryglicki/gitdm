#!/bin/sh
PWD=`pwd`
cd ~/dev/kubernetes/
git config merge.renameLimit 10000
# git log -p -M | cncfdm.py -b /Users/mac/dev/gitdm/ > first_run.txt
git log -p -M | cncfdm.py -b /Users/mac/dev/gitdm/ -D -U -u -h first_run_patch.html -o first_run_patch.txt
git log --numstat -M | cncfdm.py -n -b /Users/mac/dev/gitdm/ -D -U -u -h first_run_numstat.html -o first_run_numstat.txt
git config --unset merge.renameLimit
cp first_run.txt ~/dev/gitdm/
cd $PWD

