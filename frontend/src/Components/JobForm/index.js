import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

class JobForm extends Component {
  state = {
    title: '',
    skill: null
  }

  onChangeHandle = (event) => {
    const currentJob = this.props.jobList.filter(job => job.id === parseInt(event.target.value))
    this.setState({ title: currentJob[0].title, skill: currentJob[0].skill})
  }

  onClickMatchHandle = event => {
    event.preventDefault()
    this.props.onClickMatch(this.state.title, this.state.skill)
  }
  render() {
    const { jobList } = this.props;
    if (jobList && !jobList.filter(job => job.title === 'Choose a Job...').length)
      jobList.unshift({ id: jobList.length + 1, skill: null, skill_name: null, title: 'Choose a Job...' });
    return (
      <Form inline onSubmit={this.onClickMatchHandle}>
        <Form.Label className="mr-sm-2" htmlFor="inlineFormCustomSelect" srOnly>
          Preference
        </Form.Label>
        <Form.Control as="select" className="mx-sm-3" id="inlineFormCustomSelect" custom onChange={this.onChangeHandle}>
          {jobList.length &&
            jobList.map((jobItem, index) => (
              <option key={index} value={jobItem.id}>
                {jobItem.title}
                {jobItem.skill ? ` (${jobItem.skill_name})` : null}
              </option>
            ))}
        </Form.Control>
        <Button type="submit">Match</Button>
      </Form>
    );
  }
}

export default JobForm;
