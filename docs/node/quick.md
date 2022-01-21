# Quick Install

Run the following command to

```
bash -c "$(curl -s https://node.phenotype.dev)"
```
source available on [GitHub](https://github.com/glasgowm148/ergoscripts)

# Prerequisities 
- Java
- Python
- Windows Subsystem if running Windows

## Java
```
curl -s "https://get.sdkman.io" | bash
sdk install java
```

Java 11 is recommended. 

## Python

```
# Ubuntu
sudo apt update && upgrade
sudo apt install python3 python3-pip ipython3

# OSX
brew install python
```



## Windows
See [this guide](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) or run this command in your terminal. This will enable the *Linux Subsystem* and allow you to execute as Linux. 

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 
```