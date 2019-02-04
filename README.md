## Fibonnaci sequence generator api
- Made using:
   - django
   - django-rest-framework
   - django-rest-framework-swagger
- Deployed using:
   - docker
   - ansible

When running, open the api with http:<used_ip>:<used_port>/swagger/ to see test out and see basic curl usage.


## Deploy using docker (requires docker installed on your host)
-  Clone repo `git clone git@github.com:audriusb/fibo_sequence_sample_project.git`
- cd to cloned dir and build docker image `docker build -t fibo_api:latest .`
- run in docker with `docker run -it -p 8000:8000 fibo_api:latest`. Add `-d` after `run` part to make it detached as deamon.
- try opening `http://localost:8000/swagger`

## Deploy to remote hosts using ansible (required ansible-playbook installed on your host)

-  Clone repo `git clone git@github.com:audriusb/fibo_sequence_sample_project.git`
- `cd fibo_sequence_sample_project/ansible`
- edit `inventory.cfg` with hosts you need to deploy onto. Supported os: Debian, Ubuntu, CentOS 7, RHEL 7
- execute `ansible-playbook -b setup.yml -i inventory.cfg`
- relax and watch it deploy

## Docs

- Read the code. It has comments and is rather simple. Cheers.