import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="wifi-password-tool",
    version="1.2.0",
    author="Sardar Muhammad Zeeshan Khan",
    author_email="Zeshankhan1996@hotmail.com",
    description="A tool to quickly fetch your WiFi password and generate a QR code for easy device connection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/wifi-password-tool",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["wifi-password = wifi_password_tool.wifi_password:main"]},
    install_requires=["qrcode", "Pillow", "Colorama"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
