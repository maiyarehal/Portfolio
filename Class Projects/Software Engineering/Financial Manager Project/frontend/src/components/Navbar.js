import React from 'react'
import Logo from "../assets/logo.png"
import { Link } from 'react-router-dom';
import "../styles/Navbar.css";
import { useNavigate } from 'react-router-dom';
import Button from './Button';


const NavbarItem = ({ linkto, text}) => {
    return (
        <li className="nav-item">
          <Link className="nav-link" to={linkto}>{text}</Link>
        </li>
    );
};



function Navbar({username}) {

    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem("user");
        navigate("/"); 
    };



    const user = JSON.parse(localStorage.getItem("user"))

    return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container d-flex justify-content-start leftside">
            <img className='navbar-brand' src={Logo} width="75" height="75" alt="Not Found"></img>

            <ul class="navbar-nav">
                <NavbarItem linkto={"/dashboard"} text ="Dashboard"></NavbarItem>
                <NavbarItem linkto={"/transactions"} text ="Transactions"></NavbarItem>
                <NavbarItem linkto={"/budget"} text ="Budgets"></NavbarItem>
            </ul>
        </div>

        <div className="rightside d-flex">
        <Button text = {"Logout of " + username} className="btn btn-success navbarBtn" onClick={handleLogout} />
        </div>
    </nav>
    )
}
export default Navbar
