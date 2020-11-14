import CandidateTable from 'Components/CandidateTable';
import JobForm from 'Components/JobForm';
import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import API from 'services/api';

class App extends Component {
  state = {
    listOfCandidates: [],
    listOfJobs: [],
    candidatesViewIsReady: false,
    jobsViewIsReady: false,
  }

  componentDidMount() {
    API.get('job/')
      .then(response => {
        this.setState({ listOfJobs: response.data })
      })
  };

  onClickMatch(title, skill) {
    if(!skill) {
      this.setState({ listOfCandidates: []})
      return
    }
    API.get(`candidate/search/?title=${title}&skill=${skill}`)
      .then(response => {
        this.setState({ listOfCandidates: response.data})
        }
      )
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <JobForm jobList={this.state.listOfJobs} onClickMatch={this.onClickMatch.bind(this)} />
        </header>

        <Container className='container-table'>
          <CandidateTable listOfCandidates={this.state.listOfCandidates} />
        </Container>
      </div>
    );
  }
}

export default App;
