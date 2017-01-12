#! /bin/bash

touch error_img.txt
for i in $(ls ./frame_image);
do
	path=$(pwd)/frame_image/${i};
	echo ${path}
	./facedetect --cascade="classifier/cascade.xml" ${path};
	read -rsn1 key
	if [ "${key}" = "s" ]; then
		echo ${path}>>error_img.txt
	fi
done

	
