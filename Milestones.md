### Milestones
1. Create a simple REST API Webserver - In progress
   
- [x] README.md explaining the purpose
- [x] Maintaining dependencies in requirements.txt
- [ ] Makefile to build and run REST API locally
- [x] DB Schema migrations to create the student table
- [x] env to pass db url and other sensitive data
- [x] Postman collections for the APIs

#### API Expectations
- [x] Support API Versioning
- [x] Proper HTTP Verbs
- [x] Meaningful logs
- [x] /healhcheck endpoint
- [ ] Unit tests for all endpoints

2 - Containerise REST API
- [x] APIs run in a container
- [x] DB runs in a container

3 - Setup one-click local development setup
- [x] DML using Alembic
- [x] Make file for automated local installation

4 - Setup a CI pipeline
- [x] GitHub actions 
- [x] Local runner

5 - Deploy REST API & its dependent services on bare metal
- [x] Ngnix as reverse proxy
- [x] Ngnix as load balancer
- [x] Use Vagrant as a bare metal box - NA ( instead used Virtualbox VM directly)

6 - Setup Kubernetes cluster
- [x] Three node Kubernetes cluster using Minikube should be spun up.



## Later

- [ ] Redis cache

