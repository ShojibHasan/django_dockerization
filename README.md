<center><h1>Django Dockerize With Postgresql</h1></center>
<hr>
<h5>Prerequisite</h5>
<br>
<ol>
  <li>

  [Install Docker in your local machine](https://www.linuxtechi.com/install-use-docker-on-ubuntu/)

  </li>

  <li>
  
  [Install Python](https://celikmustafa89.medium.com/how-to-install-python3-10-on-ubuntu-20-04-lts-b4bbc4a11f8e)

  </li>
  <li>
  
  [Install Postgresql](https://www.ovhcloud.com/asia/community/tutorials/how-to-install-pg-ubuntu/)

  </li>
</ol>
<br>
<h5>All The Example Code Was Given in

[Dockerfile](https://github.com/ShojibHasan/django_dockerization/blob/main/Dockerfile) and 

[docker-compose.yml](https://github.com/ShojibHasan/django_dockerization/blob/main/docker-compose.yml)
file</h5>
<h4>Commands</h4>
<p>Docker Version: </p>

```
sudo docker --version
```
<p>Docker Compose Version: </p> 

```
sudo docker-compose --version
```

<p>Docker Info: </p>

```
sudo docker info
```
<p>Run Docker: </p> 

```
sudo docker-compose up
```
<p>Stop Docker: </p>

```
sudo docker-compose down
```
<p>Run docker in Ditach Mode: </p> 

```
sudo docker-compose up -d
```
<p>Docker Logs: </p>

```
sudo docker-compose logs
```
<p>Docker Build and RUN: </p>

```
sudo docker-compose up --build
```
<p>Execute Python command throug docker: </p>

```
sudo docker-compose exec web python manage.py createsuperuser(e.g: createsuperuser,makemigrations,migrate)
```