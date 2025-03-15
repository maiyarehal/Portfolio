import React from "react";

import Button from "./Button";

const BudgetItem = ({ budget, editBudget, deleteBudget }) => {
  const progress = ((parseFloat(budget.spent) || 0) / (parseFloat(budget.amount_limit) || 1)) * 100;

  return (
    <div className="col-md-6">
      <div className="card shadow-sm mb-4">
        <div className="card-body">
          <h5 className="card-title">{budget.category}</h5>
          <div className="progress mb-2">
            <div
              className="progress-bar bg-success text-dark"
              role="progressbar"
              style={{ width: `${progress}%` }}
              aria-valuenow={progress}
              aria-valuemin="0"
              aria-valuemax="100"
            >
              ${parseFloat(budget.spent || 0).toFixed(2)} of $
              {parseFloat(budget.amount_limit || 0).toFixed(2)}
            </div>
          </div>
          <p className="card-text">
            Remaining: $
            {(parseFloat(budget.amount_limit || 0) - parseFloat(budget.spent || 0)).toFixed(2)}
          </p>
          <p className="card-text">
            <strong>Start Date:</strong> {budget.start_date}
          </p>
          <p className="card-text">
            <strong>End Date:</strong> {budget.end_date}
          </p>

          <Button className="btn btn-warning me-2" onClick={() => editBudget(budget)} text="Edit"/>
          <Button className="btn btn-danger" onClick={() => deleteBudget(budget.id)} text="Remove"/>
        </div>
      </div>
    </div>
  );
};

export default BudgetItem;
