# Airbnb Clone Project

This project is an Airbnb clone, designed to mimic the functionality of the popular online platform for booking accommodations. It provides a command-line interface (CLI) for managing properties, users, bookings, and other aspects of the application.

## Command Interpreter

The command interpreter is a CLI tool that allows users to interact with the Airbnb clone system. It provides a set of commands for performing various actions such as creating properties, managing users, and making bookings.

### Starting the Command Interpreter

To start the command interpreter, simply run the `console.py` file using Python:

```bash
python console.py
```

### Using the Command Interpreter

Once the command interpreter is running, you can enter commands to perform different actions within the application. The available commands include:

- `create <class_name>`: Create a new instance of a class (e.g., create User).
- `show <class_name> <id>`: Show details of a specific instance.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Update the attributes of a specific instance.
- `destroy <class_name> <id>`: Delete a specific instance.
- `all <class_name>`: Show details of all instances of a specific class.
- `quit`: Exit the command interpreter.

### Examples

- To create a new user: `create User`
- To show details of a specific property: `show Place 1234`
- To update the name of a user: `update User 5678 name "John Doe"`
- To delete a specific booking: `destroy Booking 9876`
- To show details of all properties: `all Place`
