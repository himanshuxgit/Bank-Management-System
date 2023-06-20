function createAccount() {
    var acno = parseInt(prompt("Enter The Account No.: "));
    var name = prompt("Enter The Name of The Account Holder: ");
    var type = prompt("Enter Type of The Account (C/S): ").toUpperCase();
    var deposit = parseInt(prompt("Enter The Initial Amount: "));

    var account = {
        acno: acno,
        name: name,
        type: type,
        deposit: deposit
    };

    fetch('/createAccount', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(account)
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
    });
}

function displayAllAccounts() {
    fetch('/displayAllAccounts')
    .then(response => response.text())
    .then(data => {
        document.getElementById("accountList").innerHTML = data;
    });
}

function searchAccount() {
    var acno = parseInt(prompt("Enter The Account No.: "));

    fetch('/searchAccount', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ acno: acno })
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
    });
}

function depositWithdraw(isDeposit) {
    var acno = parseInt(prompt("Enter The Account No.: "));
    var amount = parseInt(prompt("Enter The Amount: "));

    fetch('/depositWithdraw', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ acno: acno, amount: amount, isDeposit: isDeposit })
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
    });
}

function deleteAccount() {
    var acno = parseInt(prompt("Enter The Account No.: "));

    fetch('/deleteAccount', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ acno: acno })
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
    });
}
