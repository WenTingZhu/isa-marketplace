#!/bin/bash
# usage: bash start.sh
# if you want to reset all images and containers and then run: bash start.sh --reset
# If cannot modify files: chmod -R 777 ./*


# clean the repo so no migration issues occur
echo "Cleaning your local repository"
bash ./clean.sh

sleeptime=30

# these lines can be used to remove all images and containers thus totally resetting docker
if [ "$#" -eq  "1" ]; then
    if [ "$1" == "--reset-hard" ]; then
      sudo docker images | awk 'NR > 1 {print "sudo docker rmi -f "$3}' | sh
      sudo docker-compose stop
      sudo docker-compose rm
      sleeptime=90
    fi
    if [ "$1" == "--reset" ]; then
      sudo docker-compose stop
      sudo docker-compose rm
      sleeptime=45
    fi

fi


# note: this section can be removed if the files are eventually made different. Right now, they are the same so its easier to keep them consistent using these copy commands
# copy paste requirements.txt to all required containers
echo "Copying requirements.txt into each container"
cp requirements.txt batch/requirements.txt
cp requirements.txt experience/requirements.txt
cp requirements.txt frontend/requirements.txt
echo "Copying Dockerfile to each container"
# copy paste Dockerfile to all required containers
cp Dockerfile batch/Dockerfile
cp Dockerfile experience/Dockerfile
cp Dockerfile frontend/Dockerfile

echo "Running mysql container in the background"
# run mysql in the background
sudo docker-compose up mysql &

echo "Sleeping for $sleeptime seconds"
# wait for mysql to work. hopefully this is long enough, but not too long
sleep $sleeptime
echo "Running the remaining containers"
# make the rest work
sudo docker-compose up models experience frontend kafka batch es
