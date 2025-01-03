from setuptools import setup, find_packages

setup(
    name="car_number_plate_detection",
    version="0.1",
    author="Rohit Ghorpade",
    author_email="rohitghorpade098@gmail.com",
    description="A real-time car number plate detection system using OpenCV and Haar Cascade Classifier.",
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    
)
