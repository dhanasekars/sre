## SRE Bootcamp Exercises

[Part one - From Local to Production](https://one2n.io/sre-bootcamp/sre-bootcamp-exercises)


## Prerequisites

The following tools/tech stacks are to be installed 

1. Brew / apt
2. Docker
3. Make
4. [Alembic](https://alembic.sqlalchemy.org/en/latest/front.html#installation)
5. Python 

## Project Structure

- API - Contains FastAPI endpoint and all it dependencies in requirements.txt and Docker file 
- ngnix - acts a reverse proxy and load balancer for FastAPI app.
- tests - unit and integration tests for all endpoints and functions
- Look at Makefile for one click local deployment



## Setup 

1. Clone repo
2. Create .env file in the root
```shell
    ENVIRONMENT=local
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_LOCAL_HOST=localhost:3306
    DATABASE_NAME=
    DATABASE_ROOT_USER_PWD=
```
3. run docker-compose
4. 





