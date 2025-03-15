import React, { useState } from 'react';
import TransForm from './TransForm';
import TransTable from './TransTable';

const TransactionTable = ({ transactions: initialTransactions, username , handleButtonClick}) => {
  const [transactions, setTransactions] = useState(initialTransactions);
  const [formData, setFormData] = useState({
    type: '',
    date: '',
    amount: '',
    category: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.type || !formData.date || !formData.amount || !formData.category) return;

    const newTransaction = {
      id: transactions.length + 1, 
      type: formData.type,
      date: formData.date,
      amount: parseFloat(formData.amount),
      category: formData.category,
    };


    fetch(`http://localhost:3000/api/transactions?username=${username}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newTransaction),
    })
      .then((response) => response.json())
      .then((data) => {
        setTransactions([...transactions, newTransaction]);
        console.log('Transaction saved:', data);
      })
      .catch((error) => {
        console.error('Error saving transaction:', error);
      });
    
    setFormData({
      type: '',
      date: '',
      amount: '',
      category: '',
    });
  };

  

  const formatAmount = (type, amount) => {
    return type === "Expense" ? `- $${Math.abs(amount).toFixed(2)}` : `+ $${amount.toFixed(2)}`;
  };

  return (
    <div className="container my-5">

      <TransForm 
        formData={formData} 
        handleInputChange={handleInputChange} 
        handleSubmit={handleSubmit} 
      />

      <TransTable 
        transactions={transactions} 
        formatAmount={formatAmount}
        handleButtonClick={handleButtonClick} 
      />
    </div>
  );
};

export default TransactionTable;
