import React, { Component, Suspense} from 'react';
import { Route, Redirect, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import Screen from 'screens/Screen/Screen'

export class Router extends Component {

    componentDidMount(){
    }
  
    componentDidUpdate() {
    }
  
    render() {
      return (
        <>
          <Navbar />
          <Suspense fallback={Loading}>
            <Switch>
              <Route path="/bard" exact component={Screen} />
            </Switch>
          </Suspense>
        </>
      );
    }
  }
  
