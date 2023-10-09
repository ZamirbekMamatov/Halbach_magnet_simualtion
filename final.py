import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy

DIMENSION_h = 20
DIMENSION_d = 10
r = DIMENSION_d * np.sqrt(3) / 6 + 1
ARBITARY_Z = r + DIMENSION_h / 2 + 6
DISTANCE_X = DIMENSION_d / 2 + 2
DISTANCE_Y = ARBITARY_Z * np.sqrt(3) / 2
DISTANCE_Z = ARBITARY_Z / 2
MAG_x = 0
MAG_y = 0
MAG_z = 1100

DIMENSION_h_t = 30
DIMENSION_b_t = 20
DIMENSION_a_t = 10
r = DIMENSION_a_t * np.sqrt(3) / 6 + 0.5
ARBITARY_Z_t = r + DIMENSION_h_t / 2
DISTANCE_X_t = DIMENSION_b_t / 2 + 2
DISTANCE_Y_t = ARBITARY_Z_t * np.sqrt(3) / 2
DISTANCE_Z_t = ARBITARY_Z_t / 2
sensor_pos = [0, 0, 0]

# Cylinderic magnets
magnet1 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[-DISTANCE_X, DISTANCE_Y, DISTANCE_Z])
magnet1.rotate_from_angax(angle=-60, axis='x')

magnet2 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[-DISTANCE_X, 0, -ARBITARY_Z])
magnet2.rotate_from_angax(angle=-180, axis='x')

magnet3 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[-DISTANCE_X, -(DISTANCE_Y), DISTANCE_Z])
magnet3.rotate_from_angax(angle=-300, axis='x')

magnet4 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[DISTANCE_X, DISTANCE_Y, DISTANCE_Z])
magnet4.rotate_from_angax(angle=120, axis='x')

magnet5 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[DISTANCE_X, 0, -ARBITARY_Z])
magnet5.rotate_from_angax(angle=0, axis='x')

magnet6 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[DISTANCE_X, -(DISTANCE_Y), DISTANCE_Z])
magnet6.rotate_from_angax(angle=-120, axis='x')

# extra cylinders

magnet7 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[-DISTANCE_X - 10, DISTANCE_Y, DISTANCE_Z])
magnet7.rotate_from_angax(angle=-60, axis='x')

magnet8 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[-DISTANCE_X - 10, 0, -ARBITARY_Z])
magnet8.rotate_from_angax(angle=-180, axis='x')

magnet9 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                position=[-DISTANCE_X - 10, -(DISTANCE_Y), DISTANCE_Z])
magnet9.rotate_from_angax(angle=-300, axis='x')

magnet10 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                 position=[DISTANCE_X + 10, DISTANCE_Y, DISTANCE_Z])
magnet10.rotate_from_angax(angle=120, axis='x')

magnet111 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                  position=[DISTANCE_X + 10, 0, -ARBITARY_Z])
magnet111.rotate_from_angax(angle=0, axis='x')

magnet12 = magpy.magnet.Cylinder(magnetization=(MAG_x, MAG_y, MAG_z), dimension=(DIMENSION_d, DIMENSION_h),
                                 position=[DISTANCE_X + 10, -(DISTANCE_Y), DISTANCE_Z])
magnet12.rotate_from_angax(angle=-120, axis='x')

# Cuboid magnets
magnet11 = magpy.magnet.Cuboid(magnetization=(MAG_x, MAG_y, MAG_z),
                               dimension=(DIMENSION_b_t, DIMENSION_a_t, DIMENSION_h_t),
                               position=[-DISTANCE_X_t, -DISTANCE_Y_t, -DISTANCE_Z_t])
magnet11.rotate_from_angax(angle=120, axis='x')

magnet21 = magpy.magnet.Cuboid(magnetization=(MAG_x, MAG_y, MAG_z),
                               dimension=(DIMENSION_b_t, DIMENSION_a_t, DIMENSION_h_t),
                               position=[-DISTANCE_X_t, 0, ARBITARY_Z_t])
magnet21.rotate_from_angax(angle=0, axis='x')

magnet31 = magpy.magnet.Cuboid(magnetization=(MAG_x, MAG_y, MAG_z),
                               dimension=(DIMENSION_b_t, DIMENSION_a_t, DIMENSION_h_t),
                               position=[-DISTANCE_X_t, (DISTANCE_Y_t), -DISTANCE_Z_t])
magnet31.rotate_from_angax(angle=-120, axis='x')

magnet41 = magpy.magnet.Cuboid(magnetization=(MAG_x, MAG_y, MAG_z),
                               dimension=(DIMENSION_b_t, DIMENSION_a_t, DIMENSION_h_t),
                               position=[DISTANCE_X_t, -DISTANCE_Y_t, -DISTANCE_Z_t])
magnet41.rotate_from_angax(angle=-60, axis='x')

magnet51 = magpy.magnet.Cuboid(magnetization=(MAG_x, MAG_y, MAG_z),
                               dimension=(DIMENSION_b_t, DIMENSION_a_t, DIMENSION_h_t),
                               position=[DISTANCE_X_t, 0, ARBITARY_Z_t])
magnet51.rotate_from_angax(angle=180, axis='x')

magnet61 = magpy.magnet.Cuboid(magnetization=(MAG_x, MAG_y, MAG_z),
                               dimension=(DIMENSION_b_t, DIMENSION_a_t, DIMENSION_h_t),
                               position=[DISTANCE_X_t, (DISTANCE_Y_t), -DISTANCE_Z_t])
magnet61.rotate_from_angax(angle=60, axis='x')

col = magpy.Collection(
    magnet1, magnet2, magnet3, magnet4, magnet5, magnet6,
    magnet7, magnet8, magnet9, magnet10, magnet111, magnet12,
    magnet11, magnet21, magnet31, magnet41, magnet51, magnet61,

)
# Create a sensor and position it
sensor = magpy.Sensor(position=sensor_pos)

magpy.show(col, sensor, backend='plotly')

# Calculate B-field on a grid
xs = np.linspace(-40, 40, 100)
zs = np.linspace(-40, 40, 100)
Bs = np.array([[col.getB([x, 0, z]) for x in xs] for z in zs])

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Display field in xz-plane using matplotlib
X, Z = np.meshgrid(xs, zs)
U, V = Bs[:, :, 0], Bs[:, :, 2]
splt = ax.streamplot(X, Z, U, V, color=np.sqrt(U ** 2 + V ** 2), density=5, cmap='inferno')
ax.set_title('Magnetic Field Lines in XZ-plane')

ax.plot([-1.5, 1.5, 1.5, -1.5, -1.5], [r, r, -r, -r, r], "k--", lw=2)

normalization = np.sqrt(sensor.getB(col)[0] ** 2 + sensor.getB(col)[1] ** 2 + sensor.getB(col)[2] ** 2)

# Add colorbar
cb = plt.colorbar(splt.lines, ax=ax, label="|B| (mT)")
ax.set(
    xlabel="x-position (mm)",
    ylabel="z-position (mm)",
)
print(f'magnetic field strength at {sensor_pos} position is {round(normalization, 2)} mT')
print(f"inner circle diameter is {round(r * 2, 2)} mm")
plt.tight_layout()
plt.show()