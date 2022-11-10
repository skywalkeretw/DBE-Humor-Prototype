#!/bin/bash

# checkandupdate usage
# Funtion to keep container upto date 
# checkandupdate docker_image container_name port
checkandupdate () {
    # Pull image and check for any changes 
    docker pull ${1} | grep "Status: Image is up to date for ${1}" >/dev/null 2>&1
    PULLIMAGE="$?"

    # Check if Container is running 
    docker ps -a | grep "${2}" >/dev/null 2>&1
    CONTAINERRUNNING="$?"

    # if new image is available or container is not running
    if [[ "$PULLIMAGE" == "1" || "$CONTAINERRUNNING" == "1" ]]; then
        echo "New Image ${1} is available Downloaded"
        # if container is running stop and remove container
        if [[ "$CONTAINERRUNNING" == "0" ]]; then
            echo "Container ${2} is already running"
            # stop running container 
            docker stop ${2} >/dev/null 2>&1
            echo "Container ${2} has been stopped"
            # remove container
            docker rm ${2} >/dev/null 2>&1
            echo "Container ${2} has been removed"
        fi
        echo "Container ${2} has been started"
        # create container in detached mode
        docker run -d --name ${2} -p ${3}  ${1} >/dev/null 2>&1
    else
        echo "Image is up to date nothing to do"
    fi
}



checkandupdate lukeroy/humor-prototype-1:latest joke_ai 6969:8080