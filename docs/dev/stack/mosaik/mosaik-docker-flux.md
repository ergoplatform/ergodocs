# Ergo Mosaik: Build, dockerize and deploy 

In our Mosaik tutorial series, we've built a Mosaik app using Spring Boot. It runs perfectly on our
local machine, but what we really want is other people enjoying our application. These people might 
not want to deal with Gradle and Git, so let's see how we can bring our app to them!

All examples here are done to our Mosaik example app we've built in the tutorial series. You can 
find the [repository on GitHub](https://github.com/MrStahlfelge/mosaik-tutorial-series).

## Building the jar

Although we used Kotlin to write parts of our application, it compiles to a plain JAR file - a 
Java ARchive. That is a good thing: Java is a widely used language for applications and runs on all
desktop and server systems. The only prerequisite to run a JAR file is installing a JRE - a Java 
Runtime Environment - first.

Building the jar file for your Mosaik app based on Spring Boot is quite simple: You do it with the
`gradlew bootJar` command. When this finished, you will find your compiled jar in the `build/libs` 
subdirectory. It is named with the project name and version, so in our case it is 
`mosaikapp-0.0.1-SNAPSHOT.jar`. Try running it with `java -jar mosaikapp-0.0.1-SNAPSHOT.jar`: Your 
application starts up and the Mosaik app is served on your local network.

You can now give this JAR file to other people to run it, or run it on a server. For running it on 
a server, it often is needed to pack the application into a Docker container. We'll do that next!

## Dockerizing the jar

[Docker](https://docs.docker.com/) is an application to package and run your application within its
own predefined container. You already know that you need a JRE to run the application. With Docker, 
you can build an image with an installed Java and your application, and with predefined commands to 
run your application. This is not aiming to end users: for end users it is better to download JRE
and run your application manually. But on servers, it is very good to have an image defining what to
spin up and how, and Docker is usually available. It is also prerequisite to host your application 
on [Flux](https://runonflux.io/), which is a natural fit for dAps and Ergo is partnering with.

To dockerize your application, place a plain text file named `dockerfile` on the root level of your 
Mosaik app repo (next to `gradlew` and `build.gradle` files) with the following content:

        # syntax=docker/dockerfile:1
        FROM eclipse-temurin:17-jdk-jammy
        COPY build/libs/mosaikapp-0.0.1-SNAPSHOT.jar app.jar
        EXPOSE 8080
        ENTRYPOINT ["java","-jar","/app.jar"]

The first line is defining the docker file syntax and not interesting for us. The second line is
the most powerful one: It defines that our Docker image will built up on the definitions of a 
Docker image called `eclipse-temurin:17-jdk-jammy` - it is an image shipping a Java 17 JDK. 
Find more information on the [project page](https://hub.docker.com/_/eclipse-temurin).

The third line copies our jar we've built before into the Docker image, and the last line defines
running it is the "entry point" to the container image.

Our Spring Boot server runs on port 8080, so line 4 defines that this port is exposed when the image
runs in a Docker container.

With this file, we can build a Docker image. You'll need to install Docker on your system for this.
You'll find information how to do so on [Docker Docs](https://docs.docker.com/). When Docker is 
installed, you can build the Docker image with a command like the following

    docker build -t mosaikappexample:latest .

Don't miss the last character (point), it defines that `docker build` runs in the current directory. 
The `-t ...` 
parameter define a name and version tag for our image. When the build completes, you can run your 
image from Docker Desktop or command line and verify that your application works the same as run 
directly on your system. You can now push this image to remote Docker repositories to run it on 
other machines. There is also an [official dockerhub repository](https://hub.docker.com/) that 
you'll need to sign up for and push to to deploy on Flux.


## Deploy on Flux

You can deploy your jar or docker image on any hosting provider. We emphasize Flux here because it
is decentralized, can be paid with the Flux cryptocurrency and is very inexpensive for a Mosaik app.

Flux provides a [step by step guide](https://jetpack2.app.runonflux.io/#/launch/details) how to deploy an example 
app on their service. Besides the Docker image from the step before, you'll need a Zel ID and 
around 1 USD in Flux.

Follow the Flux guide to register your app, but take care on the following steps:

### Step 1  

#### App name
The app name defines on which URL your Mosaik app will be available later. Replace `127.0.0.1:8080`
with this URL in your app source before building the Docker image.

#### Owner / Zel ID

Don't confuse Zel ID with your ZelCore log in name. You find your Zel ID on the Zel ID app.

### Step 2 

#### Run command

You can leave it blank, our Docker image already defines its run command.

### Step 3 

#### Public port

You must enter a port here. Just enter 31000.

#### Domains

Leave it blank

#### Private ports

Enter 8080 here, as this was the port our Spring Boot process is listening on.

### Step 4

#### Instances

You can leave it at 3

#### Processors

Your Mosaik app will perform okay on 0.1 processors, but of course it will be three times faster 
with 0.3 processors. Go for 0.1 if you want it as cheap as possible, or more if you want a better
performance.

#### RAM

The Java process will take around 300 MB of RAM, so give it 1000 here to be safe to not run into 
problems. 

#### SSD space

Our image is around 750 MB in size, so give it 2 GB here to be safe.


## Deploy on other hosters

If you deployed to other hosters, feel free to enhance this guide.