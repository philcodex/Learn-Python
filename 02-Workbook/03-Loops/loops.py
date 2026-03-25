"""This module contains exercises for practicing loops in Python."""

for i in range(14):
    print("Checking server")


def my_function():
    """This function prints a simple greeting."""
    print("Hello")

for i in range(5):
    print("This is a loop")
    print("This is still part of the loop")
for i in range(5):
    print("This is a loop")
print("This is not part of the loop")



new_hires = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Instead of 'i', we use a descriptive name like 'person'
for person in new_hires:
    print(f"Creating Stripe account for: {person}")

    """Module to demonstrate processing a list of SaaS platforms."""

platforms = ["Slack", "Jira", "GitHub", "Okta"]

for app in platforms:
    # We use an 'f-string' to inject the variable into the text
    print(f"Checking integration status for: {app}")

# Stripe SaaS Operations Interview Example: Processing Customer Subscriptions
# In SaaS operations, we often need to process lists of data like customer subscriptions,
# calculate metrics, or perform batch operations.

subscriptions = [
    {"customer_id": "cus_123", "plan": "Basic", "amount": 29.99, "status": "active"},
    {"customer_id": "cus_456", "plan": "Pro", "amount": 99.99, "status": "active"},
    {"customer_id": "cus_789", "plan": "Enterprise", "amount": 299.99, "status": "past_due"},
    {"customer_id": "cus_101", "plan": "Basic", "amount": 29.99, "status": "canceled"},
    {"customer_id": "cus_202", "plan": "Pro", "amount": 99.99, "status": "active"}
]

total_revenue = 0
active_customers = 0
past_due_alerts = []

for subscription in subscriptions:
    # Calculate total revenue from active subscriptions
    if subscription["status"] == "active":
        total_revenue += subscription["amount"]
        active_customers += 1
        print(f"Processed payment for {subscription['customer_id']}: ${subscription['amount']}")
    
    # Flag past due accounts for follow-up
    elif subscription["status"] == "past_due":
        past_due_alerts.append(subscription["customer_id"])
        print(f"ALERT: Past due payment for {subscription['customer_id']}")

print(f"\nSummary:")
print(f"Total active customers: {active_customers}")
print(f"Total monthly revenue: ${total_revenue:.2f}")
print(f"Past due accounts requiring attention: {len(past_due_alerts)}")
if past_due_alerts:
    print(f"Customer IDs: {', '.join(past_due_alerts)}")

for i in range(10, 110, 10):
    print(i)

numbers = [10, 20, 30]
for number in numbers:
    print(number)


import os
for _ in range(20):
    os.system("ping -c 1 google.com")

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

print(10 %3)

print(-10 % 3)

list = [1, 2, 3]
print(list)

for number in range(5):
    print("attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print(number)  

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue # gets to 13 and continues
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break # gets to 13 and breaks out of loop
    else:
        print(x)

