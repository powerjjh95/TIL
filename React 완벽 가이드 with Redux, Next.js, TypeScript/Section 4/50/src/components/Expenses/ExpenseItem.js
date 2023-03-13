import React from "react";

import ExpenseDate from "./ExpenseDate";
import Card from "../UI/Card";
import "./ExpenseItem.css";

// function ExpenseItem(props) {
//   return (
//     <Card className="expense-item">
//       {/* <div>{props.date.toISOString()}</div> */}
//       <ExpenseDate date={props.date} />
//       <div className="expense-item__description">
//         {/* <h2>{expenseTitle}</h2> */}
//         <h2>{props.title}</h2>
//         <div className="expense-item__price">${props.amount}</div>
//       </div>
//       <button
//         onClick={() => {
//           console.log("Clicked!");
//         }}
//       >
//         Change Title
//       </button>
//     </Card>
//   );
// }

const ExpenseItem = (props) => {
  // function clickHandler() {}

  const clickHandler = () => {
    console.log("Clicked!!!!");
  };
  return (
    <Card className="expense-item">
      {/* <div>{props.date.toISOString()}</div> */}
      <ExpenseDate date={props.date} />
      <div className="expense-item__description">
        {/* <h2>{expenseTitle}</h2> */}
        <h2>{props.title}</h2>
        <div className="expense-item__price">${props.amount}</div>
      </div>
      {/* <button
        onClick={() => {
          console.log("Clicked!");
        }}
      >
        Change Title
      </button> */}
      <button onClick={clickHandler}>Change Title</button>
    </Card>
  );
};

export default ExpenseItem;
