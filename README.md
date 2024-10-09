# flask_post_demo
## Trevor DePew

### Description
Demonstrates a `POST` request with validation using Python/Flask.

### Run locally:
`python -i main.py`

### Endpoints:
`localhost:5000/users/create_user`

### Dependencies:
`Flask`
`Flask-SQLAlchemy`

### Expected and Observed Behaviour:

| Request                                                          | Response                                                                            | Status            |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------|
| `{"name": "","age": 42}`                                         | `{"message": {"Error": "Name cannot be empty"},"status": 400}`                      | `400 BAD_REQUEST` |
| `{"name": "01234","age": null}`                                  | `{"message": {"Error": "Age cannot be empty"},"status": 400}`                       | `400 BAD_REQUEST` |
| `{"name": "0123456789012345678901234567890123456789","age": 45}` | `{"message": {"Error": "Name cannot be longer than 32 characters."},"status": 400}` | `400 BAD_REQUEST` |
| `{"name": "01234","age": "42"}`                                  | `{"message": {"Error": "Age must be a number"},"status": 400}`                      | `400 BAD_REQUEST` |
| `{"name": "01234","age": 2}`                                     | `{"message": {"Error": "Age must be 16 or older"},"status": 400}`                   | `400 BAD_REQUEST` |
| `{"name": "01234", "age": 42 }`                                  | `[{"age": 42,"name": "01234"}, 201]`                                                | `201 CREATED`     |
