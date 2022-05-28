Setting up MiningCore on windows 10:


Step 1) Install PostgreSQL 10 (or latest version) https://www.postgresql.org/download/
(When installing, the "StackBuilder" tool is not required)

----------------------------------------------------------------------------------------------------

Step 2) In the windows search bar; search for "psql" and login using the info provided next to the questions in the pSQL Shell (The password is the one used when installing PostgreSQL)

----------------------------------------------------------------------------------------------------

Step 3) Run the following commands: (Replace "myPassword" with your own password)

CREATE ROLE miningcore WITH LOGIN ENCRYPTED PASSWORD 'myPassword';
CREATE DATABASE miningcore OWNER miningcore;

----------------------------------------------------------------------------------------------------

Step 4) Search your pc for the location the following files and run the following commands: (Replace the paths under in commands, with the path to these files on your pc)

Files to locate:

createdb.sql
createdb_postgresql_11_appendix.sql


Commands:

\i c:/Users/Admin/Desktop/miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb.sql
\i c:/Users/Admin/Desktop/miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb_postgresql_11_appendix.sql

----------------------------------------------------------------------------------------------------

Step 5) Create the pool (for each coin you setup) using the following command: (Only needs to be done ONCE per pool per coin) (Replace "coinName" with the name of your choice)

CREATE TABLE shares_coinName PARTITION OF shares FOR VALUES IN ('coinName');

----------------------------------------------------------------------------------------------------

Step 6) In your miningcore directory folder, in the "build" directory; create a coinName.json file and configure it (Change the name to whatever coin you're setting up) (Make sure that under "logging", "logFile" and "apiLogFile" are not empty (The names could be "coinName_core.log" and "coinName_api.log") (Replace "coinName" with your coin name)

Example of what to put in your file: https://github.com/oliverw/miningcore/wiki/Configuration

----------------------------------------------------------------------------------------------------

Step 7) In your miningcore directory folder; create a bat file to run the following commands: (Replace "coinName" with the name used in the previous step)

cd build
./Miningcore -c coinName.json

----------------------------------------------------------------------------------------------------

Step 8) Miningcore setup done. Enjoy!   (Make sure your Node is synced completely for this to work)
