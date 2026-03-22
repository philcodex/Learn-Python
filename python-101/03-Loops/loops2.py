for i in range(2):
    print("Phil")

"""Module to find and report inactive users."""

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": False},
    {"name": "David", "active": True}
]

print("Deactivation List:")
for user in users:
    if not user["active"]:
        # This only runs if 'active' is False
        print(f"- {user['name']} needs to be removed.")

for i in range(20):
    if i % 2 != 0:
        print(i)
    
for i in range(0, 20, 2):
    print(i)

count = 0

while count < 5:
    print(count)
    count +=1
    
count = 0
while count < 5:
    print(count)
    count += 1

tools = ["Postman", "wireshark", "Splunk"]
for tool in tools:
    print("Using", tool)

for i in range(20):
    if i % 2 == 1:
        print(i)

attempts = 0

while attempts < 3:
    print("Trying API request...")
    attempts += 1

attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}: Trying API request")

    # simulate request
    sucess = False

    if sucess:
        print("Request Succeeded")
        break

    attempts += 1

print("Successfully completed API request after 2 attempts")

platform = ["aws", "azure", "gcp"]
for platforms in platform:
    print(f"checking status of {platforms} integration")

servers = ["web01", "web02", "db01", "db02"]

for server in servers:
    print("Pinging:", server)


def greet(name):
    print("Hellooo", name)

greet("Philip")