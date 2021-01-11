import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Link } from "react-router-dom";

import Header from "./header";
import Main from "./main";
import Footer from "./footer";

import "./common.css";

import Hoge from "../hoge/hoge";
import Bar from "../bar/bar";
import Foo from "../foo/foo";

class Common extends React.Component {
  render() {
    return (
      <div id="components">
        <div id="header"></div>
        <div id="main"></div>
        <div id="footer"></div>
      </div>
    );
  }
}

const common = document.getElementById('common');
ReactDOM.render(<Common/>, common);

const header = document.getElementById('header');
ReactDOM.render(<Header/>, header);
const main = document.getElementById('main');
ReactDOM.render(
  <Router>
    <ul>
      <li><Link to="/foo">foo</Link></li>
      <li><Link to="/bar">bar</Link></li>
      <li><Link to="/">hoge</Link></li>
    </ul>
    <Main>
      <Route exact path="/" component={Hoge}></Route>
      <Route path="/foo" component={Foo}></Route>
      <Route path="/bar" component={Bar}></Route>
    </Main>
  </Router>,
  main);
const footer = document.getElementById('footer');
ReactDOM.render(<Footer/>, footer);
