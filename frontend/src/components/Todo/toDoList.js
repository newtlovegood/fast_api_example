import  React, { useState } from  'react';
import { Form } from 'react-bootstrap';
import { nanoid } from 'nanoid';
import  '../../css/todo.css';


function FormTodo({ todo, addTodo, index, changeTodo, changeIsDone, removeTodo }) {

    
    const [is_done, setDone] = useState(false);
    const [value, setValue] = useState(todo.text);

    const handleChange = e => {
      changeTodo(e.target.value, index);
      setValue(e.target.value);
    };

    const markDone = () => {
      changeIsDone(!is_done, index)
      setDone(!is_done);
    };

    const handleSubmit = e => {
      e.preventDefault();
      if (!value) return;
      addTodo();
    };

    const handleRemove = () => {
      removeTodo(index);
      setValue('');
      setDone(false);
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
          <input type="button" className=" btn btn-lg btn-danger" value='X' onClick={() => handleRemove(index)}></input>
        </div>

    </Form>
    );
  }


  function ToDoList() {

    const [todos, setTodos] = useState([{'text': '', 'is_done': false, 'id': nanoid()}]);
  
    const addTodo = () => {
      const newTodos = [...todos];
      newTodos.push({'text': '', 'is_done': false, 'id': nanoid()});
      setTodos(newTodos);
    };

    const changeTodo = (text, index) => {
      const newTodos = [...todos];
      newTodos[index].text = text;
      setTodos(newTodos);
    }

    const changeIsDone = (is_done, index) => {
      const newTodos = [...todos];
      newTodos[index].is_done = is_done;
      setTodos(newTodos);
    }

    const removeTodo = index => {
      let newTodos = [...todos];
      
      if (newTodos.length === 1) {
        newTodos[0].text = '';
        newTodos[0].is_done = false;
      } else {
        newTodos.splice(index, 1);
      }
      setTodos(newTodos);
    };
  
    return (
      <div className="app">
        <div className="container">
          <h1 className="text-center mb-4">Todo List</h1>
          <div>
            {todos.map((todo, index) => (
                <FormTodo
                  key={todo.id}
                  index={index}
                  todo={todo}
                  addTodo={addTodo}
                  changeTodo={changeTodo}
                  changeIsDone={changeIsDone}
                  removeTodo={removeTodo}
                />
            ))}
          </div>
        </div>
      </div>
    );
  }


  export default ToDoList;
