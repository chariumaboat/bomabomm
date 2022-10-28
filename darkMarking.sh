#!/bin/sh
echo "word=" $1
echo "env=" $2

mkdir -p ./log/

statusIds="jogaiStatusId.csv"
userIds="jogaiUserId.csv"

if [ ! -e $statusIds ]; then
  touch $statusIds
fi

if [ ! -e $userIds ]; then
  touch $userIds
fi

if [ -e $statusIds ] && [ -e $userIds ]; then
  python darkMarking.py $1 $2 2>&1 | tee ./log/`date "+%Y%m%d_%H%M%S"`.log
fi


