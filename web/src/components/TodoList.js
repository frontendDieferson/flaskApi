import React from 'react';

async function deleteData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

async function updateData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

function TodoList({ todos, updateTodos, setTodos }) {

    const removeTask = async (index, todo) => {
        await deleteData('http://localhost:5000/todo/delete',
            todo)
            .then(data => {
                const updatedList = todos.filter((task, taskIndex) => {
                    return taskIndex !== index;
                });
                updateTodos(updatedList);
            })
    }

    const markComplete = async (index, todo) => {
        const updated = { ...todo, complete: !todo.complete }
        await updateData('http://localhost:5000/todo/update',
            updated)
            .then(data => {
                const updatedList = todos.map((item, id) => {
                    if (index !== id) return item;
                    return updated;
                });
                updateTodos(updatedList);
            })
    }
    return (

        <div className="todo-list">
            {todos.map((todo, index) => (
                <div key={index}>
                    <div
                        className={`todo ${todo.complete ? "taskDone" : ""}`}
                        onClick={() => setTodos(markComplete(index))}>
                        Item {index + 1}: {todo.task}
                    </div>
                    <div>
                        <button className="button" onClick={() => removeTask(index, todo)}>Delete</button>
                    </div>

                </div>

            ))}
        </div>
    );
};

export default TodoList;