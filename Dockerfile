FROM centos:8
RUN yum update -y && yum upgrade -y && \
    yum install python38 -y && \
    pip3 install Django && \
    pip3 install djangorestframework
COPY C:/Users/dk/PythonProjects/EcoApp app/
CMD python3 /app/manage.py runserver 0.0.0.0:8080