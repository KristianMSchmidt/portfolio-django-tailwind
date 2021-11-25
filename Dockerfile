FROM python:3.9

## Install node.js
RUN apt-get update
RUN apt-get install curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash
RUN apt-get install nodejs

# confirm that it was successful 
RUN node -v
# npm installs automatically 
RUN npm -v

# prevent Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1

# prevent Python from writing bytecode .pyc to disk
ENV PYTHONDONTWRITEBYTECODE 1


# Create working directory and copy project files
WORKDIR /code
COPY . /code

COPY Pipfile Pipfile.lock /code/

# Install pip, pipenv, and requirements
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --dev --deploy
