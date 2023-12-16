import React from "react";
import backgroundImage from "./assets/loginimg.jpg"; 

const Home = () => {
    return (
        <div className="relative w-full h-screen overflow-hidden">
            
            <img
                src={backgroundImage}
                alt="Background"
                className=" fixed absolute bg-no-repeat bg-top inset-0 object-cover w-full h-full"
            />

            <div className="absolute inset-0 bg-black opacity-40" />

            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-white text-center">
                <h3 className="text-4xl font-bold mb-4">Welcome to DocTalk!</h3>
                <div className="text-lg mb-8">Empowering healthcare at your fingertips - Discover doctalk, the game-changing 
                web app that revolutionizes doctor-patient interaction, allowing consultations 
                and sharing of medical insights like never before.</div>
                <div className="border-b border-white w-full max-h-full mx-auto"></div>
            </div>
        </div>
    );
};

export default Home;

