if   [ $(command -v g++-9) ] ; then
	g++-9 -std=c++11 $1 -o $2
elif [ $(command -v g++) ] ; then
    g++ -std=c++11 $1 -o $2
else
	echo "ERR: please install gcc"
fi