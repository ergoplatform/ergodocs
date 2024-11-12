# Satergo Offline Vault

## About

An Android application that starts a Bluetooth Low Energy (BLE) service which accepts connections from other devices. The application stores your encrypted seed phrase and when the device connected to it (for example, a desktop computer with Satergo) requests things the user needs to accept them on the mobile device. This is more secure compared to keeping the wallet file on the computer where it is decrypted on that same computer when the password is entered, so malware could steal the seed phrase/private key and take all the funds if the computer is infected.

With Satergo Offline Vault, even if the computer is infected with malware, it will not matter because the Android mobile device never needs to connect to the internet and as such has a very low risk of getting infected with malware. The application will keep the seed phrase securely contained in the private directory of itself. Not the user nor other applications on an Android device can access another app's private folder (the one located at /data/data/ in the filesystem). The only way that could be accessed is with a full system root exploit which are rare nowadays and also would unlikely be possible to be performed remotely over Bluetooth. Official methods of rooting involve wiping the entire device which means that there is no way to even access the encrypted seed phrase without a very serious exploit.

The seed phrase is encrypted using AES and cannot be decrypted without the password that was originally used when creating/restoring the wallet.

## Example of how one might use it

- A user installs Satergo on his computer
- He chooses to create a new wallet using the Satergo Offline Vault feature
- He transfers the APK file of Satergo Offline Vault to his Android device without using internet (for example, over Bluetooth)
- He installs it on his Android device and creates a new wallet. This seed phrase is random and will never leave the device unless the user himself decrypts it using the "View seed" feature and enters it somewhere. As usual the seed phrase should be noted down on something that is not digital.
- The user pairs Satergo on his computer with Satergo Offline Vault on his phone
- Satergo now needs the public key of the wallet, so it requests it. Satergo on the computer cannot do anything until the user accepts the request that has now appeared on his Android device. The public key is not encrypted, so just accepting the request is enough.
- The user makes a transaction using Satergo (desktop), which then sends the unsigned transaction to the phone. As the seed phrase is encrypted, the user needs to enter his password on the phone to decrypt it and use it for signing the transaction. The seed phrase is never sent anywhere.
- The signatures are sent back to the Satergo wallet on the desktop, provided the user accepted the request on his phone after viewing what it would spend from the wallet.

## Tasks done in this ErgoHack

- Programmed an entire Android application that securely stores wallet details, starts a Bluetooth LE service and performs actions (signing transactions) with the confirmation of the user.
- Programmed (in a new branch of the Satergo git repository) a Linux implementation for the BLE service.

The application is working.

## More information

- The application will not be on the Google Play Store as that would need an internet connection to be downloaded.
- Other wallet programs are welcome to implement support for Satergo Offline Vault.

## Improvements that can be made

- Satergo should download the APK so that all the user needs to do is to transfer it and not have to download it as well.
- Satergo Offline Vault's implementation supports having multiple wallets, however this needs to be made available in the user interface as well.
- Support for other desktop operating systems. Since Bluetooth is differently implemented on each platform, the current implementation is only for Linux (bluez).

## Threat model

There is no code in app that sends your seed phrase anywhere. Whatever the device or application connected to your mobile device sends to it, it will not respond with anything except for:

- The application version (Sent without confirmation)
- The extended public key (Confirmation needed) which is used to derive the public addresses of the wallet
- Signatures for transactions (Confirmation & password needed)

In the case of Bluetooth vulnerabilities, even if an attacker would be able to establish a connection using one, they cannot access the private key because only the app can access it unless the device is rooted. This means that the Bluetooth vulnerability would need to have an exploit chain that also has a root exploit.

Root exploits are rare and are very serious as they give full control of the device to the attacker. Even if there was such an exploit it would not be able to access the contents of the file as it is encrypted with your password. A very sophisticated virus could however monitor everything on the phone and find the password when entered. Summary of what it would take:

- A full Android Bluetooth exploit
- A full Android root exploit that can be performed over Bluetooth, to install purpose-built malware on the device
- The user entering the password while still being near the attacker or connected to the internet

This is in my opinion very far-fetched.


