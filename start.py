#!/usr/bin/env python3

import yaml
import os
import subprocess

def print_banner():
    banner = '''
 ______     __     ______     __    __     ______     __   __     ______     __  __     ______  
/\  ___\   /\ \   /\  ___\   /\ "-./  \   /\  __ \   /\ "-.\ \   /\  __ \   /\ \/\ \   /\__  _\ 
\ \___  \  \ \ \  \ \ \__ \  \ \ \-./\ \  \ \  __ \  \ \ \-.  \  \ \  __ \  \ \ \_\ \  \/_/\ \/ 
 \/\_____\  \ \_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\\"\_\  \ \_\ \_\  \ \_____\    \ \_\ 
  \/_____/   \/_/   \/_____/   \/_/  \/_/   \/_/\/_/   \/_/ \/_/   \/_/\/_/   \/_____/     \/_/ 
                                                                                                 
 __    __     ______     ______     ______                                                       
/\ "-./  \   /\  ___\   /\  ___\   /\  __ \                                                      
\ \ \-./\ \  \ \  __\   \ \ \__ \  \ \  __ \                                                     
 \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\ \_\                                                    
  \/_/  \/_/   \/_____/   \/_____/   \/_/\/_/                                                    
                                                                                                 
 ______     ______     ______     ______                                                         
/\  ___\   /\  __ \   /\  == \   /\  ___\                                                        
\ \ \____  \ \ \/\ \  \ \  __<   \ \  __\                                                        
 \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\                                                      
  \/_____/   \/_____/   \/_/ /_/   \/_____/                                        
'''
    print(banner)

def read_config():
    with open('conf/conf.yaml', 'r') as file:
        return yaml.safe_load(file)

def start_services(config):
    services = config.get('services', {})
        
    for service, enabled in services.items():
        if enabled:
            print(f"Starting {service} service...")
            subprocess.run(['docker', 'compose', 'up', '-d', service])
        else:
            print(f"{service} service is disabled in configuration.")

    # Always start nginx last
    if services.get('nginx', True):  # Default to True if not specified
        print("Starting nginx service...")
        subprocess.run(['docker', 'compose', 'up', '-d', 'nginx'])

if __name__ == "__main__":
    print_banner()
    print("Starting Sigmanaut Node Core services...")
    config = read_config()
    start_services(config)
    print("Startup complete.")
