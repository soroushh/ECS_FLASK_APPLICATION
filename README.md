# What

This repository is about deploying a simple flask application to AWS through 
AWS ECS.

# Deployment steps

1. You can complete the application in the app folder. You can add routes to the 
app defined in the app package.

2. You can create the nginx image and gunicorn image by the Dockerfiles defined 
in the root of the repository(This is for gunicorn container) and the Dockerfile 
in the nginx package(This is for nginx container) by running the following commands 
in the packages:

```
docker build -t <name_of_gunicorn_container>
```

```
docker build -t <name_of_nginx_container>
```

3. Create two repositories in the `AWS ECR` for pushing the docker images.

4. Push the `nginx` and `gunicorn` images that you created in step `2` to the 
created `ECR` repositories.

5. Use the image URLs that you created in step `4` in the `task-definition.json` file 
instead of `<your nginx reverse proxy image URL here>` and `<your app image URL here>`
and use the task-definition.json file ass the json file for creating a task 
definition in `AWS ECS Task Definitions` section.

6. Assign the created `task definition` in step `5` to a service in `AWS ECS`.


# Improvements
A CI/CD pipeline can be added to this project.
