# Запуск контейнера

Для корректного запуска контейнера необходимо использовать команду

```
sudo docker container run \
  --name jenkins-jenkins \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --publish 2443:2443 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins
```

Где myjenkins собраный образ из Dockerfile