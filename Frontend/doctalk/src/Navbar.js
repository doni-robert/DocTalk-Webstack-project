import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import SignUp from "./Signup";

const Navbar = ({ loggedIn, email, onLogout }) => {
  const [showSignup, setShowSignup] = useState(false);
  const navigate = useNavigate();

  const onSignupClick = () => {
    navigate('/signup');
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


