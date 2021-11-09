## ErgoScript playground using Kiosk
I created a tool called Kiosk that allows one to play with ErgoScript using a basic web-based UI. In particular, we can do the following:

1. Define boxes with arbitrary ErgoScript code and register values
2. Create transaction outputting some predefined boxes

URL: https://github.com/scalahub/Kiosk

An online instance of Kiosk for experimental use is deployed at https://ergo.kioskweb.org/
This is running the exact code at https://github.com/scalahub/Kiosk
Please use the above instance only for experiments and not for transferring any large amounts.
For actual use, run your local instance as explained below. 


Kiosk is opensource and written in Scala. To run it from source, first, clone the repository and do 
`sbt run` (requires [SBT](https://www.scala-sbt.org/release/docs/Setup.html) to be installed). The web-interface will open in http://localhost:8080

Kiosk requires a fully configured Ergo node running and by default assumes that its REST API is available at http://localhost:9052. This can be changed by calling the method `org.sh.kiosk.ergo.ErgoAPI.setUrl` from the web-UI. 

A precompiled jar is available [here](https://github.com/scalahub/Kiosk/releases/tag/0.1), which can be run using `java -jar <jarfile>`. 
You can generate the jar from sources by issuing the command `sbt assembly`.

Use it as follows:

1. Set the environment to use in ErgoScript. This is a map of (key, value) pairs where keys will be referenced within ErgoScript code and also for setting registers of boxes. See the first image.
![kiosk0|496x500](upload://jRDvlqHNHtIR8XtYuxH9rHk6H7P.png) 
2. Define one or more boxes using ErgoScript code and some registers if needed. See the second image.
![kiosk1|384x500](upload://nCYAcIqMsNby8myRYPsQG4Phb9s.png) 
3. Create and send a transaction with some given boxes defined earlier in Step 2. See the third image.
![kiosk3|690x272](upload://Wye2vnXTJJqgssPy3s4i8MH88c.png) 

The final output will be txid of the transaction along with the request that was made to the Ergo node's API.


To run you own copy (which is the right way to use it), you must clone the project and then do one of the following. 

1. Run sbt using the command `sbt`
Then inside sbt prompt type the following `jetty:start`
This will run the project using built in jetty web server on port 8080 which you can access at http://localhost:8080

2. Compile the war file using `sbt package`. (the file is in `target/scala-2.12` folder in my case). Then run the war file as you would run any other J2EE app. 

Kiosk currently depends only on ergo-appkit and uses the public explorer to post transactions. In particular it does not require a local running Ergo node.

Signing is performed via Appkit, which replicates a large part of the Ergo node wallet's functionality locally. after all both are JVM based).

Kiosk is "multi-tenant" because each URL corresponds to a private copy of the script environment and box storage. Hence you can bookmark a URL and visit it later, and your declared variables and boxes should be present. Without the same URL, no one else will be able to see or modify your environment.