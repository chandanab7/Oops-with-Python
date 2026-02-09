# Task/Assignment:
# Problem Statement
# Create a program for an Instagram Account System using Encapsulation.
# Requirements
# Create a class named InstagramAccount
# Public Variable
# account_name
# Protected Variable
# _private_reels (list of strings)
# Private Variable
# __archived_reels (list of strings)
# Methods to Implement
# 1. add_private_reel(reel_name)
# Adds a reel into _private_reels
# 2. display_private_reels(is_follower)
# If is_follower is True → display all private reels
# Else → print "Access Denied! Only followers can view private reels"
# 3. add_archived_reel(reel_name)
# Adds a reel into __archived_reels
# 4. display_archived_reels(password)
# If password is correct → display all archived reels
# Else → print "Access Denied! Only account holder can view archived reels"
# 5. getter method for archived reels
# Create a getter method to return archived reels only if password is correct
# 6. setter method to update password
# Create a setter method to update password
# Task
# Create one object of InstagramAccount
# Add at least 2 private reels
# Add at least 2 archived reels
# Display private reels as follower and non-follower
# Display archived reels using correct and wrong password
# Update password using setter and check again
# Push the code to github.



class InstagramAccount:
    # Public variable
    account_name = "" #class variable meaning it is shared among all objects of the class

    def __init__(self, account_name, password):
        self.account_name = account_name
        # Protected variable
        self._private_reels = [] #instance variable meaning it is specific to each object of the class
        # Private variable
        self.__archived_reels = []
        self.__password = password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # 2. Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # 4. Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # 5. Getter method for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            print("Access Denied!")
            return None

    # 6. Setter method to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password")
    # Create object
account = InstagramAccount("chandana_official", "insta123")

# Add private reels
account.add_private_reel("Vacation Reel")
account.add_private_reel("Birthday Reel")

# Add archived reels
account.add_archived_reel("Old Dance Reel")
account.add_archived_reel("College Memories Reel")

# Display private reels
print("\nAs Follower:")
account.display_private_reels(True)

print("\nAs Non-Follower:")
account.display_private_reels(False)

# Display archived reels
print("\nArchived Reels with Correct Password:")
account.display_archived_reels("insta123")

print("\nArchived Reels with Wrong Password:")
account.display_archived_reels("wrongpass")

# Update password
print("\nUpdating Password:")
account.set_password("insta123", "newpass456")

# Check archived reels again
print("\nArchived Reels after Password Change:")
account.display_archived_reels("newpass456")


