from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

class Account:
    def __init__(self):
        self.acno = 0
        self.name = ""
        self.type = ""
        self.deposit = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createAccount', methods=['POST'])
def create_account():
    account = Account()
    account.acno = int(request.json['acno'])
    account.name = request.json['name']
    account.type = request.json['type']
    account.deposit = int(request.json['deposit'])

    with open('accounts.dat', 'ab') as file:
        pickle.dump(account, file)

    return "Account Created and written to file successfully."

@app.route('/displayAllAccounts')
def display_all_accounts():
    accounts = []
    with open('accounts.dat', 'rb') as file:
        try:
            while True:
                account = pickle.load(file)
                accounts.append(account)
        except EOFError:
            pass

    if not accounts:
        return "No accounts found."

    table = "<table>"
    table += "<tr><th>Account No.</th><th>Name</th><th>Type</th><th>Balance</th></tr>"
    for account in accounts:
        table += f"<tr><td>{account.acno}</td><td>{account.name}</td><td>{account.type}</td><td>{account.deposit}</td></tr>"
    table += "</table>"
    return table

@app.route('/searchAccount', methods=['POST'])
def search_account():
    acno = int(request.json['acno'])
    with open('accounts.dat', 'rb') as file:
        try:
            while True:
                account = pickle.load(file)
                if account.acno == acno:
                    return f"Account No.: {account.acno}\nName: {account.name}\nType: {account.type}\nBalance: {account.deposit}"
        except EOFError:
            pass

    return "Account number does not exist."

@app.route('/depositWithdraw', methods=['POST'])
def deposit_withdraw():
    acno = int(request.json['acno'])
    amount = int(request.json['amount'])
    is_deposit = request.json['isDeposit']

    with open('accounts.dat', 'rb+') as file:
        try:
            while True:
                pos = file.tell()
                account = pickle.load(file)
                if account.acno == acno:
                    if is_deposit:
                        account.deposit += amount
                    else:
                        if account.deposit >= amount:
                            account.deposit -= amount
                        else:
                            return "Insufficient balance."
                    file.seek(pos)
                    pickle.dump(account, file)
                    return "Transaction Successful."
        except EOFError:
            pass

    return "Account not found."

@app.route('/deleteAccount', methods=['POST'])
def delete_account():
    acno = int(request.json['acno'])
    accountsNew = []
    count = 0

    with open('accounts.dat', 'rb') as file:
        try:
            while True:
                account = pickle.load(file)
                count+=1
                if account.acno != acno:
                    accountsNew.append(account)
        except EOFError:
            pass

    if len(accountsNew) < count:
        with open('accounts.dat', 'wb') as file:
            for account in accountsNew:
                pickle.dump(account, file)
        return "Account Deleted Successfully."
    else:
        return "Account not found."

if __name__ == '__main__':
    app.run()

