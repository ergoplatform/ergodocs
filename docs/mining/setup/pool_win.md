# MiningCore Setup Tutorial on Windows 10

This guide walks you through setting up MiningCore on a Windows 10 machine step-by-step.

---

## 📦 Step 1: Install PostgreSQL

- Download and install PostgreSQL 10 or the latest version:  
  👉 [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

> ⚠️ During installation, **you do not need to install StackBuilder**.

---

## 🐘 Step 2: Launch pSQL Shell

- Open the Windows search bar and type **`psql`**.
- Launch the **pSQL Shell**.
- Login using the credentials you set during PostgreSQL installation.
  - Username: `postgres` (default)
  - Password: (the one you set during install)

---

## 🔐 Step 3: Create Database Role and Schema

In the pSQL Shell, run the following commands (replace `myPassword` with your actual password):

```sql
CREATE ROLE miningcore WITH LOGIN ENCRYPTED PASSWORD 'myPassword';
CREATE DATABASE miningcore OWNER miningcore;
```

---

## 📂 Step 4: Run Database Setup Scripts

Locate the following files on your PC:

- `createdb.sql`
- `createdb_postgresql_11_appendix.sql`

Then, in the pSQL Shell, run these commands (replace with actual paths):

```sql
\i c:/Users/YourUser/Desktop/miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb.sql
\i c:/Users/YourUser/Desktop/miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb_postgresql_11_appendix.sql
```

---

## 🧱 Step 5: Create Pool Table

For **each coin you setup**, create a partition of the shares table:

```sql
CREATE TABLE shares_coinName PARTITION OF shares FOR VALUES IN ('coinName');
```

> 🔁 Replace **`coinName`** with your desired coin identifier (e.g., `btc`, `eth`).

---

## ⚙️ Step 6: Configure the Pool

1. Go to your MiningCore `build` directory.
2. Create a `coinName.json` config file for your coin.
3. Inside the config file:
   - Ensure `"logFile"` and `"apiLogFile"` under `"logging"` are filled in (e.g., `coinName_core.log`, `coinName_api.log`).

📝 Example config:  
[MiningCore Configuration Example](https://github.com/oliverw/miningcore/wiki/Configuration)

---

## 🛠️ Step 7: Create a Startup Batch File

In your MiningCore root directory, create a `.bat` file with the following content (adjust for your coin name):

```bat
cd build
./Miningcore -c coinName.json
```

---

## ✅ Step 8: All Done!

MiningCore is now set up and ready to go!

> ⚠️ Ensure your coin's **node is fully synced** before launching the pool.

Happy mining! ⛏️
