# movies_rating
A Python program to get movies 'Rotten Tomatoes' rating from http://www.omdbapi.com/
Note: Tested on CentOS 7 with Python 2.7 & 3 or later.

Dependencies

        # Install epel-release to install pip
        yum install -y epel-release

        # Install python-pip
        yum install -y python-pip

        # Install Python module 'requests' using pip
        pip install requests


Dockerize Python program

        # Create docker file 'Dockerfile'

        # Build docker image using 'Dockerfile'
        docker build -t <image_name> .
        docker build -t movies_rating .

        # Verify docker image
        docker image ls
