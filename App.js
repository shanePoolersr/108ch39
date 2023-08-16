
import './App.css';
import Footer from './components/footer';
import Navbar from './components/navbar';
import Catalog from './pages/catalog';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import Home from "./pages/home";
import about
import { BrowserRouter, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    
    <div className="App">
      <Navbar/>

      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/' element={<Home />} />
        <Route path='/' element={<Home />} />
        <Route path='/' element={<Home />} />
        <Route path='/' element={<Home />} />





      </Routes>
      <Catalog/>        
      <Footer/>          
    </BrowserRouter>
    </div>
  );
}

export default App;

/**
 * Create the cart page
 * register a route on app.js for /cart
 * update the navbar, the button should be a link to /cart
 */