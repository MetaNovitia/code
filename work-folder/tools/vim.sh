if   [ $(command -v vim) ] ; then
	vim $1
elif [ $(command -v vi) ] ; then
	vi $1
else
	echo "ERR: please install vim/vi"
fi