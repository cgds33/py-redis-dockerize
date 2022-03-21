## py-redis-dockerize

### 1. Summary

This project is a dockerize example with 4 containers. These are flask, redis, postgres and python worker containers. Proje was writed with docker-compose.

Flask container run on public network on port '80' and communicates on local network with other containers. 

Flask gets user information in json format with post requests. Redis queues incoming requests and send it to workers. User information sent to workers is saved in the database. 

<br>

### 2. Execute

for up containers with command line:

`docker-compose up --build`

<br>

### 3. Usage

Project have two endpoint:

#### a) '/', method=GET

Returns the information that the process is active 

#### b) '/api/user', method=POST

Saves user information to database with json. 

The submitted json takes 9 values and they are "id", "first_name", "last_name", "email", "gender", "ip_adress", "user_name", "agent", "country".

<br>

### 4. Implement your own project 

If you want to use that codes, you must don't forget change database and redis defauld passwords.

<br>
<br>
