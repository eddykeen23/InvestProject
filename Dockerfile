# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /InvestApp

# Set the working directory to /InvestApp
WORKDIR /InvestApp

# Copy the current directory contents into the container at /InvestApp
ADD . /InvestApp/

# Expose Port 8000
EXPOSE 8000

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install requests
RUN pip install psycopg2-binary

CMD ./manage.py runserver 0.0.0.0:8000