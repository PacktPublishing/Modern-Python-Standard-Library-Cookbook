import struct

with open('/tmp/packet.dump', 'wb') as f:
    data = struct.pack('>HHLL', 50291, 80, 2778997212, 644363807)
    f.write(data)
print(data)

with open('/tmp/packet.dump', 'rb') as f:
    data = struct.unpack_from('>HHLL', f.read())
print(data)

