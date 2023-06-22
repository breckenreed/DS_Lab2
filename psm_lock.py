import time
import hazelcast

if __name__ == "__main__":

    def write_pessimistic_lock():
        print("Starting pessimistic write")
        # Connect to Hazelcast cluster.
        client = hazelcast.HazelcastClient(
        cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703"
    ],
    lifecycle_listeners=[
        lambda state: print("New event appeared in lifecycle: ", state),
    ])

        lock_map = client.get_map("lock-map")
        key = "test_val"
        lock_map.put_if_absent(key, 1)

        for i in range(100):
            lock_map.lock(key).result()
            try:
                value = lock_map.get(key).result()
                #print("Value var type: ", type(value)) 
                value += 1
                lock_map.put(key, value).result()
            finally:
                lock_map.unlock(key)

        print("Finalized with result: ", lock_map.get(key).result())
        
    write_pessimistic_lock()
