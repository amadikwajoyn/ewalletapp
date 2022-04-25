import React from "react";
import phoneImg from "../../images/phone.svg";
import { FaChevronRight } from "react-icons/fa";
import { useGlobalContext } from "../../context";
import { Link } from "react-router-dom";
import "./Hero.css";


const Hero = () => {
  const { closeSubmenu } = useGlobalContext();
  return (
    
    <section className="hero" onMouseOver={closeSubmenu}>
      <div className="hero-center">
        <article className="hero-info">
          <h1>
            Easy Payment Gateway <br />
            to Use
          </h1>
          <p className="hero-text">
            Good number of organizations all over the world uses myewalletapp 
            APIs to accept payments, send payouts, and
            manage their businesses online.
          </p>
          <span className="group">
            <Link to ='/signup'>
              <button className="btn startnow">

                Start now{""}
                <span className="right-arrow">
                  <FaChevronRight />
                </span>
              </button> 
            </Link>
            &nbsp; &nbsp;
            <button className="btn">
              Contact Sales{" "}
              <span className="right-arrow">
                <FaChevronRight />
              </span>
            </button>
          </span>
        </article>
        <article className="hero-images">
          <img src={phoneImg} alt="phoneImage" className="phone-img" />
        </article>
      </div>
    </section>
    
  );
};

export default Hero;