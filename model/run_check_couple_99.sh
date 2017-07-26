#! /use/bin/env fish
# written by python script: generate_run_sh.py

mkdir -p 99; cd 99
cp ../prcw .

mkdir -p ./shift0_trial0
cd ./shift0_trial0; cp ../prcw .; ./prcw -m=99 -o=0 -r=0 > output.txt &
mkdir -p ../shift0_trial1
cd ../shift0_trial1; cp ../prcw .; ./prcw -m=99 -o=0 -r=1 > output.txt &
mkdir -p ../shift0_trial2
cd ../shift0_trial2; cp ../prcw .; ./prcw -m=99 -o=0 -r=2 > output.txt &
mkdir -p ../shift0_trial3
cd ../shift0_trial3; cp ../prcw .; ./prcw -m=99 -o=0 -r=3 > output.txt &
mkdir -p ../shift0_trial4
cd ../shift0_trial4; cp ../prcw .; ./prcw -m=99 -o=0 -r=4 > output.txt &
mkdir -p ../shift0_trial5
cd ../shift0_trial5; cp ../prcw .; ./prcw -m=99 -o=0 -r=5 > output.txt &
mkdir -p ../shift0_trial6
cd ../shift0_trial6; cp ../prcw .; ./prcw -m=99 -o=0 -r=6 > output.txt &
mkdir -p ../shift0_trial7
cd ../shift0_trial7; cp ../prcw .; ./prcw -m=99 -o=0 -r=7 > output.txt &
mkdir -p ../shift0_trial8
cd ../shift0_trial8; cp ../prcw .; ./prcw -m=99 -o=0 -r=8 > output.txt &
mkdir -p ../shift0_trial9
cd ../shift0_trial9; cp ../prcw .; ./prcw -m=99 -o=0 -r=9 > output.txt &

# mkdir -p ../shift0_trial10
# cd ../shift0_trial10; cp ../prcw .; ./prcw -m=99 -o=0 -r=10 > output.txt &
# mkdir -p ../shift0_trial11
# cd ../shift0_trial11; cp ../prcw .; ./prcw -m=99 -o=0 -r=11 > output.txt &
# mkdir -p ../shift0_trial12
# cd ../shift0_trial12; cp ../prcw .; ./prcw -m=99 -o=0 -r=12 > output.txt &
# mkdir -p ../shift0_trial13
# cd ../shift0_trial13; cp ../prcw .; ./prcw -m=99 -o=0 -r=13 > output.txt &
# mkdir -p ../shift0_trial14
# cd ../shift0_trial14; cp ../prcw .; ./prcw -m=99 -o=0 -r=14 > output.txt &
# mkdir -p ../shift0_trial15
# cd ../shift0_trial15; cp ../prcw .; ./prcw -m=99 -o=0 -r=15 > output.txt &
# mkdir -p ../shift0_trial16
# cd ../shift0_trial16; cp ../prcw .; ./prcw -m=99 -o=0 -r=16 > output.txt &
# mkdir -p ../shift0_trial17
# cd ../shift0_trial17; cp ../prcw .; ./prcw -m=99 -o=0 -r=17 > output.txt &
# mkdir -p ../shift0_trial18
# cd ../shift0_trial18; cp ../prcw .; ./prcw -m=99 -o=0 -r=18 > output.txt &
# mkdir -p ../shift0_trial19
# cd ../shift0_trial19; cp ../prcw .; ./prcw -m=99 -o=0 -r=19 > output.txt &

cd ..
