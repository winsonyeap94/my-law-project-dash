FROM python:3.8.10-slim-buster

LABEL maintainer="My LAW Project"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# ODBC Drivers
RUN apt-get -y update \
    && apt-get -y install gcc g++

# Install pip requirements
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m pip install gunicorn

# Shift all codes to /app folder, otherwise there are many other folders in root
WORKDIR /home/my-law-project-dash/
COPY . /home/my-law-project-dash/

# Set PythonPath
ENV PYTHONPATH "${PYTHONPATH}:/home/my-law-project-dash/"

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser && chown -R appuser /home/my-law-project-dash/
USER appuser

# Exposing port
EXPOSE 1689

# Command to host app using gunicorn
CMD ["gunicorn", "-b", ":1689", "--workers", "4", "index:server", "--timeout" , "3600"]



