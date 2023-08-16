import "./navbar.css"
import {}

function Navbar(){
    return(
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <Link className="nav-link active" aria-current="page" to="/">
                  Home
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/catalog">
                  Catalog
                </a>
              
              </li>

              <li className="nav-item">
                <a className="nav-link" href="/about">
                  About
            </ul>
           
              <Link className="btn btn-outline-success" t0="/cart">
                cart
              </Link>
            </form>
          </div>
        </div>
      </nav>
      
    );
}//create a footer component and add it to the app.js, create 
//the css files and import it into the component

export default Navbar;

