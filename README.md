<h1>Django Dockarize With Postgresql</h1>
<hr>
<h5>Prerequisite</h5>
<br>
<ol>
  <li>Install Docker in your local machine</li>
  <li>Install Python</li>
  <li>Install Postgresql</li>
</ol>
<br>
<h5>All The Example Code Was Given in "Dockerfile and docker-compose.yml" file</h5>
<h4>Commands</h4><br>
<br>
<p>Docker Version: </p> `sudo docker --version`
<p>Docker Compose Version: </p> `sudo docker-compose --version`
<p>Docker Info: </p> ` sudo docker info`
<p>Run Docker: </p> `sudo docker-compose up`
<p>Stop Docker: </p> `sudo docker-compose down`
<p>Run docker in Ditach Mode: </p> `sudo docker-compose up -d`
<p>Docker Logs: </p> `sudo docker-compose logs`
<p>Docker Build and RUN: </p> `sudo docker-compose up --build `
<p>Execute Python command throug docker: </p> `sudo docker-compose exec web python manage.py command(e.g: createsuperuser,makemigrations,migrate)'