#! /bin/bash

TRAIN_FOLDER=$1 
POS_FILE_NUM=$2 
NEG_FILE_NUM=$3 
SAMPLE_NUM=$4 
SIDE_LEN=$5 
STAGE_NUM=$6 
# args
echo "  
TRAIN_FOLDER=$1 
POS_FILE_NUM=$2 
NEG_FILE_NUM=$3 
SAMPLE_NUM=$4 
SIDE_LEN=$5 
STAGE_NUM=$6 
"
echo "train from start?"
read -rsn1 key
if [ "${key}" = "y" ];then

if [ -d ./${TRAIN_FOLDER} ];then
	echo "ready"
else
	mkdir ${TRAIN_FOLDER}
	echo "input data in ${TRAIN_FOLDER}"
fi

cp ${TRAIN_FOLDER}/calssifier -r ${TRAIN_FOLDER}/calssifier_cp
rm ${TRAIN_FOLDER}/samples/*
rm ${TRAIN_FOLDER}/classifier/*
rm ${TRAIN_FOLDER}/samples.vec
find ${TRAIN_FOLDER}/positive_images -iname "*.jpg" > positives.txt
find ${TRAIN_FOLDER}/negative_images -iname "*.jpg" > negatives.txt


echo ${NEG_FILE_NUM}
perl bin/createsamples.pl positives.txt negatives.txt  ${TRAIN_FOLDER}/samples ${SAMPLE_NUM}\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
    -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w ${SIDE_LEN} -h ${SIDE_LEN}"
python ./tools/mergevec.py -v ${TRAIN_FOLDER}/samples/ -o ${TRAIN_FOLDER}/samples.vec
fi

opencv_traincascade -data ${TRAIN_FOLDER}/classifier -vec ${TRAIN_FOLDER}/samples.vec -bg negatives.txt  \
-numStages ${STAGE_NUM} -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos ${POS_FILE_NUM}  -numNeg ${NEG_FILE_NUM} \
-mode ALL -precalcValBufSize 1024  -precalcIdxBufSize 1024 -w 40 -h 40

#perl bin/createsamples.pl ./trainSet1/positives.txt ./trainSet1/negatives.txt ./trainSet1/samples 1000  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 50 -h 50"
#python ./tools/mergevec.py -v trainSet1/samples/ -o trainSet1/samples.vec

#opencv_traincascade -data trainSet1/classifier -vec ./trainSet1/samples.vec -bg negatives1.txt  -numStages 11 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 300  -numNeg 600 -w 50 -h 50 -mode ALL -precalcValBufSize 1024  -precalcIdxBufSize 1024
