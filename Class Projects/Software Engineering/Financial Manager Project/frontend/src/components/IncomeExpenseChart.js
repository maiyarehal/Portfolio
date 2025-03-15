import React from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

const IncomeExpenseChart = ({ totalIncome, totalExpense }) => {
  const data = {
    labels: ["Income", "Expenses"],
    datasets: [
      {
        label: "Income vs. Expenses",
        data: [totalIncome, totalExpense],
        backgroundColor: ["#4CAF50", "#F44336"], 
        hoverOffset: 4,
      },
    ],
  };


  return (
    <section className="mb-5">
      <h2 className="text-center">Income vs. Expenses</h2>
      <div className="container d-flex justify-content-center align-items-center">
        <div className="card shadow-sm justify-content-center"style={{width: "300px"}}>
          <div className="card-body" style={{ position: "relative", height: "300px"}}>
              <Pie data={data} options={{ responsive: true, maintainAspectRatio: false, }} />
          </div>
        </div>
      </div>
    </section>
  );
};

export default IncomeExpenseChart;
