# A simple Python observer pattern implementation
The classic observer pattern uses two classes:
- Observable: This class is the provider of the observed state as implemented by the sub type
- Observer: This class is a registered subscriber listening to updates from the provider

## Example usage
The below example application resides in observer.py and can be run by running the module.
```python
from observer import Observable, Observer

class NewValueSubscriber(Observer):
    def __init__(self):
        super(NewValueSubscriber, self).__init__()

    def update(self, new_value):
        print('{} received new value: {}'.format(self.name, new_value[0]))

class NewValuePublisher(Observable):
    def __init__(self):
        super(NewValuePublisher, self).__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        print('{} updating new value: {} to observers'.format(self.name, value))
        self.notify(value)

publisher = NewValuePublisher()
listener = NewValueSubscriber()
listener2 = NewValueSubscriber()
publisher.attach(listener)
publisher.attach(listener)  # this is ignored
publisher.attach(listener2)
publisher.value = 5
publisher.detach(listener)
publisher.value = 6  # only listener2 is updated
publisher.detach(listener2)  # last listener is detached
publisher.value = 7  # nobody is updated
```

This gives the following console output:
```commandline
$ python observer.py 
New value: 5
NewValuePublisher updating new value: 5 to observers
NewValueSubscriber0 received new value: 5
NewValueSubscriber1 received new value: 5
New value: 6
NewValuePublisher updating new value: 6 to observers
NewValueSubscriber1 received new value: 6
New value: 7
```

## Prerequisites

Works for both Python2.6+ or python3
[Install python](https://www.python.org/downloads/)

## Install this package directly
Get this package by issuing the following command:
```console
$ pip install git+https://github.com/FrederikBjorne/python-observer
```

then import it like this:

```
from observer import ...
```
