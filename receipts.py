from glob2 import glob
import textract


docs = glob("./receipts/*")
sum = 0
acu_sum = 0
rmt_sum = 0

def init():
    for doc in docs:
        if doc != "./receipts\desktop.ini":
            try:
                text = textract.process(doc)
                half_text = text.split("Total Amount: ")[1]
                service_type_half = text.split("Description Of Service: ")[1]
                service_type = str(service_type_half.split('\n')[0])
                total = str(half_text.split('\n')[0])
                total_num = total.replace("$", "")
                global sum
                sum += int(total_num)

                if (service_type.lower() == "acupuncture treatment") or (service_type.lower() == "acupuncrure treatment"):
                    global acu_sum
                    acu_sum += int(total_num)
                elif service_type.lower() == "massage therapy":
                    global rmt_sum
                    rmt_sum += int(total_num)
                else:
                    print "CAN NOT ACCEPT SERVICE: " + service_type

            except:
                print "error at " + doc
        else:
            pass
        

    print "TOTAL: " + str(sum)
    print "ACUPUNCTURE TOTAL: " + str(acu_sum)
    print "RMT TOTAL: " + str(rmt_sum)


init()
