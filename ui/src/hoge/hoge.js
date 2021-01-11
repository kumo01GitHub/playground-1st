import React from "react";

export default class Hoge extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.state.name = "まだ商品名を取得していません";
    this.buttonClick = this.buttonClick.bind(this);
  }

  buttonClick(){
    fetch('http://localhost:5000/hoge', {
      mode: 'cors'
    }).then(response => {
      return response.json();
    }).then((json) => {
      this.setState(
        {name:JSON.parse(JSON.stringify(json)).value});
      console.log(JSON.parse(JSON.stringify(json)));
    }).catch((error) => {
      console.log('Error:', error);
    })
  }

  render() {
    return (
      <div>
        <input type="button" onClick={ this.buttonClick } value="this is test"/>
        <p>{this.state.name}</p>
      </div>
    );
  }
}
