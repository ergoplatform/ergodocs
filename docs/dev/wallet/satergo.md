# Satergo

## OS X 

1. Download .zip
2. Extract, move to `Applications` or somewhere else more appropriate. 
3. Double-click `run.command`, 



- On the 'full node' setup, hiding the download/continue button
- 'Open a new wallet' -> skip
- Restore button greyed out tries to save? 


During setup
- Mac version should have a readme.txt. (I can write this if you'd like)
- This error in CLI on boot WARNING: Unsupported JavaFX configuration: classes were loaded from 'unnamed module @359cc898'
- On the full node setup. Both `Download` and `Continue` are displayed. Bit counterintuitive as user is drawn to the right button first usually. I'd hide the second button until neeeded.
- May be a more effort than it's worth changing things, but a 'Skip for now' during wallet setup would let the sync start immediately, then the user could setup wallet and config at their leisure. Would also be good to have an option to select 'mainnet/testnet' here. 

In the app
- ERROR seems to be selected in the Node pane, but all INFO messages are streaming
- I'd have this off by default with a message in the box saying 'Click 'resume log' above to see messages from console'. 
- extra options under `...` might easily be missed. I'd just display these all on a second row. 
- Called 'java' instead of 'Satergo' in menu bar
- Stream makes the app laggy  (Unusual for apps on silicon IME)
- Trying to open the .conf file causes this error: https://pastebin.mozilla.org/y4jVvisg
