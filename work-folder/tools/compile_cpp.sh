d=$(command -v g++-9)
if [ -z $d ] ; then
    g++ -std=c++11 $1 -o $2
else
	g++-9 -std=c++11 $1 -o $2
fi