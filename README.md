# Documents

# 1. Variable
Variable are containers for storing data values.
- Creating variable
- Casting
- Checking type

### Global variable
Global variables can be used by everyone, both inside of functions and outside

# 2. Data types
- Text: str
- Numeric: int, float, complex
- Sequence: list, tuple, range
- Mapping: dict
- Set: set, frozenset
- Boolean: bool
- Binary: bytes,bytearray
- None: NoneType

# 3. String
### Slicing string
- Slice to the end [2:]
- Slice from the start [:2]
- Slice from 2 to 5( not include) [2:5]
- Negate indexing 
### Modify string
- Upper
- Lower
- Remove whitespace at begin or end of string: strip()
- Split string -> list: split(',')
- Replace string
### Concatenate
- Use the + operator

### Format string
Ex: temp = "{2} - {1} = {0}".format(5,2,5-2)

# 4. List, tuple, set, dictionary
##### List
- Store multiple items in a single variable
- Items are ordered.
- Changeable.
- Allow dupplicate values.

##### Dictionary
- Access the items by key name
- Get Items
- Get keys
- Get values
- Update or add item into dictionary: update()
- Remove: del, pop
- Loop in dictionary: thisdict.items() -> keys, values

##### Summary
- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.

# 5. Operators
### Arithmetic 
- (+,-,*,/)
- %: Modulus
- \*\*: Exponentiation
- \\\\: Floor division

### Assignment
- (=, +=, -=, *=, /=, %=, //=, \*\*=, &=,|=, ^=, >>=, <<= ) 

### Comparison
- (==, !=, <, >, <=, >= )

### Logical
- and
- or
- not

### Identity
- is: Returns True if both variables are the same object
- is not: Returns True if both variables are not the same object

### Membership
- in
- not in

### Bitwise
- &: and
- |: or
- ^: XOR
- ~: Not
- <<: Zero fill left shift
- \>\>: Signed right shift

# 6. Functions
- Creating function
- Call function
- Arguments
- Arbitrary Arguments: (\*args): If do not know many arguments that will be passed into function, add *
Function will receive a tuple of arguments
- Arbitrary keyword arguments: (\*\*kwargs)
- Default parameter value
- Return values
- Recursion: defined function can call itself.

# 7. Lambda
- Ex: x = lambda a,b : a\*b
    print(x(5,6))
- Function: 
def myfunc(n)
    return lambda a : a * n
mydoubler =myfunc(2)
print(mydoubler(11))

# 8. Classes/Object
- Object methods
- The self parameter: 
- delete object properties

### Inheritance
- Parent class: base class
- Child class: 

Ex: 
class Person:
    def __init__()

class Student(Person)

###### super()
- Use the super() function: will make the child class inherit all the methods and properties from its parent
- Use the super() function: do not have to use the name of the parent element. It will automatically inherit the methods and properties for its parent

###### Add properties to the child
###### Add methods to the child: 
- The name of methods in the child class have to differcent with the name of function in the parent class. If it is the same name,the parent method will be overridden

 # 9. try...except
 - Try: a block of code for errors
 - except: handle the error
 - else: Execute code when there is no error
 - finally: regardless of the result of the try and except block

 # Module           
## 1. datetime
- Output: date, month, year, hour, minute, second, microsecond
- Format string date output: strftime() method.
Ex
%B: month name, full version
%H: Hour 00-23

Refer: https://www.w3schools.com/python/python_datetime.asp

## 2. math
- Python has a set of built-in math function: (min,max,abs,pow)
- Beside, Python has also a built-in module called math

Refer: https://www.w3schools.com/python/module_math.asp

## 3. Pip
- Pip is a package manager for python packages, or modules.

#### Check if pip is installed 
pip --version

#### Find packages
https://pypi.org/

#### install a package
pip install \<package name\>

#### uninstall a package
pip uninstall \<package name\>

#### List packages
list

## 5. virtualenv
#### Check virtualenv
which virtualenv

#### install 
pip install virtualenv

#### Create a virtual environment
virtualenv <my_env_name>
virtualenv -p "C:\Users\tuan.tran-quoc\AppData\Local\Programs\Python\Python39\python.exe" "env"

#### Activate the virtual environment
source \<my_env_name\>/script/activate

#### Deactivate the virtual environment
deactivate

#### Getting a requirement library
pip freeze > requirements.txt

#### Install packages from requirements.txt file
pip install -r requirements.txt

## 6. os
- Get current dir.
- Rename file.
- Remove file.
- Create dir.
- Check if it is file, dir.
- Check if file or dir exists.
- Create, Join path.
- Get size, modified datetime file.
- List dir or file 

## 7. pandas
[pandas](documents/pandas.md)

