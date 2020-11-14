import sortArrayOfObjects from 'helper/data';
import React from 'react';
import Table from 'react-bootstrap/Table';

const CandidateTable = ({listOfCandidates}) => {
  return (
    <Table striped bordered>
      <thead>
        <tr>
          <th>№</th>
          <th>Title</th>
          <th>Skills</th>
        </tr>
      </thead>
      <tbody>
      {listOfCandidates.length ?
        sortArrayOfObjects(listOfCandidates, 'order_weight').map((candidate, index) => (
          <tr key={index}>
            <td>{index + 1}</td>
            <td>{candidate.title}</td>
            <td>{candidate.get_skills}</td>
          </tr>
        )) :
        (
          <tr>
            <td colSpan="3">Candidate's table is empty</td>
          </tr>
        )
      }
      </tbody>
    </Table>
  );
};

export default CandidateTable;
