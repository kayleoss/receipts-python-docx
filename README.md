# Receipt Totaler (docx) For Neshama Therapy

> Problem: Neshama Therapy has accumulated thousands of word document RMT and Acupuncture receipts and needs to total them to get income numbers and submit for income tax. 


> Problem 2: Neshama Therapy needs to categorize each receipt as either RMT or Acupuncture and also get the total income for RMT and Acupuncture separately in addition to the total income.



Solution: The script receipts.py works to get all the totals from each doc and add them up, printing the final number into the console. as well as separate numbers for RMT and ACU income. 


------------------


Limitations: 
- **Works with python 2.7**
- Each word doc must be exactly the same in terms of format and positioning. 
- Categories include 'massage therapy' or 'acupuncture treatment' only


Folder structure (where to put receipts): 
1) Create a folder called "receipts" in the root directory
2) Inside "receipts" folder create folders for where you will store your receipt documents to be totaled


------------------
 

### Example folder structure: 
`receipts/2018/receipt.docx`

![example of folder structure image](http://i63.tinypic.com/jzbgq9.png)

### Example command (to calculate all receipts inside a folder named '2018'):
`python receipts.py 2018`


------------------


To use this script, you must create a folder in the root directory called "receipts" and place all receipt documents inside it before running the script. 
