import React, { Component } from 'react'

const axios = require('axios').default;

class Frontend extends Component {
  constructor(props) {
    super(props);
    this.state = 
    {
      news:"",
      result : "",
      result2 : "",
      sentiment: "",
    }
  }

  fakeNews = () => {
    const mythis = this
    axios.post('http://127.0.0.1:5000/predict', {
      message: this.state.news
    })
    .then(function (response) {
      console.log(response.data);
      mythis.setState({result: response.data})
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  sentiment = () => {
    const mythis2 = this
    // alert(this.state.sentiment)
    axios.post('http://127.0.0.1:5000/sentiment', {
      sntmnt: this.state.sentiment
    })
    .then(function (response) {
      console.log(response.data);
      mythis2.setState({result2: response.data})
    })
    .catch(function (error) {
      console.log(error);
    });
  }



  render() {
    return (
      <div className="App">
          <div className="container card text-center"> 
            <div>
              <div className="card-header">Fake news Detector</div>
              <div className="card-body">
                <textarea defaultValue={""} className="form-control" placeholder="Enter Your news here !" value={this.state.news} onChange={e => this.setState({ news: e.target.value })}/>
                <button type="button" className="btn btn-primary my-2" onClick={() => this.fakeNews()}>Fake News!</button>
                <div classNam e="card-footer text-muted">
                   <input type="text" id="result" className="text-muted ml-2" value={this.state.result} disabled />
                </div>
              </div>
            </div>
          <hr></hr>
          <div>
              <div className="card-header">Sentiment Analysis</div>
              <div className="card-body">
                <textarea defaultValue={""} className="form-control" placeholder="Enter Your Feed here !" value={this.state.sentiment} onChange={e => this.setState({ sentiment: e.target.value })}/>
                <button type="button" className="btn btn-primary my-2" onClick={() => this.sentiment()}>Analyse des Sentimets!</button>
                <div classNam e="card-footer text-muted">
                   <input type="text" id="result" className="text-muted ml-2" value={this.state.result2} disabled />
                </div>
              </div>
            </div>
            {/* <div>
              <textarea defaultValue={""} value={this.state.sentiment} onChange={e => this.setState({ sentiment: e.target.value })}/>
              <button type="button" onClick={() => this.sentiment()}>Analyse des Sentimets!</button>
              <input type="text" value={this.state.result2}  />
            </div> */}
          </div>
      </div>
    );  
  }
}

export default Frontend;
