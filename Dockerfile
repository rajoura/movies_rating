FROM centos:7

# Install epel repo, python and pip to install requests module
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python python-pip && \
    yum clean all

# Install 'requests' python module
RUN pip install requests

# Copy the python script
COPY ./script/moviesrating.py /

# Modify file permissions
RUN chmod +x /moviesrating.py

ENTRYPOINT ["/moviesrating.py"]



