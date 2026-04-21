from setuptools import find_packages, setup

package_name = 'navigation_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mikachuuu-117',
    maintainer_email='mikachuuu-117@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'sensor = navigation_robot.sensor:main',
		'controller = navigation_robot.controller:main',
		'logger = navigation_robot.logger:main',
        ],
    },
)
