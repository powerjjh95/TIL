import React, { Component } from 'react';
import TOC from './components/TOC'
import Content from './components/Content';
import Subject from './components/Subject';
// import logo from './logo.svg';
import './App.css';

// class Subject extends Component {
//   render() {
//     return (
//       <header>
//         {/* <h1>WEB</h1> */}
//         <h1>{this.props.title}</h1>
//         {this.props.sub}
//         {/* world wide web! */}
//       </header>
//     )
//   }
// }

// class TOC extends Component {
//   render() {
//     return (
//       <nav>
//         <ul>
//           <li><a href="1.html">HTML</a></li>
//           <li><a href="2.html">CSS</a></li>
//           <li><a href="3.html">JavaScript</a></li>
//         </ul>
//       </nav>
//     )
//   }
// }

// class Content extends Component {
//   render() {
//     return (
//       <article>
//         {/* <h2>HTML</h2> */}
//         <h2>{this.props.title}</h2>
//         {this.props.desc}
//         {/* HTML is HyperText Markup Language. */}
//       </article>
//     )
//   }
// }


// 오류 수정
class App extends Component {
  constructor(props) {
    super(props)
    this.state ={
      // mode:'read',
      mode:'welcome',
      subject:{title:'WEB', sub:'World Wide Web!'},
      welcome:{title:'Welcome', desc:'Hello,React!!'},
      read:{title:'Welcome', desc:'Hello,React!!'},
      contents:[
        {id:1, title:'HTML', desc:'HTML is for information'},
        {id:2, title:'CSS', desc:'CSS is for design'},
        {id:3, title:'JavaScript', desc:'JavaScript is for interactive'}
      ]
    }
  }
  render() {
    console.log('App render')
    var _title, _desc = null
    if(this.state.mode === 'welcome') {
      _title = this.state.welcome.title
      _desc = this.state.welcome.desc
    } else if(this.state.mode === 'read') {
      _title = this.state.contents[0].title
      _desc = this.state.contents[0].desc
    }
    return (
      <div className="App">
        {/* Hello, React!! */}
        {/* <Subject 
          title={this.state.subject.title} 
          sub={this.state.subject.sub}></Subject> */}
        <header>
        {/* <h1>WEB</h1> */}
        {/* <h1>{this.props.title}</h1> */}
        <h1><a href="/" onClick={function(e) {
          alert("hi")
          e.preventDefault();
          this.state.mode = "welcome"
        }.bind(this)}>{this.state.subject.title}</a></h1>
        {this.state.subject.sub}
        {/* world wide web! */}
        </header>
        {/* <Subject title="React" sub="For UI"></Subject> */}
        {/* <Subject></Subject> */}
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    )
  }
}

// // 오류 발생
// class App extends Component {
//   render() {
//     return Hello, React!!;
//   }
// }

// class App extends Component {
//   render() {
//     return (
//       <div className='App'>
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <p>
//             Edit <code>src/App.js</code> and save to reload.
//           </p>
//           <a
//             className="App-link"
//             href="https://reactjs.org"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             Learn React
//           </a>
//         </header>
//       </div>
//     )
//   }
// }

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
