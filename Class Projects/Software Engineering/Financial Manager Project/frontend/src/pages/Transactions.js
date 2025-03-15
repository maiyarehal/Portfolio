import React, { useState, useEffect } from 'react';
import TransactionTable from '../components/TransactionTable';

const Transactions = ({ username }) => {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);

  const getTransactions = () => {
    setLoading(true);

    fetch(`http://localhost:3000/api/transactions?username=${username}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          const transactions = data.success.data.transactions || [];
          console.log('Fetched Transactions:', transactions);
          setTransactions(transactions);
        } else {
          console.error('Error fetching transactions:', data.message);
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error:', error);
        setLoading(false);
      });
  };


  const handleButtonClick = (id) => {
    fetch(`http://localhost:3000/api/transactions?id=${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          getTransactions();
        }
        else {
          console.error("Error removing budget:", data.message);
        }
      })
  }

  useEffect(() => {
    getTransactions();
  }, [username]);


  

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container my-5">
      <header className="py-4 text-center mb-4">
        <h1>Transactions for {username}</h1>
        <p className="lead">Add, view, and manage your income and expenses here.</p>
      </header>

      <TransactionTable transactions={transactions} username={username} handleButtonClick={handleButtonClick}/>
    </div>
  );
};

export default Transactions;
