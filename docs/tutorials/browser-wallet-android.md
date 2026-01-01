## Using Chrome Extension Ergo Wallets (Nautilus or Safew) on Android

To use the [Nautilus](dev/wallet/nautilus/) or [Safew](dev/wallet/safew) Ergo wallet browser extensions on Android, you need a mobile browser that supports **Chrome extensions**. Most mobile browsers do not support this, but a few do.

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
- Most Ergo dApps **will not successfully connect** to extension wallets on Android.
- Built-in dApps inside Nautilus and Safew **do work** (Nautilus: wallet optimizations, SigmaUSD protocol; Safew: token minter, [mixer](eco/ergomixer/mixer-android.md) integration).
- Desktop site mode may be required for some pages but does not guarantee compatibility.
- Background execution and notifications are unreliable.
- This setup is **not recommended** for high-frequency or critical dApp usage.

---

## Security Recommendations

- Write down your seed phrase and store it offline.
- Do **not** store seed phrases in screenshots or cloud storage.
- Lock your device and browser when not in use.
- Avoid using extension wallets on shared, rooted, or compromised devices.
- Consider using a dedicated mobile device for wallet usage.
