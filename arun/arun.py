import ansible_runner

print("Welcome to the custom Ansible running tool")

r = ansible_runner.run(private_data_dir='.', playbook='playbook.yml')

if r.rc != 0:
    print("Rollback. The playbook failed.")
else:
    print("Success! nothing to roll back.")
