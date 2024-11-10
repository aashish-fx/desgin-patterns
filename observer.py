# Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
# Use the Observer pattern when changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or changes dynamically.

# // The base publisher class includes subscription management
# // code and notification methods.
# class EventManager is
#     private field listeners: hash map of event types and listeners

#     method subscribe(eventType, listener) is
#         listeners.add(eventType, listener)

#     method unsubscribe(eventType, listener) is
#         listeners.remove(eventType, listener)

#     method notify(eventType, data) is
#         foreach (listener in listeners.of(eventType)) do
#             listener.update(data)

# // The concrete publisher contains real business logic that's
# // interesting for some subscribers. We could derive this class
# // from the base publisher, but that isn't always possible in
# // real life because the concrete publisher might already be a
# // subclass. In this case, you can patch the subscription logic
# // in with composition, as we did here.
# class Editor is
#     public field events: EventManager
#     private field file: File

#     constructor Editor() is
#         events = new EventManager()

#     // Methods of business logic can notify subscribers about
#     // changes.
#     method openFile(path) is
#         this.file = new File(path)
#         events.notify("open", file.name)

#     method saveFile() is
#         file.write()
#         events.notify("save", file.name)

#     // ...


# // Here's the subscriber interface. If your programming language
# // supports functional types, you can replace the whole
# // subscriber hierarchy with a set of functions.
# interface EventListener is
#     method update(filename)

# // Concrete subscribers react to updates issued by the publisher
# // they are attached to.
# class LoggingListener implements EventListener is
#     private field log: File
#     private field message: string

#     constructor LoggingListener(log_filename, message) is
#         this.log = new File(log_filename)
#         this.message = message

#     method update(filename) is
#         log.write(replace('%s',filename,message))

# class EmailAlertsListener implements EventListener is
#     private field email: string
#     private field message: string

#     constructor EmailAlertsListener(email, message) is
#         this.email = email
#         this.message = message

#     method update(filename) is
#         system.email(email, replace('%s',filename,message))


# // An application can configure publishers and subscribers at
# // runtime.
# class Application is
#     method config() is
#         editor = new Editor()

#         logger = new LoggingListener(
#             "/path/to/log.txt",
#             "Someone has opened the file: %s")
#         editor.events.subscribe("open", logger)

#         emailAlerts = new EmailAlertsListener(
#             "admin@example.com",
#             "Someone has changed the file: %s")
#         editor.events.subscribe("save", emailAlerts)


from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
