# alpine-flake
This is a simple flake web app demo for docker

Here creates two Dockerfiles for the two apps(Blog/Home) and upload (push) the images to ECR using AWS cli commands.

The ALB gets request on port 80 and depending on the path (uri), it will redirect the request to the proper app: "/" to home and "/blog" to the blog app.

In other words, the ALB makes routing decisions at the application layer (HTTP/HTTPS), does path-based routing, and can route requests to the ports (5000 or 8081) on each container instances in our VPC.
### Prerequisites
```
Docker-ce 
git
```

### Build the Docker images
1. Create docker images for Blog/Home apps **under /src/Blog or /src/Home**, execute the following comment, for example:
```sh
$ docker build -t aws-demo-home . 
```
2. Check new created images
```sh
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
aws-demo-home       latest              c0e2b19a6f92        27 seconds ago       99.9MB
aws-demo-blog       latest              7d3c4cd33155        About a minute ago   99.9MB
```

### Push docker images to AWS ECR
3. Login to aws ECS, (note: set [$aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) first)
[update 2020/08] After AWS CLI 1.17.10, should authenticate Docker to an Amazon ECR registry with **get-login-password**, run the aws ecr get-login-password command. 
[$get-login-password (AWS CLI)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth)
```sh
$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 318503653371.dkr.ecr.us-east-2.amazonaws.com
```
4. Create a repo on aws ECR:
```sh
$ aws ecr create-repository --repository-name ecs-alb-with-flask/home
```
5. Create docker tags for your images
```sh
$ docker tag aws-demo-home:latest 318503653371.dkr.ecr.us-east-2.amazonaws.com/ecs-alb-with-flask/home:latest 
```
6. Push this image to your newly created AWS repository
```sh
$ docker push 318503653371.dkr.ecr.us-east-2.amazonaws.com/ecs-alb-with-flask/home:latest
```



**Thanks to the reference:**
[K Hong](https://www.bogotobogo.com/DevOps/AWS/aws-ELB-ALB-Application-Load-Balancer-ECS.php)
