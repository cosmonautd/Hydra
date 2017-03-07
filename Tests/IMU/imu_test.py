import smbus
import math
import time

def twos_complement(value, bits):
    if (value & (1 << (bits - 1))) != 0:
        value = value - (1 << bits)
    return value

def get_data(address):
    high  = bus.read_byte_data(bus_address, address)
    low   = bus.read_byte_data(bus_address, address+1)
    value = (high << 8) + low
    return twos_complement(value, 16)

POWER_1 = 0x6b
POWER_2 = 0x6c
ACCEL_X = 0x3b
ACCEL_Y = 0x3d
ACCEL_Z = 0x3f
GYRO_X  = 0x43
GYRO_Y  = 0x45
GYRO_Z  = 0x47

bus = smbus.SMBus(1)
bus_address = 0x68

bus.write_byte_data(bus_address, POWER_1, 0)
bus.write_byte_data(bus_address, 0x1b, 0)
bus.write_byte_data(bus_address, 0x1c, 0)

gyro_x_off = 0
gyro_y_off = 0
gyro_z_off = 0

accel_x_off = 0
accel_y_off = 0
accel_z_off = 0

for i in range(1000):

    gyro_x_off += get_data(GYRO_X)
    gyro_y_off += get_data(GYRO_Y)
    gyro_z_off += get_data(GYRO_Z)

    accel_x_off += get_data(ACCEL_X)
    accel_y_off += get_data(ACCEL_Y)
    accel_z_off += get_data(ACCEL_Z)

    time.sleep(0.001)

gyro_x_off, gyro_y_off, gyro_z_off = gyro_x_off/1000, gyro_y_off/1000, gyro_z_off/1000
accel_x_off, accel_y_off, accel_z_off = accel_x_off/1000, accel_y_off/1000, accel_z_off/1000

while True:

    print()

    gyro_x = get_data(GYRO_X) - gyro_x_off
    gyro_y = get_data(GYRO_Y) - gyro_y_off
    gyro_z = get_data(GYRO_Z) - gyro_z_off
    gyro_x_scaled, gyro_y_scaled, gyro_z_scaled = gyro_x / 131, gyro_y / 131, gyro_z / 131
    print("gyro x:", gyro_x, "  scaled:", gyro_x_scaled)
    print("gyro y:", gyro_y, "  scaled:", gyro_y_scaled)
    print("gyro z:", gyro_z, "  scaled:", gyro_z_scaled)

    print()

    accel_x = get_data(ACCEL_X) - accel_x_off
    accel_y = get_data(ACCEL_Y) - accel_y_off
    accel_z = get_data(ACCEL_Z) - accel_z_off
    accel_x_scaled, accel_y_scaled, accel_z_scaled = accel_x / 16384, accel_y / 16384, accel_z / 16384
    print("accel x:", accel_x, "  scaled:", accel_x_scaled)
    print("accel y:", accel_y, "  scaled:", accel_y_scaled)
    print("accel z:", accel_z, "  scaled:", accel_z_scaled)

    time.sleep(0.1)
