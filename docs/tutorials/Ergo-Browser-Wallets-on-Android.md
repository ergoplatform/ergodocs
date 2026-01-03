## Overview

To use the **[Nautilus](../dev/wallet/nautilus.md)** or **[Safew](../dev/wallet/safew.md)** Ergo wallet browser extensions on Android, you need a mobile browser that supports **Chrome extensions**. Most mobile browsers do not support this, but a few do.  

This guide will walk you through installing **Nautilus** or **Safew** wallets on mobile, to be used as a **supplement to the official [Ergo wallet app](https://ergoplatform.org/en/ergo-wallet-app/)**, rather than a full replacement.

Alternatively, a full desktop browser can be installed natively within Termux, and run via a minimal desktop environment, such as XFCE. This method brings full Ergo browser wallet functionality to Android. A guide for this setup can be found below under **Advanced Setup**.

---

## Expectations

This method **does work** for installing and using Ergo wallet browser extensions on Android. 
However, it is important to set realistic expectations:

- **Wallet functionality works** (view balances, manage addresses, sign transactions).
- **dApp connectivity for external sites usually does *not* work reliably**.
- Certain **built-in dApps inside the wallets do work**:
  - **Nautilus:** wallet optimizations, SigmaUSD protocol
  - **Safew:** token minter, mixer integration (requires local mixer running in termux)
- The extension wallets on Android should be treated as:
  - An **alternative wallet interface**, or
  - A **supplement** to the official Ergo mobile wallet app

---

## Supported Android Browsers

The following Android browsers support installing Chrome extensions and can run Ergo wallet extensions:

- **Quetta Browser** 
  Download: https://www.quetta.net/

- **Mises Browser** 
  Download: https://www.mises.site/

- **Lemur Browser** 
  Download: https://lemurbrowser.com/app/en.html

- **Kiwi Browser** *(discontinued — use with caution)* 
  Source code and builds: 
  https://github.com/kiwibrowser/src.next

---

## Getting Started (Quetta Browser & Mises Browser)

The steps below describe how to install and use the **Nautilus** or **Safew** Ergo wallet extensions on Android using browsers that support Chrome extensions.

---

### Option 1: Quetta Browser

1. **Install Quetta Browser**
   - Download Quetta Browser from: 
     https://www.quetta.net/
   - Install the APK and open the browser.

2. **Install the Wallet Extension**
   - After completing the initial setup tour, you will see a **Chrome Web Store shortcut** on the homepage.
   - Use this shortcut, or navigate manually to the Chrome Web Store and search for your preferred wallet:
     - Nautilus: 
       https://chromewebstore.google.com/detail/nautilus-wallet/gjlmehlldlphhljhpnlddaodbjjcchai
     - Safew: 
       https://chromewebstore.google.com/detail/safew-simple-and-fast-erg/fmpbldieijjehhalgjblbpgjmijencll
   - Tap **Add to Chrome** in the top-right corner and confirm installation.

3. **Verify Installation**
   - Open the main browser menu (three dots in the bottom-right corner near the address bar).
   - In the bottom row of icons, tap the **puzzle piece** icon to open the Extensions menu.
   - Confirm that the wallet extension appears in the list.
   - From this menu, you can manage extensions (enable private mode access, disable, or remove extensions).

4. **Open Wallet Extension Full-Screen**
   - To view Nautilus wallet in full screen as a new tab, click the **icon in the top-right corner** of the extension popup (an arrow pointing up out of a square).

5. **Set Up or Restore Wallet**
   - Create a new wallet or restore an existing wallet using your seed phrase.
   - Set a strong password.

---

### Option 2: Mises Browser

1. **Install Mises Browser**
   - Download Mises Browser from: 
     https://www.mises.site/
   - Install and launch the browser.

2. **Open the Extension Manager**
   - Tap the **puzzle piece** icon at the bottom of the screen (just left of the tabs icon).
   - Open the Extensions menu.
   - Chrome extension support is enabled by default, and a link to the Chrome Web Store is available here.

3. **Install the Wallet Extension**
   - Navigate to the Chrome Web Store:
     - Nautilus: 
       https://chromewebstore.google.com/detail/nautilus-wallet/gjlmehlldlphhljhpnlddaodbjjcchai
     - Safew: 
       https://chromewebstore.google.com/detail/safew-simple-and-fast-erg/fmpbldieijjehhalgjblbpgjmijencll
   - Tap **Add to Chrome** and approve the requested permissions.

4. **Access the Wallet**
   - Open the Extensions menu.
   - Launch Nautilus or Safew from the list.

5. **Open Nautilus Wallet Full-Screen**
   - Click the **icon in the top-right corner** of the extension popup to open it as a full-screen tab.

6. **Initialize the Wallet**
   - Create a new wallet or restore an existing one using your seed phrase.
   - Set a strong password.

---

## Notes & Limitations

- Extension popups may not render correctly on mobile.
- Most Ergo dApps **will not successfully connect** to extension wallets on Android browsers.
- Built-in dApps inside Nautilus and Safew **do work** (Nautilus: wallet optimizations, SigmaUSD protocol; Safew: token minter, [mixer](../eco/ergomixer/mixer-android.md) integration).
- Background execution and notifications are unreliable.
- This setup is **not recommended** for high-frequency or critical dApp usage.

---

## Advanced Setup, Fully Functional dApp Connector

This slightly more advanced method of using Nautilus or SAFEW wallets on Android requires two apps to function (Termux and Termux-X11). However, it will result in a desktop-like wallet experience, with all of the normal functionalities intact. This is a great option for users who want full access to Ergo dApps but only have an Android device (Android 8 or higher), without access to a desktop or laptop.

1. **Download Termux**
   - Termux must be downloaded from F-Droid. The play store version is incompatible.
   - Download Termux from F-Droid:
     https://f-droid.org/packages/com.termux/

2. **Download Termux-X11**
   - Termux-X11 is an X server app that will display the desktop environment.
   - Download the latest release of Termux-X11 from:
     https://github.com/termux/termux-x11/releases/tag/nightly
   - Select the correct apk for your devices architecture, and when its finished downloading, install the apk.
  
3. **Open Termux and Update**
   - Open the Termux app for the first time. It will install the bootstrap system, and configure itself.
   - Optionally, at this time you can install other packages which may be useful in the desktop environment later, such as termux-setup-storage, pulseaudio, etc.
   - update Termux:
     ```pkg update -y && pkg upgrade -y```
   - During the update, you may be prompted to confirm some settings. It is ok to choose the default by simply pressing enter.

4. **Install the Desktop Environment and Browser**
   - Now it is time to install the desktop environment and browser. For this guide, I will choose XFCE and firefox.
   - First, add the X-11 repository, and then install the termux-x11 package, which will add X graphics in Termux. Here are the commands:
   ```pkg i x11-repo -y && pkg i termux-x11-nightly -y```
   - Second, install the desktop environment (XFCE) and browser (Firefox) with this command:
     ```pkg i xfce firefox -y```

5. **Start the Desktop Environment**
   - On most devices the following command will start the desktop environment, and launch the Termux X-11 app. Start command:
   ```am start --user 0 -n com.termux.x11/com.termux.x11.MainActivity > /dev/null 2>&1 && sleep 1 && termux-x11 :1 -xstartup "dbus-launch --exit-with-session xfce4-session"```
   - And for older android devices, if above command doesnt work:
   ```am start --user 0 -n com.termux.x11/com.termux.x11.MainActivity > /dev/null 2>&1 && sleep 1 && env DISPLAY=:0 dbus-launch --exit-with-session xfce4-session```

6. **Launch Desktop Browser, Install Nautilus or SAFEW**
   - Familiarize yourself with the inputs of the Termux X-11 desktop environment. The screen acts as a trackpad, which controls the mouse pointer. A tap on the screen for left click, two finger tap for right click, selecting a text box and raising the onscreen keyboard and typing will enter text as expected.
   - Navigate to the applications menu located at the top left of the screen on the panel.
   - Launch Firefox by selecting it in the applications menu. It can be found under **Internet**
   - Go though Firefox's initial setup, then visit the Firefox addons store and install/enable your desired wallet. Here is the addons page for Nautilus:
     https://addons.mozilla.org/en-US/firefox/addon/nautilus

7. **Initialize and Use the Wallet**
   - The wallet extension can be found at the top right of Firefox, under the puzzle piece icon.
   - Optionally pin the wallet to the toolbar for easy access.
   - Open the wallet addon, and create or restore a wallet in the normal way.
   - You are now able to visit any site with the Nautilus dApp connector, and authenticate using the addon like normal.

---

## Security Recommendations

- Write down your seed phrase and store it offline.
- Do **not** store seed phrases in screenshots or cloud storage.
- Lock your device and browser when not in use.
- Avoid using extension wallets on shared, rooted, or compromised devices.
- Consider using a dedicated mobile device for wallet usage.
