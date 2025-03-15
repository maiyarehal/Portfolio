import React, { useState, useEffect } from "react";
import Button from "./Button";

const BudgetForm = ({ addBudget, updateBudget, editingBudget }) => {
  const [category, setCategory] = useState("");
  const [amountLimit, setAmountLimit] = useState(0);
  const [spent, setSpent] = useState(0);
  const [startDate, setStartDate] = useState(""); 
  const [endDate, setEndDate] = useState("");

  useEffect(() => {
    if (editingBudget) {
      setCategory(editingBudget.category);
      setAmountLimit(editingBudget.amount_limit);
      setSpent(editingBudget.spent);
      setStartDate(editingBudget.start_date); 
      setEndDate(editingBudget.end_date);
    }
  }, [editingBudget]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const budget = { 
      category: category, 
      amount_limit: parseFloat(amountLimit), 
      spent: parseFloat(spent), 
      start_date: startDate,
      end_date: endDate, 
    };
  
    if (editingBudget) {
      budget.id = editingBudget.id;
      updateBudget(budget);
    } else {
      addBudget(budget);
    }
  
    
    setCategory("");
    setAmountLimit(0);
    setSpent(0);
    setStartDate(""); 
    setEndDate(""); 
  };

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h5 className="card-title">{editingBudget ? "Edit Budget" : "Add Budget"}</h5>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Category</label>
            <input
              type="text"
              className="form-control"
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Amount Limit</label>
            <input
              type="number"
              className="form-control"
              value={amountLimit}
              onChange={(e) => setAmountLimit(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Amount Spent</label>
            <input
              type="number"
              className="form-control"
              value={spent}
              onChange={(e) => setSpent(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Start Date</label>
            <input
              type="date"
              className="form-control"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>End Date</label>
            <input
              type="date"
              className="form-control"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              required
            />
          </div>

          <Button type="submit" className="btn btn-success" text={editingBudget ? "Save Changes" : "Add Budget"}/>
        </form>
      </div>
    </div>
  );
};

export default BudgetForm;
