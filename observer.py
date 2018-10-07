#!/usr/bin/env python

from abc import ABCMeta
from abc import abstractmethod


class Observer(object):
    """
    This abstract class represents the observer listening for updates from the Observable (Subject).
    A concrete observer implementation inheriting from this class, registers itself to the Observable
    class object for updates by calling Observable.attach. Notifications of a new state is received
    in the Observer.update implementation of the sub type where any threading or queueing may be put
    if needed by the application.

    Typical usage:
        >>> from Observer import Observer
        >>> class NewValueSubscriber(Observer):
        ...     def __init__(self):
        ...         super(NewValueSubscriber, self).__init__()
        ...         self._value = 0
        ...     def update(self, new_value):
        ...         print('{} received new value: {}'.format(self._name, new_value[0]))
    """
    __metaclass__ = ABCMeta

    def __init__(self, name=None):
        self.name = name if name else self.__class__.__name__

    @abstractmethod
    def update(self, *new_state):
        """
        Called by the concrete Observable when data has changed passing its state (aka new value).
        :param new_state: The new state.
        :param new_state: The new state.
        :type new_state: A tuple of arbitrary content.
        """
        pass

    @classmethod
    def __subclasshook__(cls, sub_class):  # correct behavior when isinstance, issubclass is called
        return any(cls.update.__str__() in klazz.__dict__ for klazz in sub_class.__mro__) != []


class Observable(object):
    """
    This base class represents an observable (also known as a subject or publisher) with a one-to-many
    relationship with its registered observers.
    A concrete observer implementation may register for updates using the attach method.

    Typical usage:
        >>> from Observer import Observable
        >>> class NewDataPublisher(Observable):
        ...     def __init__(self):
        ...         super(NewDataPublisher, self).__init__()
        ...         self._value = 0
        ...     @property
        ...     def value(self):
        ...         return self._value
        ...     @value.setter
        ...     def value(self, value):
        ...         self._value = value
        ...         self.notify(value)
        ...
    """

    def __init__(self, name = None):
        self.name = name if name else self.__class__.__name__
        self._observers = set()  # use a set to avoid duplicate registered observers

    def attach(self, observer):
        """
        Attach an Observer wanting to be notified of updates from the concrete Observable.
        :param observer: The listener object to be removed.
        :type observer: Observer
        :raise ValueError is raised if the observer object is not of type Observer
        """
        if not isinstance(observer, Observer):
            raise ValueError('You need to pass a valid Observer class object')
        self._observers.add(observer)

    def detach(self, observer):
        """
        Detaches an Observer from listening to updates from the concrete Observable.
        :param observer: The listener object to be removed.
        :type observer: Observer
        """
        if observer in self._observers:
            self._observers.discard(observer)

    def notify(self, *new_state):
        """
        The new state is updated to all registered Observers.
        :param new_state: The new state.
        :type new_state: A tuple of arbitrary content.
        """
        for observer in self._observers:
            observer.update(new_state)


if __name__ == "__main__":

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
            self.notify(value)  # using a property for updating value and subscribers/observers

    publisher = NewValuePublisher()
    publisher.attach(NewValueSubscriber())
    publisher.value = 5
