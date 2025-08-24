import os

from dotenv import load_dotenv
from gbox_sdk import GboxSDK

# Load environment variables from .env file
load_dotenv()

# Setup the SDK
gbox = GboxSDK(api_key=os.getenv("GBOX_API_KEY"))


# Linux box example initial
def linux_example():

    # Create a Linux box
    linux_box = gbox.create(type="linux")

    # Run Python code in the box
    result = linux_box.run_code(code='print("Hello from Python!")', language="python")

    # Print execution result
    print(f"\n- LINUX BOX ({linux_box.data.id}):\n\n{result}\n")


# Android Example
def android_example():

    # Create an Android box
    android_box = gbox.create(type="android")

    # Click
    android_box.action.click(x=100, y=100)

    # Screenshot
    android_box.action.screenshot(path="screenshot.png")


def main():

    # Run examples
    linux_example()
    android_example()


if __name__ == "__main__":
    main()
