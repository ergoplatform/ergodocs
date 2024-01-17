# Windows

## Steps
1. [Install java runtime environment](https://www.oracle.com/java/technologies/javase-downloads.html)
2. [Get the latest Ergo node](https://github.com/ergoplatform/ergo/releases/)
3. Create the configuration files

```
ergo {
    directory = "C:\ergo"
    node {
        mining = false
    }
}
```
You can now follow the steps in the [tutorial](tutorial.md)

## WSL

See [this guide](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) or run this command in your terminal. This will enable the *Linux Subsystem* and allow you to execute as Linux. 

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 
```

You can then follow the steps outlines in the [Linux](linux.md) page. 

## Resources

- [How to set up and configure a full Ergo node on Windows - July, 2020](https://www.youtube.com/watch?v=fpEDJ1CM6ns)
