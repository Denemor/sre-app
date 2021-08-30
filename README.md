# Python sre-app api
Small API written on Python using Flask with exposed Prometheus metrics.  
By default app is listening on port `80`.

## How to build

### You can choose a two ways how to build the app:
* docker-compose
* docker cli

#### docker-compose
1) In case of docker-compose you should execute `docker-compose build` command.
2) In case if you want to run the application you should execute `docker-compose run` command.
3) In case if you want build and run the application you could execute `docker-compose run` command only.

#### docker cli
1) In case to build the app you can execute `docker build -t <image_name> <project_root>`, 
where <image_name> is a name of the desired image and <project_root> is path to the dir
where project is located. By default <project_root> is equal to the `.`.