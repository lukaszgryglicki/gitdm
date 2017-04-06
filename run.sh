#!/bin/sh
cd ~/dev/kubernetes/
git config merge.renameLimit 10000
git log -p -M | cncfdm.py -b /Users/mac/dev/gitdm/ > first_run.txt
git config --unset merge.renameLimit
cp first_run.txt ~/dev/gitdm/
cd ~/dev/gitdm/

