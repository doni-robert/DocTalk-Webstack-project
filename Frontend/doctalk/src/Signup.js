import React, { useState } from "react";

function SignUp() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [errorMessages, setErrorMessages] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();

    const { username, email, password, confirmPassword } = formData;

    if (!username || !email || !password || !confirmPassword) {
      setErrorMessages({ message: "Please fill in all fields." });
    } else if (password !== confirmPassword) {
      setErrorMessages({ message: "Passwords do not match." });
    } else {
      setIsSubmitted(true);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const renderErrorMessage = () => {
    return <div className="error">{errorMessages.message}</div>;
  };

  const renderForm = (
    <form onSubmit={handleSubmit} className="p-6 bg-white rounded shadow-md w-80">
      <h2 className="text-lg font-semibold mb-4">Sign Up</h2>
      <div className="input-container">
        <input
          type="text"
          placeholder="Username"
          name="username"
          value={formData.username}
          onChange={handleInputChange}
          className="h-10 border border-gray-300 px-2"
        />
      </div>
      <div className="input-container">
        <input
          type="email"
          placeholder="Email"
          name="email"
          value={formData.email}
          onChange={handleInputChange}
          className="h-10 border border-gray-300 px-2"
        />
      </div>
      <div className="input-container">
        <input
          type="password"
          placeholder="Password"
          name="password"
          value={formData.password}
          onChange={handleInputChange}
          className="h-10 border border-gray-300 px-2"
        />
      </div>
      <div className="input-container">
        <input
          type="password"
          placeholder="Confirm Password"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleInputChange}
          className="h-10 border border-gray-300 px-2"
        />
      </div>
      <button
        type="submit"
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
      >
        Sign Up
      </button>
      {renderErrorMessage()}
    </form>
  );

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      {isSubmitted ? (
        <div>User is successfully signed up!</div>
      ) : (
        renderForm
      )}
    </div>
  );
}

export default SignUp;

