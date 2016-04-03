#!/bin/bash

# clean the repo so no migration issues occur
echo "Cleaning your local repository"
bash ./clean.sh

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
sleep_time=45
echo "Sleeping for $sleep_time seconds"
# wait for mysql to work. hopefully this is long enough, but not too long
sleep $sleep_time
echo "Running the remaining containers"
# make the rest work
sudo docker-compose up models experience frontend kafka batch es
