# Mac



## Getting Started


### Prerequisites

**Java**

To run an Ergo node you need Java installed on your system. Version 9 or 11 is recommended.

```
curl -s "https://get.sdkman.io" | bash
sdk install java 11.0.13.8.1-amzn
```

Then run the following script to download the node and setup your `API` password

```
bash -c "$(curl -s https://node.phenotype.dev)"
```

You can track the status of the sync by comparing the heights found in [127.0.0.1:9053/info](http://127.0.0.1:9053/info) to the ones on the [explorer](https://explorer.ergoplatform.com/en/).


Please see the [troubleshooting page](troubleshooting.md) for more information.

## Run each startup

- Open System Preferences > Users & Groups > User ID (your nickname on the right)
- Now select the Login items tab .

To add the jar as a startup item, you'll need to create a wrapper shell script, set the permissions to allow execute, and then add it by pressing + and selecting the script.

