# The Ergonaut’s Guide to Privacy

## Introduction: Why Privacy Matters

As the world of Web3 and Decentralized Finance continues to grow, this technology is changing the way individuals access financial tools around the globe. We have had our first glimpse into what kind of world this powerful new paradigm of decentralization can produce, and there is no telling where the next decade will take us. Projects like Ergo are working non-stop to deliver on the promises of the cypherpunk dream: fair, accessible, and individually sovereign financial tools. While progress has continued to inspire hope, this age of decentralization also comes with significant changes to the way we must take responsibility for our own well-being, forcing us to stop relying on others to manage our funds, files, and passwords. At the forefront of these responsibilities are Privacy and Security. 

While privacy in the crypto space can be conflated with criminal activity, this is simply not the case. Average individuals need privacy; it is a fundamental right. Privacy ensures that individuals have control over their personal information. It is necessary for maintaining safety; it helps protect individuals from identity theft, cyberstalking, harassment, and physical threats. In an era where online transactions are becoming the norm, privacy is necessary to prevent individuals' financial data and personal information from being misused. To disregard one’s own privacy is to disregard one’s own safety. Furthermore, privacy is also critical for maintaining social and political freedom. Without the ability to limit the personally sensitive information available online, we are at the mercy of all who have access to it. For the same reasons that you may not want to publish your Google search history, it is also wise to keep personal transactions, communications, and activity to yourself. In a society where personal beliefs and opinions are increasingly scrutinized, privacy ensures that individuals can live without fear of retribution or manipulation.

However, privacy cannot be achieved without security. Security is the means to protect individuals' personal data from malicious attacks and breaches. While it may be beyond the average user’s ability to run a phishing scam or hack into someone’s device, it is well within our ability to take the simple steps necessary to ensure that we are securing our most vital and valuable information. Together, in the world of decentralized finance, privacy and security are two of the most critical guiding principles to maintain the individual sovereignty and freedom intended by the creators of cryptocurrency. 

The following course is designed to provide you with the necessary tools and knowledge to protect your digital identity and financial assets. We will cover essential topics such as creating secure passwords, enabling two-factor authentication, setting up a VPN, and protecting your machine from malware and viruses. We will also explore how to maintain private online communications and use Tor to enhance your web browsing privacy. Finally, we will dive into privacy on the blockchain and provide practical guidance on setting up a cold wallet, installing the mixer, creating a private wallet, and sending and receiving funds privately. 

All information in this course is publicly available. Its creator is in no way responsible for the privacy, security, or actions of any user(s) who make use of this information. Please be kind and behave responsibly. 

## General Privacy Preserving Practices

The following strategies will be helpful for maintaining privacy and security for all internet users, not only those accessing DeFi or making crypto transactions. 


### Creating Secure Passwords

The most basic way to ensure privacy and security is to use strong passwords. Weak passwords are those that are easy for computers to solve by ‘brute force’ or easy for an adversary to guess because they contain obvious, publicly available information. Weak passwords are also those which have been reused across sites or simply ‘updated’ by adding an extra digit onto the old versions. Do not do this, especially for sites that contain personally identifiable information. Strong passwords contain a combination of uppercase and lowercase letters, numbers, and symbols, and are at least 14 characters long. A password that contains this level of complexity would require >200 Million years to be cracked, while an 8 character password with the same requirements would be solved in a single day. 

If you are hesitant to create such complex passwords, passphrases can be helpful. A passphrase is an easier-to-remember string of words with selected characters replaced with numbers and symbols. For example, I could use the phrase “super private wallet” to create the passphrase, S00p3rPr1v@teW@11et. It is also quite helpful to use a password manager to keep track of your many, unrepeated, highly complex passwords across many different sites. Just be sure your master password is formidable. See you in a quadrillion years, hackers! 

If your passwords do not make it into the green on this chart, change them now. 

### Enabling Two-Factor Authentication

Two-factor authentication (2FA) is an additional layer of security that protects your online accounts from unauthorized access. 2FA requires users to provide two forms of identification, typically a password and a one-time code generated through an authentication app, to log in to their accounts. This adds an extra layer of protection as even if someone has your password, they won't be able to access your account without the second factor. This helps protect against hacking, identity theft, and other types of online fraud. 

2FA is available for most traditional financial applications, such as a bank website, and on major crypto exchanges, such as Coinbase. To enable 2FA, you'll need to log in to the account that you want to secure and navigate to the security settings. From there, select the 2FA option, and choose the method you prefer, such as a phone application, text message, email, or physical 2FA key (e.g. Yubico). Follow the steps to set it up and make sure to keep a backup of your backup codes in case you lose access to your primary 2FA method. Overall, enabling 2FA is a simple but effective way to enhance the security of your online accounts and protect your personal information from unauthorized access.

While 2FA is not available for use in Ergo wallets, per se, it will protect your other accounts and your machine. If you are looking for something similar to 2FA to protect your crypto, see the section below on cold wallets, and be on the lookout for multi-signature features that could simulate a 2FA between wallets on your browser and your phone. 

### Protecting Your Machine

​​As simple as it sounds, installing security updates is crucial for maintaining the security of your computer. Software vulnerabilities can be exploited by hackers and malware to gain access to your machine, steal your personal information (like your super complex passwords), or cause damage to your system. Security updates often contain patches for these vulnerabilities and other security issues, which help protect your computer from potential attacks. By keeping your computer up to date with the latest security updates, you can reduce the risk of security breaches and ensure that your personal information remains safe. It's important to set your computer to automatically download and install updates, or check for updates regularly to ensure that you're always running the most secure version of the software.

### Maintaining Private Online Communications

Most people today use the internet to send messages or participate in social media. However, many fail to recognize that these services can compromise privacy and security. Messages and conversations exchanged through social media platforms and messaging apps can be easily intercepted by third parties. This puts users at risk of being identified personally and targeted for digital or even physical attacks. Furthermore, social media platforms collect and use personal data for advertising and other purposes, often without the user's explicit consent. Beyond targeting you with ads based on your browsing history, this leaves you at the mercy of whomever is collecting this data to handle it responsibly. Finally, using social media and messaging apps may expose users to malicious links, spam, or phishing attacks. This can lead to a number of attacks that end with your identity being stolen, your accounts being hacked, or your machine being compromised entirely. 

It is critical for users to be aware of all the ways they can inadvertently expose themselves to such risks when communicating online, and it is important to follow a few key rules. First, only share sensitive information through encrypted messages or secure channels, especially when discussing financial information or personal data. Second, avoid clicking on suspicious links or downloading attachments from unknown senders, as they may contain malware or viruses. Thirdly, limit the personal information you share online, including on social media profiles or in public chat groups. If adversaries can identify you and link your communications to other accounts or sources of information, they can track and attack you. Finally, avoid associating private or pseudonymous accounts with your public accounts. This includes sending yourself messages, liking posts, or, in highly sensitive cases, accessing these accounts from the same IP address. By following these rules, you can remain online without compromising your identity.

The previous steps are relatively simple. They only require basic knowledge to implement and 100% of users should be able use this knowledge without issue. However, some users may find the next two steps to be ‘overkill’. That is for each user to decide. The larger you have at stake, the more seriously you should consider taking one of the following steps: VPN & Tor. 

### Setting Up a VPN

A VPN, or virtual private network, is a tool that creates a secure and encrypted connection between your device and the broader internet. It works by encrypting and routing your internet traffic through a remote server, which then accesses the internet on your behalf. This makes it appear as if your device is connected to the internet from a different location. This means that anyone watching your local network will be unaware of this connection or your activity, and anyone observing you online will be unable to locate you in the physical world. While it is most obvious to use a VPN while accessing public wi-fi that could be compromised or altogether fraudulent, users should consider using them from home as well, especially if you are conducting financial activity online. 

To set up and use a VPN, begin with the following: 
- Select a reputable provider. ExpressVPN.com is a popular option. Whether choosing this option or others, users should seriously consider a paid service, rather than something that is free. While the free option is (probably) better than nothing, free means that you are the product and someone is likely making money off of your data somehow. 
- Download the client or browser extension. 
- Log in. 
- Select the remote server you wish to connect to. You may or may not have a preference based on your location, the activity you wish to engage in, and the location of the server. 
- Connect to the server, and you are good to go. You may want to enable a ‘kill switch’ that shuts off your internet if the VPN server goes down, to limit the risk of exposing your IP address. 

### Tor Browser

Tor (The Onion Router) is a free and open-source software that provides anonymous communication and web browsing on the internet. It works by routing internet traffic through a network of servers and relays, making it difficult to track the user's online activity and location. The traffic is encrypted and sent through a series of nodes in the Tor network, which are operated by volunteers worldwide. Each node only knows the previous and next node in the circuit, ensuring that no single node can see the entire path of the data. Thus, Tor can be used to access the internet anonymously and to bypass internet censorship and surveillance. It is important to note, however, that Tor is not foolproof and there are still ways that users can compromise their anonymity while using the network. 

To use Tor, you'll need to download and install the Tor Browser. Here are the steps to do so:

- Go to the Tor Project website at https://www.torproject.org/download/ and download the appropriate version of the Tor Browser for your operating system.
- Once the download is complete, open the installation file and follow the instructions to install the Tor Browser.
- After the installation is complete, open the Tor Browser.
- The Tor Browser should automatically connect to the Tor network and open a new window with the Tor Browser home page.

From there, you can use the Tor Browser like any other web browser to access websites anonymously. There are many features that you will be familiar with in the Tor browser, such as search functionality or browser extensions, and some that you may not have used before, such as the various security settings that limit what can be displayed in your browser. Explore https://www.torproject.org to learn more about these advanced features, or learn more about them on youtube. 

The advantage of Tor over a VPN is that Tor is more decentralised and does not require you to trust a third party. Using a VPN allows you to choose which centralised entity to handle your traffic, but in theory, they could also abuse your data. The advantage of a VPN over Tor is that it will route your entire internet connection through the remote server, while Tor simply secures the information sent and received through its browser. Depending on what VPN you use and how much you pay, you may also have more bandwidth than what Tor can provide. Advanced users may choose to connect to a VPN first, and then use the Tor Browser to try and get the best of both worlds. 

Finally, it is important for users to realize that even when using a VPN and/or the Tor Browser, you can still download and run malicious programs that will compromise your machine and any sensitive information contained on it. You should be cautious about what you access online and only download things from trusted parties. Downloading things from random places across the internet is a surefire way to get hacked. 

## Privacy on the Blockchain

The following topics are related to privacy and security in crypto, specifically.

### Protecting Your Seed Phrases

In crypto, your seed phrase is everything. This is the 15 to 24 words that can be used to restore your wallet on any device, without any more information. Most wallets will only show you this information at the time of creation, so you must take care to record it correctly and store it safely. This is the most sensitive information you possess; if your seed phrase is compromised, your funds are as good as stolen. If you lose your seed phrase, or copy it incorrectly, the funds in that wallet will not be accessible to you or anyone else. It is absolutely imperative that you double check and securely store your seed phrases. Failure to do so will result in a loss of funds, with no way to get them back. 

So, what is the best way to store your seed phrase? The gold standard is to stamp or engrave your seed phrase into steel plates and store them securely in a private location. It is not advised to trust anyone else (including a safety deposit box) with seed phrase storage. However, you may wish to store only portions of your phrase with trusted parties, which you could access in an emergency. For example, you may store a third of your phrase with your parents and siblings, who would be trusted to give it back when you needed it. Kits for this purpose can be found on Amazon or through a number of private sellers. See examples here. 

If you are unable to obtain or store steel plates, or if you do not wish to immortalize every single wallet you use, there are less permanent options. Simply writing seed phrases on paper can be effective, so long as this paper is safely stored (in a book or picture frame, for example). In choosing this method, however, you are acknowledging that it will not survive a fire or flood. This method should not be used for wallets containing significant funds. 

It is important to note that storing seed phrases online is not advised. Exposing your phrase online to any extent is dangerous, no matter how secure your password is. Do not record your seed phrases in a google doc or anything similar. If you must record your seed phrase online, only do so in a non-obvious and encrypted way. An example of this is using steganography, which embeds a coded message into a digital image. That being said, please do not store your seed phrase directly online, including taking pictures of it or trying to scramble it yourself. Remember the calculations for brute forcing a password??? Don’t do it. 

For the highest level of security with your seed phrases, please also see the section below about private cold wallets and hardware wallets.

## Setting Up the Mixer

Given that most users are required to complete KYC in order to purchase crypto, the only way to achieve anonymity is through privacy coins or a mixer. Since we are all Ergonauts here, I will describe how to set up and use the mixer to create an anonymous wallet (See CW’s fantastic overview here).

About the ErgoMixer: This is a local application that runs on the user’s machine alone. This means that no third parties have to be trusted to operate the mixer. It is capable of mixing all native Ergo assets, however, it is limited to those with liquidity in the mixer. It works by combining funds from every mixer user and then redistributing the funds in appropriate amounts. This essentially means that, with enough users in the pool, funds sent through the mixer cannot be traced. 

### Installing the mixer: 
- Ensure you have JDK8+ installed on your machine. 
- Go to https://github.com/ergoMixer/ergoMixBack 
- On the right hand side of the screen, click on the latest release of the mixer. As of January 2023, that would be version 4.3.0. 
- Download the file (.jar for unix, .dmg for mac, .exe for windows)
- Install the mixer on your machine

### Sending funds:

- Click Active Mixes
- Start New Mix
- Select the token you wish to mix and click next
- Decide how to distribute the tokens (smaller or larger boxes) and click next. 
- Note the ring activity. More activity means faster and more private mixing.
- Set withdrawal address (where you want the funds to go) and click next
- Set the mixing level and note the mixing fee
- Click ‘start mixing’, then deposit the total amount (mixing amount + fee) to the address indicated. 

### Covert address: 

A covert address allows you to share an address publicly without exposing your personal wallet. Imagine owning a shop- this will allow customers to send you funds without letting them see your actual address. 

- Click covert address
- Click new covert address
- Name the address
- Select the mixing level
- Add withdrawal addresses (the more the better)
- Click create covert address

Recently, the SAFEW wallet integrated mixer functionality directly into the wallet. This allows users to send funds through the mixer right from their wallet. Granted, this will not be as private as using the mixer directly, but it is quite simple and accessible. 

### Creating Private Wallets
Now that you know how to use the mixer, you can use it to create an anonymous wallet. This anonymous wallet may be useful for maintaining privacy while interacting with DeFi applications or with others online. It may be helpful in maintaining a pseudonym on social media with a known address, without that address being linked to your true identity. To create a private wallet follow these steps: First, create a brand new wallet. Second, send funds from a non-private wallet through the mixer to this new wallet. It is best to send a few mixed transactions, rather than just a single one, and spread them out over time. 

This new wallet will have funds and no association to your identity or public addresses. Activity in this wallet will be separated from those addresses until you break that anonymity by either revealing personal information (sending money to someone who knows you personally from that wallet) or by sending funds from that wallet to one of your own public addresses. If you wish to maintain the anonymity of this wallet, do not use it in association with your identity or any of your publicly known addresses, and use a VPN when accessing it. 

The wallet described above is what is known as a ‘Hot Wallet’, meaning that it is connected to a computer and is available for use online. A ‘Cold Wallet’, on the other hand, is a wallet that is not, and has never been, connected to the internet. 
Hardware Wallets

### Sending and Receiving Funds Privately

Caution: Nothing is 100% Private

Avoiding Privacy Leaks
The following infographic is meant to serve as a brief guide for maintaining privacy.


**To-Do List**

- Use a strong password
- Use 2FA
- Update your machine
- Maintain anonymous / pseudonymous accounts
- Use encrypted messaging
- Use a VPN
- Use the Tor Browser
- Secure your seed phrase
- Use the mixer to send funds
- Use a cold wallet
- Use a hardware wallet

**Not-To-Do List**

- Reuse passwords across sites
- Send information between private & public accounts
- Send funds between private & public wallets
- Share personally identifiable information
- Use or download untrusted applications
- Public Wi-Fi use without a VPN
- Ad Personalization


