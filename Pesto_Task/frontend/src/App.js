import React from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';

function App() {
  return (
    <div className="App">
      <h1>Task Management App</h1>
      <TaskForm />
      <TaskList />
    </div>
  );
}

export default App;
