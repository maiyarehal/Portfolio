
import React from "react";
import SummaryCard from "./SummaryCard";

const Summary = ({ totalIncome, totalExpense }) => {
  return (
    <section className="mb-5">
      <h2 className="text-center">Overview</h2>
      <div className="row text-center">
        <SummaryCard title="Total Income" value={totalIncome} />
        <SummaryCard title="Total Expenses" value={totalExpense} />
        <SummaryCard title="Savings" value={totalIncome - totalExpense} />
      </div>
    </section>
  );
};

export default Summary;
