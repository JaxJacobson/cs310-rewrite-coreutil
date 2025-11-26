# Jax Jacobson
# 10/21/25
# Rewrite the base functionality of a GNU Coreutil without calling the original Coreutil.
# I will be changing the GNU Coreutil "whoami" to "me".

import os

# Allow us to get user account information
import pwd

import subprocess

def main ():

    # Get the user's Effective User ID
    user_id = os.geteuid()

    # Get the user's Groupt ID
    group_id = os.getgid()

    # Return only the name linked to the user's password
    username = pwd.getpwuid(user_id).pw_name

    user_path = pwd.getpwuid(user_id).pw_dir

    
#    new_dir = subprocess.run(["sudo", "mkdir", "newcoreutils"])
#
#    subprocess.run(["mv", "whoami.py", "newcoreutils"])


    # Python will look up the cached path if I don't make an edited version.
#    path = os.environ.copy()

#   # Put my whoami2 in front of whoami in the path, so my version shadows the original.
#    path["PATH"] = user_path + new_dir + path["PATH"]

    # path=path makes sure python looks up MY path, not the cached version.
#    subprocess.run(["whoami"], env=path)


    print()
    print("USERNAME : ", username)
    print("USER ID  : ", user_id)
    print("GROUP ID : ", group_id)
    print("USER PATH: ", user_path)
    print()

if __name__ == "__main__":
    main()