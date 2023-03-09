# How to Set Up the Ergo Mixer on an Android Device

## Getting Started

Running ErgoMixer on an Android device is important because it enables an individual who may not own a desktop or laptop computer to take advantage of the privacy features available in ErgoMixer. It will make it possible for someone with a mobile device to utilize Ergo's Sigma protocols to enable efficient, trustless mixing of funds, enabling a high degree of privacy and security.

## Device Requirements

There are some minimum system requirements to run ErgoMixer on Android. Android OS of version 7.0 or higher, a minimum of 10GB of available storage, and a minimum of 1GB ram available for apps. So far, this has been tested and is working well on a Samsung Galaxy S8+.

## Prerequisites

A terminal emulator app is required to run an Ergo node on an Android device. The emulator app, Termux, has been tested and works well for running the node. To download Termux, you will need first to download and install [F-Droid](https://f-droid.org), an installable catalog of FOSS (Free and Open Source Software) applications for the Android platform. 

Within F-droid, search for `Termux - Terminal emulator with packages` and then download and install it.

## Installing Packages in Termux

The next step is to launch Termux and update and upgrade all packages. Using the default responses to all the prompts during the upgrade is okay.

```bash
pkg upgrade
```

Now install the package proot-distro. This is necessary to run OpenJDK-8 in Ubuntu, as it is currently unavailable for the base Linux environment in Android.

```bash
pkg install proot-distro
```

The next step is to download Ubuntu with proot-distro.

```bash
proot-distro install ubuntu
```

Now we need to log in to Ubuntu. 

```bash
proot-distro login ubuntu
```

And now, we need to update Ubuntu; then, we can install wget and OpenJDK-8.

```bash
apt-get update
```
```bash
apt-get install wget openjdk-8-jdk
```

## ErgoMixer Release Download & Running the Mixer

The next step is to download the latest release of ErgoMixer using wget. You can find the latest release [here.](https://github.com/ergoMixer/ergoMixBack/releases/tag/4.2.0)

```bash
wget https://github.com/ergoMixer/ergoMixBack/releases/download/4.2.0/ergoMixer-4.2.0.jar
```

And now, you can run the mixer with the following command:

```bash
java -jar ergoMixer-4.2.0.jar
```

In the event of a restart of the phone or after terminating Termux, the mixer can be started again by logging back into Ubuntu with `proot` and re-issuing the java command to start the mixer. 

## Accessing ErgoMixer Dashboard

At this point, the mixer will begin running on the device. To view the ErgoMixer dashboard, open a browser on the device and navigate to [http://0.0.0.0:9000/dashboard](http://0.0.0.0:9000/dashboard).

## Tips & Tricks

I recommend downloading a different keyboard to be used in Termux. The stock Samsung keyboard was not working well in my case. You can find a keyboard called Hacker's Keyboard in F-Droid that worked great for me.

Installing a package called tmux will help if you want to run other programs alongside the Ergo Mixer within Termux. It is possible to run the Ergo node in one tmux pane and the mixer in another.




