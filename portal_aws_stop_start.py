import boto3
instance_id= ["Priovide instance id"]
]

ec2 = boto3.client("ec2")

def manage_ec2 (action):
    if action== "start":
        print(f"sendind start command to {instance_id}")
        ec2.start_instances(InstanceIds=instance_id)
        print("Start command send successfully It may few seconds to start the instance")
        
    elif action== "stop":
        print(f"Sending stop command to {instance_id}")
        ec2.stop_instances(InstanceIds=instance_id)
        print("Stop command sent successfully. It may take a few seconds to stop the instance.")
        
    else:
        print("Invalid action. Please use 'start' or 'stop'.")
        
manage_ec2("stop")
