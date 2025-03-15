import React from 'react';
import Button from './Button';

const TransTable = ({ transactions, formatAmount, handleButtonClick}) => {

  return (
    <section className="mb-5">
      <h3>Transactions</h3>
      <div className="table-responsive">
        <table className="table table-bordered table-striped shadow-sm">
          <thead className="table-success bg-sucess">
            <tr>
              <th scope="col">Transaction ID</th>
              <th scope="col">Transaction Type</th>
              <th scope="col">Date</th>
              <th scope="col">Amount</th>
              <th scope="col">Category</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((transaction) => (
              <tr key={transaction.id}>
                <th scope="row">{transaction.id} <Button type='button' onClick={() => handleButtonClick(transaction.id)} className={"btn btn-danger"} text="Remove"/></th>
                <td>{transaction.type}</td>
                <td>{transaction.date}</td>
                <td>{formatAmount(transaction.type, transaction.amount)}</td>
                <td>{transaction.category}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};

export default TransTable;