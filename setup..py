from setuptools import setup, find_packages

setup(
    name="car_number_plate_detection",
    version="0.1",
    author="Rohit Ghorpade",
    author_email="rohitghorpade098@gmail.com",
    description="A real-time car number plate detection system using OpenCV and Haar Cascade Classifier.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/car_number_plate",
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
