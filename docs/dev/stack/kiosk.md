## ErgoScript playground using Kiosk

[Kiosk](https://github.com/scalahub/Kiosk) lets anyone play with ErgoScript using a basic web-based UI. In particular, it can do the following:

1. Define boxes with arbitrary ErgoScript code and register values
2. Create transaction outputting some predefined boxes



- An online instance of Kiosk for experimental use is deployed at [ergo.kioskweb.org/](https://ergo.kioskweb.org/)
- This is running the exact code from [GitHub](https://github.com/scalahub/Kiosk)
- **Please use the above instance only for experiments and not for transferring any large amounts.**
- For actual use, run your local instance as explained below. 


## Getting Started


Kiosk requires a fully configured Ergo node running and, by default, assumes that its REST API is available at http://localhost:9052. You can change this by calling the method `org.sh. Kiosk.ergo.ErgoAPI.setUrl` from the web-UI. 

A precompiled jar is available [here](https://github.com/scalahub/Kiosk/releases/tag/0.1), which can be run using `java -jar <jarfile>`. 
You can generate the jar from sources by issuing the command `sbt assembly`.

To run a local copy (which is the recommended way to use it), you must clone the project and do one of the following. 

1. Run sbt using the command `sbt`
Then inside the sbt prompt, type the following `jetty:start`
This will run the project using a built-in Jetty web server on port 8080, which you can access at http://localhost:8080

2. Compile the war file using the `sbt package`. (the file is in `target/scala-2.12` folder in my case). Then run the war file as you would run any other J2EE app. 

Kiosk currently depends only on ergo-appkit and uses the public explorer to post transactions. In particular, it does not require a local running Ergo node.

Signing is performed via Appkit, which replicates a large part of the Ergo node wallet's functionality locally. After all, both are JVM based).

The Kiosk is "multi-tenant" because each URL corresponds to a private copy of the script environment and box storage. Hence you can bookmark a URL and visit it later, and your declared variables and boxes should be present. Without the same URL, no one else will be able to see or modify your environment.

## Use

1. Set the environment to use in ErgoScript. This is a map of (key, value) pairs where keys will be referenced within ErgoScript code and set boxes' registers. See the first image.
![kiosk0|496x500](upload://jRDvlqHNHtIR8XtYuxH9rHk6H7P.png) 
2. Define one or more boxes using ErgoScript code and some registers if needed. See the second image.
![kiosk1|384x500](upload://nCYAcIqMsNby8myRYPsQG4Phb9s.png) 
3. Create and send a transaction with some given boxes defined earlier in Step 2. See the third image.
![kiosk3|690x272](upload://Wye2vnXTJJqgssPy3s4i8MH88c.png) 

The final output will be the transaction's ID and the request we made to the Ergo node's API.


