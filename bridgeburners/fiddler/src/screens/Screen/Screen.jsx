import React from 'react';
import c from 'classnames'
import { compose } from 'redux'
import { connect } from 'react-redux';
import { withRouter } from 'react-router'


import './Screen.scss';

export class Screen extends React.Component { 
  constructor(props){
    super(props);
  }

  componentDidMount() {
    window.scrollTo(0,0);
  }


  render() {
    return (
      <div className={c('Screen', "HomePage")}>
        Screen
      </div>
    )
  }
}

const mapStateToProps = state => ({
  thing: "thing:1",
})

export default compose(
  withRouter,
  connect(mapStateToProps),
)(Screen)

