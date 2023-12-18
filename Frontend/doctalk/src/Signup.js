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

    // Check if all fields are filled
    if (!username || !email || !password || !confirmPassword) {
      setErrorMessages({ message: "Please fill in all fields." });
    } else if (password !== confirmPassword) {
      setErrorMessages({ message: "Passwords do not match." });
    } else {
      // Proceed with signup
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
    <form onSubmit={handleSubmit}>
      <div className="input-container">
        <label>Username</label>
        <input
          type="text"
          name="username"
          value={formData.username}
          onChange={handleInputChange}
          required
        />
      </div>
      <div className="input-container">
        <label>Email</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleInputChange}
          required
        />
      </div>
      <div className="input-container">
        <label>Password</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleInputChange}
          required
        />
      </div>
      <div className="input-container">
        <label>Confirm Password</label>
        <input
          type="password"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleInputChange}
          required
        />
      </div>
      <div className="button-container">
        <input type="submit" value="Sign Up" />
      </div>
      {renderErrorMessage()}
    </form>
  );

  return (
    <div className="signup-form">
      <div className="title">SignUp</div>
      {isSubmitted ? (
        <div>User is successfully signed up!</div>
      ) : (
        renderForm
      )}
    </div>
  );
}

export default SignUp;
