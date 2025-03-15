import React, { useState, useEffect } from "react";
import BudgetList from "../components/BudgetList";
import BudgetForm from "../components/BudgetForm";

const Budget = ({ username }) => {
  const [budgets, setBudgets] = useState([]);
  const [editingBudget, setEditingBudget] = useState(null);
  const [loading, setLoading] = useState(true);


  const getBudgets = () => {
    setLoading(true);
    fetch(`http://localhost:3000/api/budgets?username=${username}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          const budgets = data.success.data.budgets || [];
          console.log('Fetched Budgets:', budgets);
          setBudgets(budgets);
        } else {
          console.error('Error fetching Budgets:', data.message);
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error:', error);
        setLoading(false);
      });
  }
  const addBudget = (budget) => {
    fetch(`http://localhost:3000/api/budgets?username=${username}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(budget),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          getBudgets();
        } else {
          console.error("Error adding budget:", data.message);
        }
      })
      .catch((error) => console.error("Error:", error));
  };


  const updateBudget = (updatedBudget) => {
    fetch(`http://localhost:3000/api/budgets`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updatedBudget),
    })
      .then((response) => response.json())
      .then(() => getBudgets())
      .catch((error) => console.error("Error updating budget:", error));
    setEditingBudget(null);
  };


  const deleteBudget = (id) => {
    fetch(`http://localhost:3000/api/budgets?id=${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then(() => getBudgets())
      .catch((error) => console.error("Error deleting budget:", error));
  };

  useEffect(() => {
    getBudgets();
  }, [username]);


  if (loading) {
    return <div>Loading...</div>;
  }
  return (
    <div className="container my-5">
      <h1 className="text-center mb-4">Manage Budgets</h1>

      <BudgetForm
        addBudget={addBudget}
        updateBudget={updateBudget}
        editingBudget={editingBudget}
      />
      
      <BudgetList budgets={budgets} editBudget={setEditingBudget} deleteBudget = {deleteBudget}/>
    </div>
  );
};

export default Budget;
