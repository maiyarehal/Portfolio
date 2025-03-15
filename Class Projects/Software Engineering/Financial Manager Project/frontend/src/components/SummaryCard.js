
import React from "react";

const SummaryCard = ({ title, value }) => (
  <div className="col-md-4">
    <div className="card shadow-sm mb-4">
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">${value.toFixed(2)}</p>
      </div>
    </div>
  </div>
);

export default SummaryCard;
