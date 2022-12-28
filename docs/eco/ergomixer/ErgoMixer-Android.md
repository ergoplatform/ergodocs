# How Set Up the Ergo Mixer on an Android Device

## Getting Started

Running the ErgoMixer on an Android device is important because it enables an idividual who may not own a desktop or laptop computer to take advantage of the privacy features available in the ErgoMixer. It will make it possible for someone with a mobile device to utilize Ergo's Sigma protocols to enable efficient, trustless mixing of funds, enabling a high degree of privacy and security.

### Device Requirements

To run the ErgoMixer on a device running Android OS, there are minimum system requirements. Android OS of version 7.0 or higher, a minimum of 10GB of available storage, and a minimum of 1GB ram available for apps. So far this has been tested and is working well on a Samsung Galaxy S8+.

### Prerequisites

To run the ErgoMixer on an Android device a terminal emulator app is required. The emulator app, Termux has been tested, and works well for running the mixer.. To download Termux you will need to first download and install F-Droid. 

F-Droid is an installable catalog of FOSS (Free and Open Source Software) applications for the Android platform. F-Droid is available at https://f-droid.org.

Within F-droid, search for “Termux - Terminal emulator with packages”. Download and install it. 

### Installing Packages in Termux

The next step is to launch Termux and update and upgrade all packages. It is ok to use the default responses to all the prompts during the upgrade.

```
pkg upgrade
```

Now install the package proot-distro. This is necessary to run openjdk-8 in Ubuntu, as it is currently unavailable for the base linux environment in Android.

```
pkg install proot-distro
```

The next step is to download Ubuntu with proot-distro.

```
proot-distro install ubuntu
```

Now we need to login to ubuntu. 

```
proot-distro login ubuntu
```

And now we need to update Ubuntu, then we can install wget and openjdk-8.

```
apt-get update
```
```
apt-get install wget openjdk-8-jdk
```

### ErgoMixer Release Download & Running the Mixer

The next step is to download the latest release of the ErgoMixer using wget. The latest release can be found [here.](https://github.com/ergoMixer/ergoMixBack/releases/tag/4.2.0)

```
wget https://github.com/ergoMixer/ergoMixBack/releases/download/4.2.0/ergoMixer-4.2.0.jar
```

And now the mixer can be run with the following command:

```
java -jar ergoMixer-4.2.0.jar
```

In the event of a restart of the phone, or after terminating termux, the way the mixer can be started again is by logging back into Ubuntu with proot and re-issuing the java command to start the mixer. 

### Accessing the ErgoMixer Dashboard

At this point the mixer will begin running on the device. To view the ErgoMixer dashboard, open a browser on the device, and go to http://0.0.0.0:9000/dashboard.

### Tips & Tricks

I recommend downloading a different keyboard to be used in Termux. The stock Samsung keyboard was not working well in my case. A keyboard called Hacker’s Keyboard can be found in F-Droid that worked great for me.

Installing a package called tmux will help if you would like to run other programs alongside the Ergo Mixer, within Termux. It is possible to run the Ergo node in one tmux pane, and the mixer in another.




