import subprocess


'''
wifi card device is enp3s0
'''

new_mac_address = 'ee:75:f4:55:5e'

subprocess.call('ifconfig enp3s0 down', shell=True)
subprocess.call('ifconfig enp3s0 hw ether ee:75:f4:55:5e', shell=True)
subprocess.call('ifconfig enp3s0 up', shell=True)
