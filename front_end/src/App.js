// import logo from './logo.svg';
import pes from './title.png';
import './App.css';
import React from 'react'; 
// import axios from 'axios';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={pes} alt="PeopleEatSmart" />
        {/* <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
      <footer>
        <cite class="Author"> 
          -- 4peeps 
        </cite>
      </footer>
    </div>
  );
}

// class App_Randy extends React.Component {
  
//   state = {
//       details : [],
//   }

//   componentDidMount() {

//       let data ;

//       axios.get('http://127.0.0.1:8000/api/randy/')
//       .then(res => {
//           data = res.data;
//           this.setState({
//               details : data    
//           });
//       })
//       .catch(err => {})
//   }

//   render() {
//     return (
//       <div>
//         {this.state.details.map((detail, id) => (
//           <div className="App">
//             <header className="App-header">
//               <img src={pes} alt="PeopleEatSmart" />
//             </header>
//             <h3>Username: {detail.username}</h3>
//             <h4>Password: {detail.password}</h4>
//             <footer>
//               <cite class="Author"> 
//                 -- 4peeps 
//               </cite>
//             </footer>
//           </div>
//           )
//         )}
//       </div>
//     );
//   }
// }

export default App;
