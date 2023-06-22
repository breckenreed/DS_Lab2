import hazelcast

if __name__ == "__main__":

    def write_optimistic_lock():
        client = hazelcast.HazelcastClient(
        cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703"
    ],
    lifecycle_listeners=[
        lambda state: print("New event appeared in lifecycle: ", state),
    ])

        opt_map = client.get_map("OPTI-MAP")
        key = "testing"
        opt_map.put_if_absent(key, 1)

        for i in range(100):
            while True:
                oldValue = opt_map.get( key).result()
                new_value = oldValue +1
                if opt_map.replace_if_same( key, oldValue, new_value ).result():
                    break

        print("Finalized with result: ", opt_map.get(key).result())
        client.shutdown()

    write_optimistic_lock()
 
