from setuptools import setup

package_name = 'cut_n_repub'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ilian Voelker',
    maintainer_email='s78393@bht-berlin.de',
    description="A node to cut and republish the Unitree Go1's camera streams into left and right Image Message topics. Requires prior conversion from from gstreamer streams to ROS2 topics, which can be accommplished using gscam.",
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
      	'webcam_repub = cut_n_repub.webcam_repub:main',
      	'go1_front_repub = cut_n_repub.go1_front_repub:main',
      	'go1_all_repub = cut_n_repub.go1_all_repub:main',
        ],
    },
)
