import os
from glob import glob
from setuptools import setup

package_name = 'talker_listener'

setup(
  name=package_name,
  version='0.0.0',
  packages=[package_name],
  data_files=[
    ('share/ament_index/resource_index/packages',
      ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'launch/'), glob('launch/*launch.[pxy][yma]*')),
],
  install_requires=['setuptools'],
  zip_safe=True,
  maintainer='tanjim',
  maintainer_email='shoebtanjim@outlook.com',
  description='TODO: Package description',
  license='TODO: License declaration',
  tests_require=['pytest'],
  entry_points={
    'console_scripts': [
      'talkerNode = talker_listener.talker:main',
      'listenerNode = talker_listener.listener:main'
    ],
},
)
