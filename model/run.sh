go build prcw.go

mkdir 0 1 2 3 4 5 6 7 8 9
cp prcw 0
cp prcw 1
cp prcw 2
cp prcw 3
cp prcw 4
cp prcw 5
cp prcw 6
cp prcw 7
cp prcw 8
cp prcw 9

cd 0
./prcw -o=0 -m=0 -r=0 > output.txt &
cd ../1
./prcw -o=0 -m=0 -r=1 > output.txt &
cd ../2
./prcw -o=0 -m=0 -r=2 > output.txt &
cd ../3
./prcw -o=0 -m=0 -r=3 > output.txt &
cd ../4
./prcw -o=0 -m=0 -r=4 > output.txt &
cd ../5
./prcw -o=0 -m=0 -r=5 > output.txt &
cd ../6
./prcw -o=0 -m=0 -r=6 > output.txt &
cd ../7
./prcw -o=0 -m=0 -r=7 > output.txt &
cd ../8
./prcw -o=0 -m=0 -r=8 > output.txt &
cd ../9
./prcw -o=0 -m=0 -r=9 > output.txt &
cd ..
