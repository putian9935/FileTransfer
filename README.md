# FileTransfer

A alternative approach to file transfer when SSH is banned for various reasons.  

## How to use? 

Assume you have two computers A & B and want to keep computer A updated with certain files from computer B. 

- Clone this repo on both computers. Update the ``file.txt`` with the full path to the files (one line per file) you want to update;
- Run ``fileTransferManager.py`` on computer B; 
- Run ``client.py`` on computer A; now computer A will keep updated versions of the files.

## Possible issues 

1. You might want to set this repo **private** once cloned. 

2. Current implementation only concerns one sender (*i.e.* one computer B); ``branch`` can be used to make it work with multiple senders.

3. Commit counts may explode over time; "squashing" commits is an option to avoid this. 
