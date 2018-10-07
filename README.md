# A Python observer pattern implementation
The classic observer pattern uses two classes:
- Observable: This class is the provider of the observed state as implemented by the sub type
- Observer: This class is the observer that listens to updates from the provider

## Example usage
```python
from Observer import Observable, Observer

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
    publisher.attach(NewValueSubscriber())
    publisher.value = 5
```

##Prerequisites
Python2.6+ [Install python2.7](https://www.python.org/downloads/)
