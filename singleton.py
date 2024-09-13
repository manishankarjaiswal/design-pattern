import threading
import copy
import pickle

class SingletonMeta(type):
    """
    A thread-safe Singleton metaclass.
    """
    _instances = {}
    _lock = threading.Lock()  # Ensures thread-safety for singleton instantiation

    def __call__(cls, *args, **kwargs):
        # Critical section where instance creation happens
        with cls._lock:
            if cls not in cls._instances:
                # If the class does not have an instance, create one
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """
    Singleton class. This class enforces the Singleton behavior using SingletonMeta.
    """
    def __copy__(self):
        """
        Prevent creating a new instance via copy.
        """
        return self

    def __deepcopy__(self, memo):
        """
        Prevent creating a new instance via deepcopy.
        """
        return self

    def __reduce__(self):
        """
        Ensure that unpickling does not create a new instance.
        """
        return (self.__class__, ())

# Example usage of Singleton
if __name__ == "__main__":
    # Test: Ensure only one instance is created, even in multi-threaded environments
    def create_singleton_instance():
        singleton = Singleton()
        print(f"Singleton instance: {singleton}")

    thread1 = threading.Thread(target=create_singleton_instance)
    thread2 = threading.Thread(target=create_singleton_instance)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    # Test: Singleton with pickling
    singleton = Singleton()
    singleton_pickled = pickle.loads(pickle.dumps(singleton))
    
    print(f"Singleton is pickled and unpickled: {singleton is singleton_pickled}")  # True

    # Test: Singleton with copying
    singleton_copy = copy.copy(singleton)
    singleton_deepcopy = copy.deepcopy(singleton)

    print(f"Singleton is same after copy: {singleton is singleton_copy}")  # True
    print(f"Singleton is same after deepcopy: {singleton is singleton_deepcopy}")  # True
