# Import libraries
from flask import Flask, request, render_template,url_for, redirect
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation: List all Tarnsactions
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation: Display add transaction form
@app.route("/add", methods=['GET', 'POST'])
def add_transaction():
    #Check if the request method is POST
    if request.method == 'POST':
        #create a new transaction obect using form data
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        #Append the new transaction to the transcations list
        transactions.append(transaction)

        #Redirect the new transaction to the transactions
        return redirect(url_for('get_transactions'))
    #If the request method is GET, render the form template to display the add transaction form

    return render_template('form.html')

# Update operation: Display edit transaction form
# Route to handle the editing of an existing transaction
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    #Check if the request method is POST- form submission
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        
        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for('get_transactions'))
    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route('/delete/<int:transaction_id>', methods = ['GET', 'POST'])
def delete_transaction(transaction_id):
    #Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    #redirect to transaction list
    return redirect(url_for("get_transactions"))

#run the flask app
if __name__ == "__main__":
    app.run(debug=True)