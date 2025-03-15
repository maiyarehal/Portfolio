# Ca$hKeeper

Ca$hKeeper is a personal finance management application designed to simplify the process of tracking income, expenses, and budgets. It helps users organize their finances, set financial goals, and make informed decisions.

---

## Features

- **User Authentication**: Secure login for personalized financial data.
- **Income Tracking**: Monitor and categorize earnings over time.
- **Expense Management**: Log and analyze spending habits.
- **Budget Creation**: Set and track financial goals with spending limits.
- **Dashboard**: Visualize trends and summaries for better decision-making.

---

## Technology Stack

### Frontend
- **Framework**: React.js
- **Routing**: React Router
- **Styling**: HTML, JavaScript, CSS

### Backend
- **Language**: Python
- **Database**: SQLite, FLask
- **Core Scripts**: `main.py`, `util.py`, `database.py`

### Tools
- **Version Control**: GitLab
- **Linters**: Prettier, ESLint (Frontend), Black (Backend)
- **Testing**:
  - **Frontend**: React Testing Library
  - **Backend**: Python `unittest`

---

## Installation

### Prerequisites
- **Node.js** (for frontend development)
- **Python 3** (for backend development)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://gitlab.com/cs-department-ecu/csci-3030-softeware-engineering-i-fall-2024/financial-manager/financial-manager/-/tree/main
    ```
2. **Set Up Frontend**:
    ```
    cd frontend
    npm install
    npm start
    ```
3. **Set Up Backend**:
    ```
    cd backend
    pip install - r requirements.txt
    python database.py
    python main.py
    ```
---

## Usage

1. Launch the frontend application using `npm start`.
2. Run the backend server with `python main.py`.
3. Access the webpage through the browser.
4. Use the webpage to:
    - Log income and expenses.
    - Create, update, or delete budgets.
    - View summaries and manage finances.

---

## Usage

This project is liceensed under the **MIT License**.

---

## Authors

- Nick Jones
- Maiya Rehal
- Vlad Rodgers
- Bailey Hatoum
- Noah Brown

---

## Acknowledgments

Special thanks to the team for their dedication and effort in making Ca$hKeeper a success!