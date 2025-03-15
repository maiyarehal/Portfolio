import './App.css';
import React, { useEffect} from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation, useNavigate} from 'react-router-dom';
import Navbar from './components/Navbar';
import Transactions from './pages/Transactions'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import Budget from './pages/Budget';


const App = () => {
  return (
    <Router>
      <AppContent />
    </Router>
  );
};

const AppContent = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const user = localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : null;
  const username = user?.username || '';

  useEffect(() => {
    if (!user && location.pathname !== '/') {
      navigate('/');
    }
  }, [user, location, navigate]);

  return (
    <div className='App'>
      {(location.pathname !== '/') && <Navbar username={username}/>}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard username={username}/>} />
        <Route 
          path="/transactions" 
          element={user ? <Transactions username={username} /> : <Login />}
        />
        <Route path="/budget" element={<Budget username={username}/>} />
      </Routes>
    </div>
  );
};



export default App;
