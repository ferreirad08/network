from network import Network

network = Network(remote_host='www.anaconda.com')
network.ping(count=4)
print('Network is connected:', network.is_connected())
print('Port:', network.get_port())
