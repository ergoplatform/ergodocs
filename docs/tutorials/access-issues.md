---
tags:
  - Access Issues
  - Wallet
  - Troubleshooting
  - Seed Phrase
  - Recovery
  - Guide
---

# Access Issues

This page provides solutions to common access issues that users may encounter with their Ergo wallets. It covers scenarios where you have your seed phrase but the restored wallet doesn't contain any ERG or shows a different address, and situations where you do not have your seed phrase. It also provides instructions on deriving additional addresses and best practices for storing your seed securely.

/// details | Your seed phrase / mnemonic
     {type: info, open: true}
A wallet is simply an *interface* for the blockchain, if you have your seed phrase, simply restore in one of our [wallets](wallets.md)
///

## I have my seed phrase but the wallet restored doesn't contain any ERG and is a different address

- **Were you using the Ergo mobile wallet or the Ergo Reference Client?**
    - **Yes**: Try [deriving additional addresses](#deriving-additional-addresses).
    - **Was the wallet created before October 18th, 2022?**
        - **Yes**: There was a [BIP32 key derivation bug](https://github.com/ergoplatform/ergo-appkit/pull/139) impacting certain wallets. Verify if your wallet was affected using [satergo.com](https://satergo.com/) which [checks this for you](https://t.me/Satergo/9509) when you restore.
- **How did you record your seed phrase?**
    - **Written down**: Are any characters hard to read or ambiguous? Refer to the [BIP-39 wordlist](https://www.blockplate.com/pages/bip-39-wordlist) for clarification.
    - **Screenshot**: Are you sure this mnemonic represents the wallet you are trying to recover?


## I do not have my seed phrase


- **using Yoroi?**: 
    - **Yes**: Decrypt the wallet using [yoroi-ergo-wallet-recover](https://github.com/satsen/yoroi-ergo-wallet-recover)
- **iOS Terminus / Ergo Mobile Wallet**:
    - **Do you still have access to the mobile wallet/Terminus but are facing a 'User not authenticated' error?**
        - **Yes**: This error often indicates a change in device credentials, possibly due to biometric changes or system updates.
        - **No**: Explore other recovery options
    - **Were you using the iOS Beta version?**
        - **Yes**: The developer may be able to reactivate the beta if asked nicely. Ensure to attempt resolving it yourself first.

## Deriving Additional Addresses

Ergo node uses a secret root key (derived from seed) for the change address

### In the Ergo Mobile Wallet / Terminus

Does the address that's been generated belong to the wallet you've restored? Check the derivation index and derive up to that number in `wallet config -> addresses -> derive more`

Simply select the wallet
### In the Reference Client/Node

Navigate to `localhost:9053/swagger#/wallet/walletDeriveKey` 

Click ***"Try it out"***

```bash
"derivationPath": "m/44'/429'/0'/0/0" 
```

- The wallet needs to be unlocked, and you need to authorize on top right on swagger
- Click execute and check the address you get in the response

## Best practices for storing your seed securely

If you've followed the steps above and managed to recover your funds, please store your seed inline with these best practices below to avoid further issues.


1. **Avoid Digital Storage**: Never store the seed phrase on digital devices prone to hacking.
2. **Physical Writing**: Write the seed phrase on paper or durable materials like metal.
3. **Secure Storage**: Keep it in a safe or lockbox, protected from theft and environmental damage.
4. **Redundancy**: Have multiple copies in different secure locations.
5. **Splitting**: Divide the seed phrase and store parts separately for added security.
6. **No Cloud Storage**: Avoid using cloud services for storing the seed phrase.
7. **Limit Access**: Restrict knowledge of the seed phrase's location to only essential individuals.
8. **Regular Checks**: Periodically verify the condition and security of the stored seed phrase.
9. **Use Reputable Services**: If using third-party storage, ensure they are trustworthy.
10. **Stay Informed**: Keep up-to-date with security practices and threats.
11. **Plan for Emergencies**: Arrange for the safe transfer of your seed phrase in case of death or incapacitation.
