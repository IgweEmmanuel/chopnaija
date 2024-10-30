import React from 'react'

const Header = () => {
  return (
    <header className="py-5" style={{ backgroundColor: '#51A262' }}>
      <div className="container px-4 px-lg-5 my-5">
        <div className="text-center text-white">
          <h1 className="display-4 fw-bold">
            Welcome to your Farm Marketplace
          </h1>
          <p className="lead fw-normal text-white-75 mb-4">
            Discover the freshest farm produce
          </p>
          <a
            href="#shop"
            className="btn btn-light btn-lg rounded-pill px-4 py-2"
          >
            Shop Now
          </a>
        </div>
      </div>
    </header>
  )
}

export default Header
