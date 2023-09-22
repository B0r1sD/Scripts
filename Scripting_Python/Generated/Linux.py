import subprocess
'''
# Run the 'ls' command
ls_output = subprocess.run(["ls"], stdout=subprocess.PIPE).stdout.decode()

# Print the output
print(ls_output)
'''


# Run the 'bash' shell in interactive mode
bash_shell = subprocess.Popen(["bash", "-i"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Loop indefinitely
while True:
    # Read a command from the user
    command = input("> ")

    # Send the command to the bash shell
    bash_shell.stdin.write(command.encode() + b"\n")

    # Flush the stdin buffer
    bash_shell.stdin.flush()

    # Read the output from the shell
    output = bash_shell.stdout.readline().decode()

    # Print the output
    print(output)
