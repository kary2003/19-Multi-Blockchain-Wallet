# Multi-Blockchain-Wallet

![image](https://user-images.githubusercontent.com/70820754/111232761-01bc0a80-85a9-11eb-8f67-f60abb5d86d4.png)

Building a portfolio management system that supports not only tradinal assets such as gold, silver, stocks etc but new virtual asets such as crypto by utilizing the commmand line tool hd-wallet-derive. In order to use this tool/script it will need to be integrated into the backend using python. 

HD-Wallet Derive is a tool that supports:
  * BIP32
  * BIP39
  * BIP44
  * Also supports non-standard derivation paths for most wallets currently available.

By integrating the wallet into our backend development the company will be able to use this 'universal' wallet to manage billions of addresses across 300+ coins.

## Dependencies 

Dependencies

PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will not need to know any PHP.

You will need to clone the hd-wallet-derive tool.

bit Python Bitcoin library.

web3.py Python Ethereum library.

## Instructions

Instructions

Project setup


Create a project directory called wallet and cd into it.


Clone the hd-wallet-derive tool into this folder and install it using the instructions on its README.md.


Create a symlink called derive for the hd-wallet-derive/hd-wallet-derive.php script into the top level project
directory like so: ln -s hd-wallet-derive/hd-wallet-derive.php derive
This will clean up the command needed to run the script in our code, as we can call ./derive
instead of ./hd-wallet-derive/hd-wallet-derive.php.

Test that you can run the ./derive script properly, use one of the examples on the repo's README.md

Create a file called wallet.py -- this will be your universal wallet script.
