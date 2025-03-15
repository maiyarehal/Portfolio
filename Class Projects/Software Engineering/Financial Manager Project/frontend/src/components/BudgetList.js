import React from "react";
import BudgetItem from "./BudgetItem";

const BudgetList = ({ budgets, editBudget, deleteBudget }) => {
  return (
    <div className="row">
      {budgets.map((budget) => (
        <BudgetItem
          key={budget.id}
          budget={budget}
          editBudget={editBudget}
          deleteBudget={deleteBudget}
        />
      ))}
    </div>
  );
};

export default BudgetList;
