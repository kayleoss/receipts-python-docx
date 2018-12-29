from glob2 import glob
import textract


docs = glob("./receipts/*")
sum = 0

def init():
    for doc in docs:
        if doc != "./receipts\desktop.ini":
            try:
                text = textract.process(doc)
                half_text = text.split("Total Amount: ")[1]
                total = str(half_text.split('\n')[0])
                total_num = total.replace("$", "")
                global sum
                sum += int(total_num)
            except:
                print "error at " + doc
        else:
            pass
        

    print sum

init()
