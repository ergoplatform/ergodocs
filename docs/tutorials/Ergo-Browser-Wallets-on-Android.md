## Overview

There are three ways of using the **[Nautilus](../dev/wallet/nautilus.md)** or **[Safew](../dev/wallet/safew.md)** Ergo wallet browser extensions on Android.

Two of the options require a mobile browser that supports **Chrome extensions**. Most mobile browsers do not support this, but a few do. These mobile browser methods involve trade-offs between ease of setup, wallet version, and dApp compatibility.

The third option makes use of a full desktop browser, installed natively within Termux, and run via a minimal desktop environment, such as XFCE. This method brings full Ergo browser wallet functionality to Android using the most up to date version of Nautilus wallet. A guide for this setup can be found below under **Advanced Setup**.

This guide will walk you through installing **Nautilus** or **Safew** wallets on mobile, to be used as a **supplement to the official [Ergo wallet app](https://ergoplatform.org/en/ergo-wallet-app/)**, rather than a full replacement.

---

### Summary of Options (Easiest → Most Advanced)

There are three ways to use Nautilus on Android, listed below from easiest to most advanced:

- **Option 1:** Use the **latest release of Nautilus** in a mobile browser  
  *Easy setup, but the dApp connector is currently broken.*

- **Option 2:** Use **Nautilus release 0.9.4** in a mobile browser  
  *Easy setup with a fully functional dApp connector, but uses an outdated wallet version.*

- **Option 3:** Use **Termux with a desktop environment** on Android  
  *More complex setup, but provides the latest Nautilus release with a fully functional dApp connector.*
  
---

## Getting Started (Option 1 & 2)

The steps below describe how to install and use the **Nautilus** or **Safew** Ergo wallet extensions on Android using browsers that support Chrome extensions.

### Option 1: Quetta Browser, Latest Release of Nautilus (broken dApp connector) and SAFEW

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

### Option 2: Quetta Browser, Release 0.9.4 of Nautilus (working dApp connector)

1. **Install Quetta Browser**
   - Download Quetta Browser from: 
     https://www.quetta.net/
   - Install the APK and open the browser.
  
2. **Download Nautilus Release 0.9.4**
   - The last version of Nautilus that fully supports mobile browsers is release 0.9.4. Download ``nautilus-mainnet-0.9.4.zip`` from the release page:
     https://github.com/nautls/nautilus-wallet/releases/tag/v0.9.4

3. **Install the Wallet Extension**
   - Open the main browser menu (three dots in the bottom-right corner near the address bar).
   - In the bottom row of icons, tap the **puzzle piece** icon to open the Extensions menu.
   - Next, tap **Manage Extensions** to open the extensions options.
   - At the bottom of the manage extensions page, tap **Developer options...** it is in red text.
   - Install ``nautilus-mainnet-0.9.4.zip`` by tapping the button **(from .zip/.crx/.user.js)**
   - This will open your file explorer, where you will need to select the downloaded release from your downloads directory.
   - A successful install will result in a Nautilus wallet popping up in the extensions menu.

4. **Verify Installation**
   - Go back to the browsers home page, then open the main browser menu again (three dots in the bottom-right corner near the address bar).
   - In the bottom row of icons, tap the **puzzle piece** icon to open the Extensions menu.
   - Confirm that the wallet extension appears in the list.

5. **Open Wallet Extension Full-Screen**
   - To view Nautilus wallet in full screen as a new tab, click the **icon in the top-right corner** of the extension popup (an arrow pointing up out of a square).

6. **Set Up or Restore Wallet**
   - Create a new wallet or restore an existing wallet using your seed phrase.
   - Set a strong password.

7. **Use Ergo dApps**
   - Release 0.9.4 does work with dApps
   - Using dApps is exactly the same as on a desktop browser. Simply visit the dApp webpage, and connect Nautilus.
   - Nautilus will launch, and prompt you to accept the connection.

---

## Advanced Setup (Option 3)

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

## Security Recommendations

- Write down your seed phrase and store it offline.
- Do **not** store seed phrases in screenshots or cloud storage.
- Lock your device and browser when not in use.
- Avoid using extension wallets on shared, rooted, or compromised devices.
- Consider using a dedicated mobile device for wallet usage.

