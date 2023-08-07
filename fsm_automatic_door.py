from __future__ import annotations
from abc import ABC, abstractmethod

class AutomaticDoor:

    _state = None

    def __init__(self, state: State) -> None:
        self.setDoor(state)

    # method to change the state of the object
    def setDoor(self, state: State):

        self._state = state
        self._state.door = self

    def presentState(self):
        print(f"Door is {type(self._state).__name__}.")

    # methods for executing the Automatic Door functionality (depends on the current state of the object)
    def front(self):
        self._state.front()

    def rear(self):
        self._state.rear()

    # if there is someone in front and rear at the same time, nothing should happen
    def frontAndRear(self) -> None:
        print("Oops.. the automatic door won't move when there are people in the front and the rear both, simutaneously")

    # if neither front nor rear is occupied, door should be closed
    def nofrontOrRear(self) -> None:
        print("The door will be closed")


# The common state interface for all the states
class State(ABC):
    @property
    def door(self) -> AutomaticDoor:
        return self._door

    @door.setter
    def door(self, door: AutomaticDoor) -> None:
        self._door = door

    @abstractmethod
    def front(self) -> None:
        pass

    @abstractmethod
    def rear(self) -> None:
        pass


# The concrete states
# We have two states of the door: when it is closed or when it is open
class closed(State):

    def rear(self) -> None:
        print("The Automatic Door is in Closed state.")

    def front(self) -> None:
        print("The Automatic Door is opening.")
        self.door.setDoor(open())


class open(State):

    # if there is no one in the front, the door should close
    def rear(self) -> None:
        print("Careful... The Automatic door will close now.")
        self.door.setdoor(closed())

    # if someone is in the front of the door, nothing should happen
    def front(self) -> None:
        print("The Automatic Door is already Open.")


if __name__ == "__main__":
    # The client code

    myDoor = AutomaticDoor(closed())
    myDoor.presentState()

    # There is someone in the front of the door
    myDoor.front()

    myDoor.presentState()
