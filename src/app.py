from flask import Flask,render_template,redirect,request
from web3 import Web3, HTTPProvider
from ca import *
import json
import time
from SendEmail import *

app=Flask(__name__)

def connect_with_blockchain(acc):
    web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
    if(acc==0):
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc
    compiled_contract_path='../build/contracts/rentcar.json'
    deployed_contract_address=carRentContractAddress

    with open(compiled_contract_path) as file:
        contract_json=json.load(file)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=deployed_contract_address,abi=contract_abi)
    return contract, web3

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/services')
def servicesPage():
    return render_template('services.html')

@app.route('/pricing')
def pricingPage():
    return render_template('pricing.html')

@app.route('/cars')
def carsPage():
    return render_template('car.html')

@app.route('/car-single')
def carSinglePage():
    return render_template('car-single.html')

@app.route('/contact')
def contactPage():
    return render_template('contact.html')

@app.route('/rentCarRequest',methods=['POST','GET'])
def rentCarRequest():
    walletaddr=request.form['walletaddr']
    cartype=request.form['cartype']
    pickup=request.form['pickup']
    dropoff=request.form['dropoff']
    pickupdate=request.form['pickupdate']
    dropoffdate=request.form['dropoffdate']
    pickuptime=request.form['pickuptime']
    phoneno=request.form['phoneno']
    emailid=request.form['emailid']
    print(pickup,dropoff,pickupdate,dropoffdate,pickuptime,phoneno,emailid,cartype,walletaddr)
    contract,web3=connect_with_blockchain(0)
    tx_hash=contract.functions.addRequest(walletaddr,pickup,dropoff,pickupdate,dropoffdate,pickuptime,cartype,phoneno,emailid).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    verifyIdentity(emailid)
    while True:
        try:
            a=sendmessage('Your cab booked, Driver will pick you accordingly',walletaddr,pickup,dropoff,pickupdate,dropoffdate,pickuptime,cartype,phoneno,emailid)
            if(a):
                break
            else:
                continue
        except:
            time.sleep(10)

    return render_template('index.html')

@app.route('/bookings')
def bookingsPage():
    data=[]
    contract,web3=connect_with_blockchain(0)
    _users,_pickups,_dropoffs,_pickupdates,_dropoffdates,_pickuptime,_cartypes,_phonenos,_emailids=contract.functions.viewRequests().call()
    for i in range(len(_users)):
        dummy=[]
        dummy.append(_users[i])
        dummy.append(_pickups[i])
        dummy.append(_dropoffs[1])
        dummy.append(_pickupdates[i])
        dummy.append(_dropoffdates[i])
        dummy.append(_pickuptime[i])
        dummy.append(_cartypes[i])
        dummy.append(_phonenos[i])
        dummy.append(_emailids[i])
        data.append(dummy)
    l=len(data)
    return render_template('booking.html',dashboard_data=data,len=l)

if __name__=="__main__":
    app.run(debug=True)