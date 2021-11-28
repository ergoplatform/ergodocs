## Initialize wallet

Restart the node and go to [http://127.0.0.1:9053/panel](http://127.0.0.1:9053/panel) to access the panel. Then set the API key secret from the previous step. Note that you need to set the **secret** and not the hash from the config file. In our example, this is the string `hello`. 

![set API key](https://user-images.githubusercontent.com/23208922/69916579-b7ca1680-1482-11ea-880e-251c8139a613.png)

Click on **Initialize wallet**. After the pop-up opens, there are two ways to proceed depending on your scenario.

1. If this is the first time you are running the node then you need to initialize it with a new mnemonic sentence.
2. If you had created a wallet earlier and would like to obtain the same address (possibly because there are funds stored in it), then you have to restore the wallet using the mnemonic sentence you had saved earlier. 

Follow one of the below steps depending on your situation. 

### Initialize wallet from scratch

![Initialize wallet](https://user-images.githubusercontent.com/23208922/69916584-d4fee500-1482-11ea-838c-e8aba9f41c76.png)

In the pop-up that opens, you must enter a wallet password. The mnemonic password is optional. After you click send, the wallet will return a mnemonic sentence as shown below. 

![mnemonic sentence](https://user-images.githubusercontent.com/23208922/69916693-2360b380-1484-11ea-9366-1bf9eb0f8b30.png)

You must copy this sentence and save it in a safe place. This sentence will be needed to restore the wallet on a different computer.

### Restore wallet from earlier

Copy the mnemonic sentence from earlier paste it into the "Mnemonic" field in the Restore-wallet form. Enter a secure wallet password. Leave the Mnemonic password empty (it is only for advanced users). Refer to the figure below.

![restore wallet](https://user-images.githubusercontent.com/23208922/71127599-66a37c00-2211-11ea-9b9e-9a69ac80c306.png)

After the wallet has been successfully restored from the mnemonic sentence, you will see a confirmation as shown in the figure below.

![successfully restored confirmation](https://user-images.githubusercontent.com/23208922/71127600-673c1280-2211-11ea-95eb-7c775c59180d.png)

### Get wallet addresses

This is a test to ensure you have set up the node properly. It will return the current addresses in the wallet. 
In the panel at [http://127.0.0.1:9053/panel](http://127.0.0.1:9053/panel) click on the `Wallet` tab on the left and then on `Get all wallet addresses` to view the addresses currently maintained by the wallet. It should return at least one address if the node is set correctly.

![Get addresses](https://user-images.githubusercontent.com/23208922/69978955-5b82f780-1553-11ea-85b6-413c63a46334.png)

### Check wallet balance

Once the node is synced, use the wallet API in the panel to see your balance, as shown below.

![check balance](https://user-images.githubusercontent.com/23208922/71127598-66a37c00-2211-11ea-9d53-f6d7738d1726.png)

### Sending funds

If there is a non-zero balance, you can send Ergs to any other address using the panel as shown below:

![send ergs](https://user-images.githubusercontent.com/23208922/71129066-a28c1080-2214-11ea-9806-7d768059980a.png)

