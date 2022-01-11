import "./styles.css";
import { code } from "./striverCode.js";
import { useState } from "react";

export default function App() {
  const topics = Array.from(new Set(code.map((item) => item.type)));

  const [topicSelected, setTopic] = useState("arrays");
  function setTopicOnClick(topic) {
    setTopic(topic);
  }
  return (
    <div className="App">
      <div>
        <h1 className="header">striver sheet</h1>

        <div>
          <button onClick={() => setTopicOnClick("all")}>all</button>
          {topics.map((item) => {
            return (
              <button onClick={() => setTopicOnClick(item)}>{item}</button>
            );
          })}
        </div>
      </div>
      <hr />

      <ul>
        {code.map((item) => {
          return (
            (topicSelected === "all" || item.type === topicSelected) && (
              <ProblemDisplay item={item}></ProblemDisplay>
            )
          );
        })}
      </ul>
    </div>
  );
}

function ProblemDisplay(props) {
  return (
    <li>
      <div className="listItem">
        <p>{props.item.question}</p>
        <small>{props.item.date}</small>
        <a href={props.item.problem} className="btn-code">
          question
        </a>
        <a href={props.item.solution} className="btn-code">
          solution
        </a>
      </div>
    </li>
  );
}
