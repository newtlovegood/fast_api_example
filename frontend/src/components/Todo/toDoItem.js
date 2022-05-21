import  React, { useState } from  'react';
import { Button, Form } from 'react-bootstrap';
import  '../../css/todo.css';




function ToDoItem({ todo, index, removeTodo }) {

    const [is_done, setDone] = useState(false);

    const markDone = () => {
        setDone(!is_done);
    };

    return (
      <div
        className="todo"
      >
          {/* <Form.Check aria-label="option 3"  checked={is_done} onChange={markDone} /> */}
          <div className='checkbox'>
            <input type='checkbox' style={{transform: "scale(2)"}} checked={is_done} onChange={markDone}></input>
          </div>
          <div className='todo-text'>
            <h3 style={{ textDecoration: is_done ? "line-through" : "" }}>{todo.text}</h3>
          </div>
          <div className='remove-btn'>
            <Button variant="outline-danger" onClick={() => removeTodo(index)}>✕</Button>
          </div>
      </div>
    );
  }

export default ToDoItem;