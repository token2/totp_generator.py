# totp_generator.py
/\* CSS for code blocks \*/ pre { background-color: #f4f4f4; border: 1px solid #d1d1d1; border-radius: 5px; padding: 10px; font-family: 'Courier New', monospace; white-space: pre-wrap; } /\* CSS for inline code \*/ code { background-color: #f4f4f4; border: 1px solid #d1d1d1; border-radius: 3px; padding: 2px; font-family: 'Courier New', monospace; } /\* CSS for headings \*/ h1, h2 { color: #333; } /\* CSS for links \*/ a { color: #007acc; }

TOTP Code Generator with Skew
=============================

This Python script allows you to generate Time-based One-Time Passwords (TOTP) using the PyOTP library. It also displays TOTP codes with a time skew, showing multiple OTPs around the current time.

Requirements
------------

*   Python 3.x
*   PyOTP library (you can install it using `pip install pyotp`)

Usage
-----

You can use this script to generate TOTP codes with the given secret key and display multiple codes around the current time.

1.  Make sure you have Python 3.x installed on your system.
2.  Install the PyOTP library using `pip install pyotp` if you haven't already.
3.  Run the script with the following command:

    python totp_generator.py your_secret_key [--num-otp NUM_OTP]

*   `your_secret_key`: Replace this with your TOTP secret key.
*   `--num-otp NUM_OTP` (optional): Specify the number of OTPs to display. The default is 5 OTPs.

Output
------

The script will display TOTP codes with a time skew, showing OTPs before and after the current time. The current OTP is displayed in green for easy identification.

Example
-------

    $ python totp_generator.py your_secret_key --num-otp 5
    Time: 2023-10-11 15:10:30, TOTP code: 123456
    Time: 2023-10-11 15:10:00, TOTP code: 789012
    Time: 2023-10-11 15:09:30, TOTP code: 345678
    Time: 2023-10-11 15:09:00, TOTP code: 901234
    Time: 2023-10-11 15:08:30, TOTP code: 456789

The current TOTP code is displayed in green.

License
-------

This script is provided under the MIT License.

_Note: Replace `your_secret_key` with your actual TOTP secret key when using the script. The `--num-otp` argument is optional, and you can adjust it to display the desired number of OTPs._
