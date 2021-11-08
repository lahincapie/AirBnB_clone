<p align="center">
  <img src="https://github.com/lahincapie/AirBnB_clone/blob/main/assets/hbnb.png" alt="hbnb logo">
</p>

---

## Description

This project's a command-line interface from which you can create modify and delete objects in your file storage.

## Classes:

| Class  | Public Instance Attributes  | Public Instance Methods  | Public Class Attributes  | Private Class Attributes  |
|---|---|---|---|---|
| BaseModel  | id, created_at, updated_at  | save, to_dict  | ****  | ****  |
| FileStorage  | **** | all, new, save, reload  | ****  | file_path, objects  |
| User  | Inherits from BaseModel | ****  | email, password, first_name, last_name  | **** |
| State  | Inherits from BaseModel | ****  | name  | **** |
| City  | Inherits from BaseModel  | **** | state_id, name  | ****  |
| Amenity  | Inherits from BaseModel  | ****  | name  | ****  |
| Place  | Inherits from BaseModel  | ****  | city_id, user_id, name, description, number_rooms, <br>number_bathrooms, max_guest, price_by_night, latitude, longitude, <br>amenity_ids  | ****  |
| Review  | Inherits from BaseModel  | **** | place_id, user_id, text   |  **** |

### Using the Console
#### Console  in non-interactive mode

To run the console in non-interactive mode, pipe the command or commands into a run of the `console.py` file on the command line.
For instance:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```
<p align="center">
  <img src="https://github.com/lahincapie/AirBnB_clone/blob/main/assets/non_interactively.png" alt="Console  in non-interactive mode">
</p>

#### Console in interactive mode

To use the console in interactive mode, run the
file `console.py` :

```
$ ./console.py
```

The console displays a prompt for input:

```
$ ./console.py
(hbnb)
```
<p align="center">
  <img src="https://github.com/lahincapie/AirBnB_clone/blob/main/assets/interactive_mode.png" alt="console in interactive mode">
</p>

#### Exit console

To exit the console, you can use the command quit or EOF.

```
$ ./console.py
(hbnb) quit
$
```

<p align="center">
  <img src="https://github.com/lahincapie/AirBnB_clone/blob/main/assets/quit.png" alt="use of exit command: quit">
</p>

```
$ ./console.py
(hbnb) EOF
$
```

<p align="center">
  <img src="https://github.com/lahincapie/AirBnB_clone/blob/main/assets/eof.png" alt="use of exit command: EOF">
</p>

### Console Commands

| Command  | Prototype  | Example  | Description  |
|---|---|---|---|
| create  |  `create [class name]`  | `create BaseModel`  | Create a new instance of a class. The class ID is displayed and the instance is saved in the file.json file.  |
| show  | `show [class name] [id]` or `[class name].show([id])`  | `show User bd4df4f2-90c3-43f5-9119-25db7e7ca19e`  | returns the string representation of a class instance based on a given id.  |
| destroy  | `destroy [class name] [id]` or `[class name].destroy([id])` | `destroy State bd4df4f2-90c3-43f5-9119-25db7e7ca19e`  | Delete a class instance based on a given id. The archive file file.json is updated after running this command.  |
| all  | `all` or `all [class name]` or `[class name].all()`  | `all BaseModel`  | Displays the string representations of all instances of a given class. If a class name is not entered, the command displays all instances of each class.  |   |
| count  | `count [class name]` or `[class name].count()`  | `count City` | Returns the number of instances of a given class. |
| update | `update [class name] [id] [attribute name] "[attribute value]"` or `[class name].update([id], [attribute name], [attribute value])` or `[class name].update([id], [attribute dictionary])` | User.update(bd4df4f2-90c3-43f5-9119-25db7e7ca19e, {'first_name': 'user, 'last_name': 'Holberton'})  | Updates a class instance based on a given id.  |

#### Console command examples

```
$ ./console.py
(hbnb) create BaseModel
a9505746-54d9-4aee-bea5-226d5a73fcc1
(hbnb) quit
$ cat file.json
{"BaseModel.a9505746-54d9-4aee-bea5-226d5a73fcc1": {"updated_at": "2021-11-07T13:31:40.931399", "created_at": "2021-11-07T13:31:40.931384", "__class__": "Base
Model", "id": "a9505746-54d9-4aee-bea5-226d5a73fcc1"}}
(hbnb) create User
f2a7bf14-12a1-4916-a794-ad20f385804a
(hbnb)
(hbnb) show User f2a7bf14-12a1-4916-a794-ad20f385804a
[User] (f2a7bf14-12a1-4916-a794-ad20f385804a) {'id': 'f2a7bf14-12a1-4916-a794-ad20f385804a', 'created_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32668), 'updated_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32679)}
(hbnb)
(hbnb) User.show(f2a7bf14-12a1-4916-a794-ad20f385804a)
[User] (f2a7bf14-12a1-4916-a794-ad20f385804a) {'id': 'f2a7bf14-12a1-4916-a794-ad20f385804a', 'created_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32668), 'updated_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32679)}
(hbnb) create State
1037701b-a19b-470c-bdf0-252e7567b7b3
(hbnb) create Place
cfb94649-66ca-4c49-b5a6-9d330e5de625
(hbnb) destroy State 1037701b-a19b-470c-bdf0-252e7567b7b3
(hbnb) Place.destroy(cfb94649-66ca-4c49-b5a6-9d330e5de625)
(hbnb) quit
$ cat file.json
{}
(hbnb) create BaseModel
b2ec2b53-c0c0-438e-9bf4-3c4697734eb3
(hbnb) create BaseModel
945c62aa-6b62-4681-8653-174477542749
(hbnb) create User
71bf6acc-13b4-4063-a264-d1a09546c770
(hbnb) create User
cfcfee85-a77f-490f-924d-54be450f0f69
(hbnb) all BaseModel
["[BaseModel] (a9505746-54d9-4aee-bea5-226d5a73fcc1) {'id': 'a9505746-54d9-4aee-bea5-226d5a73fcc1', 'created_at': datetime.datetime(2021, 11, 7, 13, 31, 40, 931384), 'updated_at': datetime.datetime(2021, 11, 7, 13, 31, 40, 931399)}", "[BaseModel] (b2ec2b53-c0c0-438e-9bf4-3c4697734eb3) {'id': 'b2ec2b53-c0c0-438e-9bf4-3c4697734eb3', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 2, 918439), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 2, 918450)}", "[BaseModel] (945c62aa-6b62-4681-8653-174477542749) {'id': '945c62aa-6b62-4681-8653-174477542749', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 13, 408756), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 13, 408766)}"]
(hbnb) User.all()
["[User] (f2a7bf14-12a1-4916-a794-ad20f385804a) {'id': 'f2a7bf14-12a1-4916-a794-ad20f385804a', 'created_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32668), 'updated_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32679)}", "[User] (71bf6acc-13b4-4063-a264-d1a09546c770) {'id': '71bf6acc-13b4-4063-a264-d1a09546c770', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 36, 132313), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 36, 132324)}", "[User] (cfcfee85-a77f-490f-924d-54be450f0f69) {'id': 'cfcfee85-a77f-490f-924d-54be450f0f69', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 38, 572434), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 38, 572446)}"]
(hbnb) all
["[BaseModel] (a9505746-54d9-4aee-bea5-226d5a73fcc1) {'id': 'a9505746-54d9-4aee-bea5-226d5a73fcc1', 'created_at': datetime.datetime(2021, 11, 7, 13, 31, 40, 931384), 'updated_at': datetime.datetime(2021, 11, 7, 13, 31, 40, 931399)}", "[User] (f2a7bf14-12a1-4916-a794-ad20f385804a) {'id': 'f2a7bf14-12a1-4916-a794-ad20f385804a', 'created_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32668), 'updated_at': datetime.datetime(2021, 11, 7, 13, 38, 17, 32679)}", "[BaseModel] (b2ec2b53-c0c0-438e-9bf4-3c4697734eb3) {'id': 'b2ec2b53-c0c0-438e-9bf4-3c4697734eb3', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 2, 918439), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 2, 918450)}", "[BaseModel] (945c62aa-6b62-4681-8653-174477542749) {'id': '945c62aa-6b62-4681-8653-174477542749', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 13, 408756), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 13, 408766)}", "[User] (71bf6acc-13b4-4063-a264-d1a09546c770) {'id': '71bf6acc-13b4-4063-a264-d1a09546c770', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 36, 132313), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 36, 132324)}", "[User] (cfcfee85-a77f-490f-924d-54be450f0f69) {'id': 'cfcfee85-a77f-490f-924d-54be450f0f69', 'created_at': datetime.datetime(2021, 11, 7, 13, 46, 38, 572434), 'updated_at': datetime.datetime(2021, 11, 7, 13, 46, 38, 572446)}"]
(hbnb) create Place
ff8be195-01eb-4461-a6a2-cff1d205a9ea
(hbnb) create Place
60cec8e9-c084-442a-939c-d50707461608
(hbnb) create Place
b8012427-5395-4d82-a5cf-f1a49fe56193
(hbnb) create Place
2ebe93e7-a5c6-4d33-9cc0-43e9728274ae
(hbnb) create City
c0cee25e-c8e8-4f37-af0f-0bd17d8b8105
(hbnb) create City
1cd79866-29da-4ef8-968a-6ad2e6a05e5e
(hbnb) count Place
4
(hbnb) City.count()
2
(hbnb) create User
03181d56-94a6-448b-b86c-028190eb81a7
(hbnb) update User 03181d56-94a6-448b-b86c-028190eb81a7 first_name "Hermione"
(hbnb) show User 03181d56-94a6-448b-b86c-028190eb81a7
[User] (03181d56-94a6-448b-b86c-028190eb81a7) {'id': '03181d56-94a6-448b-b86c-028190eb81a7', 'created_at': datetime.datetime(2021, 11, 7, 13, 52, 57, 456255), 'updated_at': datetime.datetime(2021, 11, 7, 13, 52, 57, 456267), 'first_name': 'Hermione'}
(hbnb) User.update(03181d56-94a6-448b-b86c-028190eb81a7, address, "Privet Drive Number 4")
(hbnb) User.show(03181d56-94a6-448b-b86c-028190eb81a7)
[User] (03181d56-94a6-448b-b86c-028190eb81a7) {'id': '03181d56-94a6-448b-b86c-028190eb81a7', 'created_at': datetime.datetime(2021, 11, 7, 13, 52, 57, 456255), 'updated_at': datetime.datetime(2021, 11, 7, 13, 52, 57, 456267), 'first_name': 'Hermione', 'address': 'Privet Drive Number 4'}
```

## Authors
* **Paola Andrea Garcia Altamirano** <[PaolaAndreaGA](https://github.com/PaolaAndreaGA)>
* **Alejandra Hincapie** <[lahincapie](https://github.com/lahincapie)>