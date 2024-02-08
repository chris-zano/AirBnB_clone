# <center>AirBnB Clone</center>

This repository hosts the initial phase of a student project aimed at replicating the functionality of the AirBnB website. At this stage, the project introduces a backend interface, known as the console, designed to manage program data efficiently. The console offers commands to create, update, and delete objects, along with functionalities to handle file storage. Through JSON serialization/deserialization, the system ensures persistent storage of data between sessions.

---

## Repository Contents by Project Task

| Task | Files | Description |
| ---- | ----- | ----------- |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Lists project authors |
| 1: Pep8 | N/A | All code adheres to pep8 standards |
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | Modules defining classes are thoroughly unit-tested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes |
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Enhances functionality to recreate class instances from dictionary representations |
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/__init__.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Introduces a class to manage persistent file storage systems |
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Implements basic console functionality, enabling quitting, handling empty lines, and ^D inputs |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Updates the console with methods for creating, deleting, showing, and updating stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements additional classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Enhances the console and file storage system to dynamically work with all classes, updating file storage accordingly |

## General Use

1. Begin by cloning this repository.
2. Once cloned, navigate to the "console.py" file and execute it using the following command:
```
/AirBnB_clone$ ./console.py
```
3. Upon running the command, you should see the following prompt:
```
(hbnb)
```
### Commands
- **create**: Creates an instance based on the provided class.
- **destroy**: Deletes an object based on class and UUID.
- **show**: Displays an object based on class and UUID.
- **all**: Shows all objects accessible to the program or all objects of a specific class.
- **update**: Modifies existing attributes of an object based on class name and UUID.
- **quit**: Exits the program (EOF will as well).

Advanced syntax is implemented for the following commands:
- **all**: Shows all objects accessible to the program or all objects of a specific class.
- **count**: Returns the number of object instances by class.
- **show**: Displays an object based on class and UUID.
- **destroy**: Deletes an object based on class and UUID.
- **update**: Modifies existing attributes of an object based on class name and UUID.
