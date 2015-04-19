<h1>Hedgecoin (temp working name)</h1>


<h2>Purpose of the app</h2>
Allow people to effortlessly invest in crypto currencies and not just bitcoin.

<h2>Feature set</h2>
User:
Get Hedgecoin with BTC
Withdrawl BTC

MVP1
See flow > https://moqups.com/cavensio/cNwN7Cmb

MVP2
TBD

<h2>Application views</h2>
https://moqups.com/cavensio/cNwN7Cmb


<h2>Domain modeling</h2>
Table transactions

Ether address
BTC address
Amount received



<h2>Challenges</h2>
How to manage percentages? > Increasing $ value, etc.... DONE
On ethereum? YES, in steps
What should working environment look like? (not on Nitrous) > OR....just start on Nitrous and move away later?
	Local setup?
	Vagrant?
	Postgres > how to talk to postgres from local machine?
	What about other dependencies(?) > Develop on VM?
	Boilerplate code > Flask like in course examples?

<h2>To do</h2>
Set up dev on local machine	


<h2>Steps</h2>
<h3>Buy</h3>
1. Listen to tx on specific bitcoin address using Blockchain.info API
2. When new tx comes in, record buy_tx in DB
3. Open new sell order on Cryptsy, 50% X, 50% Y, using Cryptsy API
4. When order closes > calculate BTC/HGC amount
	Exception > if first tx
5. Send HGC to Eth address

<h3>Sell</h3>


tester