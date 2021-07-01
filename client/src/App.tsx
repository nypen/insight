import React from 'react';
import { Route, Router, Switch } from 'react-router-dom'
import { Main } from './components/main'
import { createBrowserHistory } from "history"
import purple from '@material-ui/core/colors/purple';
import { createMuiTheme, ThemeProvider } from '@material-ui/core';
import { cyan } from '@material-ui/core/colors';

import './App.css';

const theme = createMuiTheme({
  palette: {
    primary: {
      main: purple[700]
    },
    secondary: {
      main: cyan[500]
    }
  }
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router history={createBrowserHistory()}>
        <Switch>
          <Route exact path='/' component={ Main } />       
        </Switch>
      </Router>
    </ThemeProvider>
  );
}

export default App;
