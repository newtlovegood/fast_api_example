import  React, { useState } from  'react';
import { Button, Card, Form } from 'react-bootstrap';
// import 'bootstrap/dist/css/bootstrap.min.css';
import  '../../css/todo.css';

import ToDoItem from './toDoItem';



function FormTodo({ todo, addTodo, index, changeTodo, removeTodo }) {

  
    const [is_done, setDone] = useState(false);
    const [value, setValue] = useState(todo.text);

    const handleChange = e => {
      setValue(e.target.value);
      changeTodo(value, index);
    };

    const markDone = () => {
        todo.is_done = !todo.is_done;
    };

    const handleSubmit = e => {
      e.preventDefault();
      if (!value) return;
      addTodo();
    };
  
    return (
      <Form onSubmit={handleSubmit}> 
        <div className="input-group mb-3">
          <div className="input-group-prepend">
            <div className="input-group-text">
              <input type="checkbox" aria-label="Checkbox for following text input" checked={is_done} onChange={markDone}></input>
            </div>
          </div>
          <input style={{ textDecoration: is_done ? "line-through" : "" }} type="text" autoFocus className="form-control" value={value} onChange={(e) => {handleChange(e)}} placeholder="Add new todo"></input>
          <input type="button" className=" btn btn-lg btn-danger" value='X' onClick={() => removeTodo(index)}></input>
        </div>


      {/* <Form.Group>
        <Form.Check type='checkbox' checked={is_done} onChange={markDone} />
        <Form.Control style={{ textDecoration: is_done ? "line-through" : "" }}type="text" className="input" value={value} onChange={e => setValue(e.target.value)} placeholder="Add new todo" />
        <Button variant="outline-danger" onClick={() => removeTodo(index)}>✕</Button>
      </Form.Group> */}

    </Form>
    );
  }


  function ToDoList() {

    const [todos, setTodos] = useState([{'text': ''}]);
  
    const addTodo = () => {
      const newTodos = [...todos];
      newTodos.push({'text': ''});
      setTodos(newTodos);
    };

    const changeTodo = (text, index) => {
      const newTodos = [...todos];
      newTodos[index].text = text;
      setTodos(newTodos);
    }

    const removeTodo = index => {
      let newTodos = [...todos];
      
      if (newTodos.length === 1) {
        newTodos[0].text = '';
      } else {
        newTodos.splice(index, 1);
      }
      setTodos(newTodos);
         
    };
  
    return (
      <div className="app">
        <div className="container">
          <h1 className="text-center mb-4">Todo List</h1>
          {/* <FormTodo key={0} index={0} addTodo={addTodo} removeTodo={removeTodo} /> */}
          <div>
            {todos.map((todo, index) => (
                <FormTodo
                  key={index}
                  index={index}
                  todo={todo}
                  addTodo={addTodo}
                  changeTodo={changeTodo}
                  removeTodo={removeTodo}
                />
            ))}
          </div>
        </div>
      </div>
    );
  }


  export default ToDoList;
