from weakref import ref
from typing import (Callable, TypeAlias)


# type alias to clean up some type hints. explained in the docstring for `EventHandler.events`.
Subscription: TypeAlias = tuple[ref[object], Callable[["Event"], None]]

class Event:
    '''The base class that all events should inherit from.'''
    pass


class EventHandler:
    '''A class that can register and manage events'''

    events: dict[type[Event], list[Subscription]]
    '''A dictionary of registered events, where the keys are event types, and the values are the subscriptions to a given event type.

    A `Subscription` is a tuple where the first value is a weak reference to the subscriber object, and the second value is a function to be called when the given event is emitted.
    '''

    def __init__(self):
        self.events = {}

    def register_event(self, event: type[Event]) -> bool:
        '''Registers an event into the `EventHandler`.

        Returns `True` if the event was successfully added, returns `False` if the event is already registered.
        '''

        if event in self.events:
            return False
        else:
            self.events[event] = []
            return True

    def subscribe(self, subscriber: object, event: type[Event], callback: Callable[[Event], None]):
        '''Register `subscriber` as being subscribed to `event`, so that whenever the given event type is emitted, `callback` is called on `subscriber`.'''

        # register the event if it isn't already registered
        if event not in self.events:
            self.events[event] = []

        # add the subscription to the event's entry
        self.events[event].append((ref(subscriber), callback))

    def emit_event(self, event: Event) -> bool:
        '''Calls the corresponding registered callback on all subscribers of `event`
        
        Returns `False` if the event isn't registered, returns `True` otherwise.
        '''

        if type(event) not in self.events:
            return False

        # get all of the subscriptions to the event
        subscriptions = self.events[type(event)]

        for subscription in subscriptions:
            # if the object has been garbage collected, remove its subscription. otherwise, call the registered callback.
            if subscription[0]() == None:
                subscriptions.remove(subscription)
            else:
                subscription[1](event)

        return True
