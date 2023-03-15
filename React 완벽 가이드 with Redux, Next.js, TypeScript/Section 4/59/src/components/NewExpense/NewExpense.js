import React from "react";

import ExpenseForm from "./ExpenseForm";
import "./NewExpense.css";

function NewExpense() {
  // const saveExpenseDataHandler = (enteredExpenseData) => {
  //   const expenseData = {
  //     ...enteredExpenseData,
  //     id: Math.random().toString(),
  //   };
  //   console.log(expenseData);
  // };

  return (
    <div className="new-expense">
      <ExpenseForm />
      {/* <ExpenseForm onSaveExpenseData /> */}
    </div>
  );
}

export default NewExpense;
