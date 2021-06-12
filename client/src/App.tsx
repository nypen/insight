import React from 'react';
import { Route, Router, Switch } from 'react-router-dom'
import { Main } from './components/main'
import { createBrowserHistory } from "history"

import './App.css';

function App() {
  return (
    <Router history={createBrowserHistory()}>
      <Switch>
        <Route exact path='/' component={ Main } />       
      </Switch>
    </Router>
  );
}

export default App;
