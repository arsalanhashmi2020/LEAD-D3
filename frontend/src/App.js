import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NavigationBar from './components/Navbar';
import HomePage from './pages/HomePage';
import DatasetsPage from './pages/DatasetsPage';
import VisualizePage from './pages/VisualizePage';
import AboutUsPage from './pages/AboutUsPage';

function App() {
  return (
    <Router>
      <NavigationBar />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/datasets" component={DatasetsPage} />
        <Route path="/visualize" component={VisualizePage} />
        <Route path="/about" component={AboutUsPage} />
      </Switch>
    </Router>
  );
}

export default App;
