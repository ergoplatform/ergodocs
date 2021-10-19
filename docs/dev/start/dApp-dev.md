# dApp Development

For most developers, [Appkit](#appkit) is the best entry point unless you're wanting to dive straight into [ErgoScript](#ergoscript) smart-contract development.

**System Architecture**

Below is a example system architecture diagram highlighting the main components of a decentralised application (dApp)


![](../assets/sys.png)

- **Front-end** | The user-interface built in your framework of choice.
    - For payments, we have the Yoroi dApp connector, proxy contracts, or Ergo-Pay. 
- **REST** | A *REST*ful API to interact with the backend
- **Backend** | Perform the off-chain logic
- **Database** (Optional) 
- **Contract** | Where the magic happens, the on-chain validation of the off-chain logic.



