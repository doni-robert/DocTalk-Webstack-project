import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const Navbar = ({ loggedIn, email, onLogout }) => {
    const [showSignup, setShowSignup] = useState(false);
    const navigate = useNavigate();
    const [signupData, setSignupData] = useState({
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
    });

    const onSignupClick = () => {
        setShowSignup(true);
        
    };

    const closeSignup = () => {
        setShowSignup(false);
        navigate(-1);
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setSignupData({
            ...signupData,
            [name]: value,
        });
    };

    const handleSignupSubmit = (e) => {
        e.preventDefault();
        // Handle signup form submission logic here
        console.log("Signup form submitted with data:", signupData);
        // After signup logic, you might want to clear the form or handle success
        setShowSignup(false);
        setSignupData({
            username: "",
            email: "",
            password: "",
            confirmPassword: "",
        });
    };

    return (
        <nav className="bg-gray-800 p-4 flex justify-between items-center relative">
            <div>
                <Link to="/" className="text-white text-lg font-semibold">
                    DocTalk
                </Link>
            </div>
            <div className="flex items-center">
                {!loggedIn ? (
                    <>
                        <Link to="/login" className="text-white mr-4">
                            Login
                        </Link>
                        <button onClick={onSignupClick} className="text-white">
                            Sign Up
                        </button>
                    </>
                ) : (
                    <div className="text-white mr-4">
                        Logged in as {email}
                        <button onClick={onLogout} className="ml-2">
                            Logout
                        </button>
                    </div>
                )}
            </div>
            {showSignup && (
                <div className=" absolute flex item-center top-16 right-4 bg-white p-6 rounded shadow-md w-80">
                    <h2 className="text-lg font-semibold mb-4">Sign Up</h2>
                    <form onSubmit={handleSignupSubmit}>
                        <div className="mb-4">
                            <input
                                type="text"
                                placeholder="Username"
                                name="username"
                                value={signupData.username}
                                onChange={handleInputChange}
                                className="inputField"
                            />
                        </div>
                        <div className="mb-4">
                            <input
                                type="email"
                                placeholder="Email"
                                name="email"
                                value={signupData.email}
                                onChange={handleInputChange}
                                className="inputField"
                            />
                        </div>
                        <div className="mb-4">
                            <input
                                type="password"
                                placeholder="Password"
                                name="password"
                                value={signupData.password}
                                onChange={handleInputChange}
                                className="inputField"
                            />
                        </div>
                        <div className="mb-4">
                            <input
                                type="password"
                                placeholder="Confirm Password"
                                name="confirmPassword"
                                value={signupData.confirmPassword}
                                onChange={handleInputChange}
                                className="inputField"
                            />
                        </div>
                        <button
                            type="submit"
                            className="inputButton bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                        >
                            Sign Up
                        </button>
                    </form>
                    <button onClick={closeSignup} className="text-sm text-blue-500 underline mt-4">
                        Close
                    </button>
                </div>
            )}
        </nav>
    );
};

export default Navbar;

//navbar code
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import SignUp from "./Signup"; // Assuming SignUp.js is in the same directory

const Navbar = ({ loggedIn, email, onLogout }) => {
  const [showSignup, setShowSignup] = useState(false);
  const navigate = useNavigate();

  const onSignupClick = () => {
    setShowSignup(true);
  };

  const closeSignup = () => {
    setShowSignup(false);
    navigate(-1);
  };

  return (
    <nav className="bg-gray-800 p-4 flex justify-between items-center relative">
      <div>
        <Link to="/" className="text-white text-lg font-semibold">
          DocTalk
        </Link>
      </div>
      <div className="flex items-center">
        {!loggedIn ? (
          <>
            <Link to="/login" className="text-white mr-4">
              Login
            </Link>
            <button onClick={onSignupClick} className="text-white">
              Sign Up
            </button>
          </>
        ) : (
          <div className="text-white mr-4">
            Logged in as {email}
            <button onClick={onLogout} className="ml-2">
              Logout
            </button>
          </div>
        )}
      </div>
      {showSignup && (
        <div className="absolute flex item-center top-16 right-4 bg-white p-6 rounded shadow-md w-80">
          <SignUp /> {/* Replacing the previous signup form with SignUp component */}
          <button onClick={closeSignup} className="text-sm text-blue-500 underline mt-4">
            Close
          </button>
        </div>
      )}
    </nav>
  );
};

export default Navbar;



