import React, { useState, useEffect } from "react";
import Summary from "../components/Summary";
import IncomeExpenseChart from "../components/IncomeExpenseChart";

export default function Dashboard({ username }) {
  const [totalIncome, setTotalIncome] = useState(0);
  const [totalExpense, setTotalExpense] = useState(0);

  const fetchTrans = async (username, type) => {
    const response = await fetch(`/api/trans?username=${username}&type=${type}`);
    if (!response.ok) {
      console.error(`Error fetching ${type} transactions:`, response.statusText);
      return [];
    }

    const data = await response.json();
    return data.transactions; 
  };

  useEffect(() => {
    const getTransactions = async () => {
      const incomeData = await fetchTrans(username, "Income");

      let total = 0;
      incomeData.forEach((transaction) => {
        total += transaction.amount;
      });

      setTotalIncome(total);
      
      total = 0;
      const expenseData = await fetchTrans(username, "Expense");
      expenseData.forEach((transaction) => {
        total += transaction.amount;
      });

      setTotalExpense(total);

      total = 0;

    };

    getTransactions();
  }, [username]);

  return (
    <div>
      <div className="container my-5">
        <header className="py-4 text-center mb-4">
          <h1>Welcome Back {username}</h1>
        </header>
        <Summary totalIncome={totalIncome} totalExpense={totalExpense}/>
        <IncomeExpenseChart totalIncome={totalIncome} totalExpense={totalExpense}/>
      </div>
    </div>
  );
}
