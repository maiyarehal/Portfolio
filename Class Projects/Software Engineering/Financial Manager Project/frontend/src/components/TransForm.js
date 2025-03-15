import React from 'react';
import Button from './Button';


const TransactionForm = ({ formData, handleInputChange, handleSubmit }) => {
  return (

  
    <div className="card mb-4">
      <div className="card-body">
        <h5 className='card-title'>Add New Transaction</h5>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Transaction Type</label>
            <select
              className="form-select"
              name="type"
              value={formData.type}
              onChange={handleInputChange}
            >
              <option value="">Select Type</option>
              <option value="Expense">Expense</option>
              <option value="Income">Income</option>
            </select>
          </div>
          <div className="mb-3">
            <label className="form-label">Date</label>
            <input
              type="date"
              className="form-control"
              name="date"
              value={formData.date}
              onChange={handleInputChange}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Amount</label>
            <input
              type="number"
              className="form-control"
              name="amount"
              value={formData.amount}
              onChange={handleInputChange}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Category</label>
            <input
              type="text"
              className="form-control"
              name="category"
              value={formData.category}
              onChange={handleInputChange}
            />
          </div>
          <Button className="btn btn-success" type="submit" text="Add Transaction"/>
        </form>
      </div>
    </div>
  );
};

export default TransactionForm;
