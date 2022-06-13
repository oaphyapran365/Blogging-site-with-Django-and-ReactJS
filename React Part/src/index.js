import React from 'react';
import './index.css';
import App from './App';
import Login from './components/Login';
import reportWebVitals from './reportWebVitals';
import { render } from "react-dom";
import { CookiesProvider } from 'react-cookie';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


const rootElement = document.getElementById("root");
render(
  <CookiesProvider>
  <BrowserRouter>
    <Routes>
      
      <Route path="/" element={<Login />} />
      <Route path="/articles" element={<App />} />

    </Routes>
  </BrowserRouter>
  </CookiesProvider>,
  rootElement
);

reportWebVitals();   
