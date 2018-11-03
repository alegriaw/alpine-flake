# alpine-flake
this is a simple flake web app demo for docker

Here creates two Dockerfiles for the two apps(Blog/Home) and upload (push) the images to ECR using AWS cli commands.

The ALB gets request on port 80 and depending on the path (uri), it will redirect the request to the proper app: "/" to home and "/blog" to the blog app.

In other words, the ALB makes routing decisions at the application layer (HTTP/HTTPS), does path-based routing, and can route requests to the ports (5000 or 8081) on each container instances in our VPC.


Thanks to the reference:
https://www.bogotobogo.com/DevOps/AWS/aws-ELB-ALB-Application-Load-Balancer-ECS.php
