import _ from 'lodash';
import React, { Component } from 'react';
import queryString from 'query-string';
import Screen from 'components/Screen/Screen';

import { compose } from 'redux';
import { connect } from 'react-redux';

import './HomeScreen.scss';

const messages = {
  title:'Dakobed Bard Website'
}


export class HomeScreen extends Component {
  constructor(props) {
    super(props);
  }

  render() {

    // const appHomePage = metadata.pages.find(page => page.home);
    return (
      <Screen
        title= {messages.title} 
      >
        <div className = "HomeScreen">

        </div>
      </Screen>
    );
  }
}
