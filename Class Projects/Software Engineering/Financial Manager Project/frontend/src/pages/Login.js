import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [username, setusername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const onButtonClick = () => {
        checkAccountExists((accountExists) => {
            if (accountExists) logIn();
            else if (
                window.confirm(
                    `An account does not exist with this username: ${username}. Do you want to create a new account?`
                )
            ) {
                logIn();
            }
        });
    };

    const checkAccountExists = (callback) => {
        fetch("http://localhost:3000/api/check-account", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username }),
        })
            .then((r) => r.json())
            .then((r) => {
                callback(r?.userExists);
            });
    };

    const logIn = () => {
        fetch("http://localhost:3000/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        })
            .then((r) => r.json())
            .then((r) => {
                if (r.user_login) {
                    localStorage.setItem("user", JSON.stringify({ username }));
                    setusername(username);
                    navigate("/dashboard");
                } else {
                    window.alert("Wrong username or password");
                }
            });
    };

    const signUp = () => {
        fetch("http://localhost:3000/api/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        })
            .then((r) => r.json())
            .then((r) => {
                if (r.user_signup) {
                    localStorage.setItem("user", JSON.stringify({ username }));
                    setusername(username);
                    navigate("/dashboard");
                } else {
                    window.alert("Error Occurred. Please try again.");
                }
            });
    };

    return (
        <div className="d-flex justify-content-center align-items-center vh-100">
            <div className="card shadow-lg" style={{ width: "350px" }}>
                <div className="card-body">
                    <h3 className="card-title text-center mb-4">
                        Login to Ca$hKeeper
                    </h3>
                    <form>
                        <div className="mb-3">
                            <label htmlFor="username" className="form-label">
                                Username
                            </label>
                            <input
                                type="text"
                                className="form-control"
                                id="username"
                                placeholder="Enter your username"
                                value={username}
                                onChange={(e) => setusername(e.target.value)}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="password" className="form-label">
                                Password
                            </label>
                            <input
                                type="password"
                                className="form-control"
                                id="password"
                                placeholder="Enter your password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>
                        <div className="d-flex justify-content-between">
                            <button
                                type="button"
                                className="btn btn-success"
                                onClick={onButtonClick}
                            >
                                Log In
                            </button>
                            <button
                                type="button"
                                className="btn btn-success"
                                onClick={signUp}
                            >
                                Sign Up
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Login;
