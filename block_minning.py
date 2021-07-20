
import json
import datetime
import hashlib


def savedata(file):
    f = open('Hash_values.txt', 'w')
    json.dump(file, f, indent=4)
    f.close()

def trans_save(file):
    f = open('Blockchain.txt', 'w')
    json.dump(file, f, indent=4)
    f.close()

def save(file):
    f = open('data.txt', 'w')
    json.dump(file, f, indent=4)
    f.close()





#block mining program

try:
    file = open('data.txt', 'r')
    data = json.load(file)
    file.close()
    print('Transaction file exists!')

except:
    print("Error no transactions available!")
    exit()
    
try:
    sam = open('Hash_values.txt', 'r')
    block_chain = json.load(sam)
    sam.close()
    print("Blockchain file exist! loading data.........")

except:

    block_chain = []                                                     #creating an empty list called block_chain to capture the genesis blocks hash value
    time = datetime.datetime.today()
    previous_hash = "first block".encode('utf8')
    new = hashlib.new('sha256')
    new.update(previous_hash)
    new1 = new.hexdigest()                                               #sha256 value of previous hash
    genesis_block = '0' + 'first block' + str(time) + str(new1)          #creating genesis block
    block = str(genesis_block).encode('utf8')                            #encoding genesis block
    final_hash = hashlib.new('sha256')
    final_hash.update(block)
    message_digest = final_hash.hexdigest()                              #message digest
    block_chain.append(message_digest)                                   #appending hash values to block_chain variable created above
    savedata(block_chain)                                                #saving data to Hash_value.txt file
    print('Genesis block has been created!')

    trans_data = []                                                      #creating an empty list called trans_data to save user transactions + index + nonce + previous hash
    log = {}                                                             #creating an empty dictionary called log to save genesis blocks data (Data + Timestamp + previous hash + index)
    log['Data'] = 'First block'
    log['Timestamp'] = str(time)
    log['Index'] = '0'
    log['Previous hash (first block)'] = str(new1)
    trans_data.append(log)                                               #appending log dictionary to the trans_data list
    trans_save(trans_data)                                               #saving trans_data list to the blockchain.txt file



if len(data) >= 1:                                                                                                           #if length of data variable is higher than one or equal to one then the below code will execute
    if len(block_chain) == 1:
        counter = 0
        counter2 = 1
    else:
        counter = len(block_chain) - 1
        counter2 = len(block_chain)

    while True:
        print('New Transaction available')
        print('Do you want to start the blockchain process: (YES/N0)')
        dam = str(input(">")).lower()
        if dam == "yes":
             for index, keys in enumerate(data):
                first = str(keys['From']) + str(keys['To']) + str(keys['Amount']) + str(keys['Timestamp']) + str(counter2)     #data + Index number
                first1 = str(first) + block_chain[0 + counter]                                                                 #adding previous hash

                log_data = {}                                                                                                  #creating an empty dictionary to store user transactions + index number + previous hash and nonce
                log_data['From'] = str(keys['From'])
                log_data['To'] = str(keys['To'])
                log_data['Amount'] = str(keys['Amount'])
                log_data['Timestamp'] = str(keys['Timestamp'])
                log_data['Index'] = str(counter2)
                log_data['Previous hash'] = block_chain[0 + counter]

                try:
                    file = open('Blockchain.txt', 'r')
                    trans_data = json.load(file)
                    file.close()
                except:
                    trans_data = []

                counter = counter + 1
                counter2 = counter2 + 1
                nonce = 0                                                                                                      #nounce variable

                while True:
                    second = first1 + str(nonce)                                                                               #adding nonce to the
                    third = second.encode('utf8')
                    fourth = hashlib.new('sha256')
                    fourth.update(third)
                    message_digest = fourth.hexdigest()
                    count = message_digest.count('0')                           #checking how many zeroes contain in message_digest
                    if count == 14:                                             #if message_digest has 14 zeroes in it
                        block_chain.append(message_digest)
                        savedata(block_chain)
                        log_data['Nonce'] = nonce
                        trans_data.append(log_data)                             #appending data in log_data variable contents into trans_data list
                        trans_save(trans_data)                                  #saving trans_data list into Blockchain.txt file
                        break

                    elif nonce > 500000:
                        block_chain.append(message_digest)
                        savedata(block_chain)
                        log_data['Nonce'] = nonce
                        trans_data.append(log_data)                             #appending data in log_data variable contents into trans_data list
                        trans_save(trans_data)                                  #saving trans_data list into Blockchain.txt file
                        break
                    else:
                        nonce = nonce + 1




             del data[:]                                                                                       #deleting contents in the data file
             save(data)                                                                                        #saving changes to the data.txt file using save function
             print("Processing..........")
             print('Block chain has been successfully updated with new transactions!')
             exit()
             

        elif dam == "no":
            print('Blockchain has been successfully cancelled')
            exit()
        
            
        else:
            print("Invalid input! please try again")
            continue

else:                                                                                                          #if legnth of data variable is lower than one, then the below message will print out to the user and the program will end
    print('Blockchain is up-to-date. Please update new transactions to continue!')
    exit()















