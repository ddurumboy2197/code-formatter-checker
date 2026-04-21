import threading
import time

class DeadlockDetector:
    def __init__(self):
        self.locks = {}

    def acquire(self, lock_id):
        if lock_id not in self.locks:
            self.locks[lock_id] = threading.Lock()
        self.locks[lock_id].acquire()

    def release(self, lock_id):
        if lock_id in self.locks:
            self.locks[lock_id].release()

    def is_deadlock(self):
        for lock_id, lock in self.locks.items():
            if lock.locked():
                print(f"Lock {lock_id} is locked")
                for other_lock_id, other_lock in self.locks.items():
                    if other_lock.locked() and other_lock != lock:
                        print(f"Lock {other_lock_id} is locked")
                        if lock._owner == other_lock._owner:
                            print(f"Deadlock detected: Locks {lock_id} and {other_lock_id} are held by the same thread")
                            return True
        return False

def thread1(lock1, lock2):
    DeadlockDetector().acquire(lock1)
    print("Thread 1 acquired lock 1")
    time.sleep(1)
    DeadlockDetector().acquire(lock2)
    print("Thread 1 acquired lock 2")
    DeadlockDetector().release(lock2)
    DeadlockDetector().release(lock1)

def thread2(lock1, lock2):
    DeadlockDetector().acquire(lock2)
    print("Thread 2 acquired lock 2")
    time.sleep(1)
    DeadlockDetector().acquire(lock1)
    print("Thread 2 acquired lock 1")
    DeadlockDetector().release(lock1)
    DeadlockDetector().release(lock2)

lock1 = "lock1"
lock2 = "lock2"

thread1(lock1, lock2)
thread2(lock1, lock2)

if DeadlockDetector().is_deadlock():
    print("Deadlock detected")
else:
    print("No deadlock detected")
```

Bu kod deadlockni aniqlash uchun mo'ljallangan. U ikkita threadni yaratib, ular o'rtasida deadlock holatini yaratadi. Deadlockni aniqlash uchun `is_deadlock` metodi ishlatiladi.
