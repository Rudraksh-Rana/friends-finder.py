
def input_friends(user):
    friends = input(f"Enter friends of {user} (separated by commas): ")
    return set(friend.strip() for friend in friends.split(","))

def find_mutual_friends(user1, user2, friends_dict):
    friends1, friends2 = friends_dict.get(user1, set()), friends_dict.get(user2, set())
    mutual_friends = friends1.intersection(friends2)
    print(f"Mutual friends between {user1} and {user2}: {', '.join(mutual_friends) if mutual_friends else 'None'}")

def find_common_friends(users, friends_dict):
    common_friends = friends_dict.get(users[0], set())
    for user in users[1:]:
        common_friends &= friends_dict.get(user, set())  
    print(f"Common friends among users {', '.join(users)}: {', '.join(common_friends) if common_friends else 'None'}")

def find_all_friends(users, friends_dict):
    all_friends = friends_dict.get(users[0], set())
    for user in users[1:]:
        all_friends |= friends_dict.get(user, set())  
    print(f"All unique friends among users {', '.join(users)}: {', '.join(all_friends)}")

def main():
    friends_dict = {}
    num_users = int(input("Enter the number of users: "))

    for i in range(num_users):
        user = input(f"Enter the name of user {i+1}: ")
        friends_dict[user] = input_friends(user)

    if input("\nDo you want to find mutual friends between two users? (y/n): ").lower() == 'y':
        user1, user2 = input("Enter the first user: "), input("Enter the second user: ")
        find_mutual_friends(user1, user2, friends_dict)

    if input("\nDo you want to find common friends among multiple users? (y/n): ").lower() == 'y':
        users = input("Enter users (separated by commas): ").split(",")
        find_common_friends(users, friends_dict)

    if input("\nDo you want to find all unique friends among multiple users? (y/n): ").lower() == 'y':
        users = input("Enter users (separated by commas): ").split(",")
        find_all_friends(users, friends_dict)

if __name__ == "__main__":
    main()
