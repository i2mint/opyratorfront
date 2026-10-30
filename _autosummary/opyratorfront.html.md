# opyratorfront

Even quicker way to get webservices, docker containers and GUIs from opyrator

`opyrator` allows us to write code like this:

```pycon
>>> from pydantic import BaseModel
>>>
>>> class Input(BaseModel):
...     message: str
...
>>> class Output(BaseModel):
...     message: str
...
>>> def hello_world(input: Input) -> Output:
...     'Returns the `message` of the input data.'
...     return Output(message=input.message)
```

Putting this in a file named `my_opurator.py` and running

from the command-line, we get a fully functional web GUI for the `hello_world` function.

But to use `opyrator` you need to make those input and output models by hand.
Or do you?…

### Modules

| [`py2pydantic`](opyratorfront.py2pydantic.html.md#module-opyratorfront.py2pydantic)   | Deprecated alias of `front.py2pydantic`.   |
|-------------------------------------------------------------------------------------------------|--------------------------------------------|
