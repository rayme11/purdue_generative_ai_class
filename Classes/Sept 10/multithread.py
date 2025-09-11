# Generate example using multithreading in Python
# Document each step with comments showing when things are executed, locked, and unlocked, etc.
import threading
import time

# Shared resource (start at a higher integer for clarity)
shared_resource = 100

# Lock for synchronizing access to the shared resource
lock = threading.Lock()

def increment():
    global shared_resource
    end_time = time.time() + 30  # Run for 30 seconds
    while time.time() < end_time:
        # Waiting to lock
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Increment: Waiting to lock")
        lock.acquire()  # Locking the shared resource
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Increment: Locked")
        shared_resource += 1
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Increment: Incremented to {shared_resource}")
        lock.release()  # Unlocking the shared resource
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Increment: Unlocked")
        time.sleep(0.2)  # Sleep to make thread activity visible

def decrement():
    global shared_resource
    end_time = time.time() + 30  # Run for 30 seconds
    while time.time() < end_time:
        # Waiting to lock
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Decrement: Waiting to lock")
        lock.acquire()  # Locking the shared resource
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Decrement: Locked")
        shared_resource -= 1
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Decrement: Decremented to {shared_resource}")
        lock.release()  # Unlocking the shared resource
        print(f"[{time.strftime('%H:%M:%S')}] Thread-Decrement: Unlocked")
        time.sleep(0.2)  # Sleep to make thread activity visible

# Creating threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

# Final value of the shared resource
print("Final value of shared resource:", shared_resource)
# Expected output is close to the starting value, as increments and