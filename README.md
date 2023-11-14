# To-Do-List-App
My First API Development Project


Greetings! and welcome to my inaugural venture into API development! I'm thrilled to introduce my first project, The To-Do List App, a project born from the simplicity of Google Tasks and brought to life through the dynamic duo of FastAPI and MySQL.



## Features ✨

- FastAPI Magic: Built with FastAPI for lightning-fast performance and easy API integration.
- Persistent Storage: Your tasks are securely stored in a MySQL database, ensuring they stay with you across sessions.
- API Awesomeness: Leverage the power of APIs for seamless integration with other applications.


## Getting Started 🚀

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdulsalam-Aderoju/To-Do-List-App.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your MySQL database and update the configuration in `database.py`.

4. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and go to `http://127.0.0.1:8000/docs` to interact with the API using Swagger.


### API Routers and Endpoints

Mission Router
- POST /mission: Create a new mission.
- GET /mission: Retrieve all missions.
- GET /mission/{id}: Retrieve a specific mission.
- PUT /mission/{id}/name: Update a mission’s name.
- PUT /mission/{id}/details: Update a mission’s description .
- PUT /mission/{id}/status: Update a mission’s status.
- DELETE /mission/{id}: Delete a mission.

Task Router
- POST /tasks: Create a new task in a mission.
- GET /tasks/{id}: Retrieve a specific task in a mission.
- PUT /tasks/{id}/name: Update a task’s name.
- PUT /tasks/{id}/details: Update a task’s description .
- PUT /tasks/{id}/status: Update a task’s status.
- DELETE /tasks/{id}: Delete a task.


Other Routers

## Accounts
## Users





## Contributing 🤝

Excited to contribute or make corrections? Follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/awesome-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to your branch: `git push origin feature/awesome-feature`.
5. Submit a pull request!

Will be looking forward to working with anyone interested in giving this a UI, or any additional feature. Thank youuuuuuuuuu.



## Questions and Support 🤔

Having trouble or just want to say hi? Reach out to me at aderojuabdulsalam15@gmail.com.



## Acknowledgments 🙏

Special thanks to Google Tasks for the inspiration and the amazing FastAPI and MySQL communities for making development a joy!



Happy Tasking! 🚀✨
```



