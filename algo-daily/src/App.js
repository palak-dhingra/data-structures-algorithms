import "./styles.css";
import { useState } from "react";
import { algoDailyDictionary } from "./dailyAlgoDictionary.js";

export default function App() {
  var types = Object.keys(algoDailyDictionary);
  const [typeSelected, setType] = useState("problems");
  function setTypeSelected(type) {
    setType(type);
  }

  return (
    <div className="App">
      <div className="header">
        <h1>algo-daily</h1>
        <div>
          {types.map((item) => {
            return (
              <button key={item} onClick={() => setTypeSelected(item)}>
                {item}
              </button>
            );
          })}
        </div>
      </div>
      <hr />
      {typeSelected === "problems" && (
        <ProblemApp type={typeSelected} data={algoDailyDictionary} />
      )}
      {typeSelected === "quotes" && (
        <QuotesApp type={typeSelected} data={algoDailyDictionary} />
      )}
    </div>
  );
}

function ProblemApp(props) {
  return (
    <ul>
      {props.data[props.type].map((item) => {
        return (
          <li className="listItem">
            <div>
              <p className="problemDesc">{item.description}</p>
              <small className="problemDate">{item.date}</small>
              <a href={item.problem} className="problemBtn">
                question
              </a>
              <a href={item.answer} className="problemBtn">
                solution
              </a>
            </div>
          </li>
        );
      })}
    </ul>
  );
}

function QuotesApp(props) {
  return (
    <ul>
      {props.data[props.type].map((item) => {
        return (
          <li className="listItem quote">
            <div>
              <p>{item.quote}</p>
              <p>{item.author}</p>
            </div>
          </li>
        );
      })}
    </ul>
  );
}
