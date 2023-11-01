import argparse
import pyotp
import time

# ANSI escape codes for text color
GREEN = '\033[92m'  # Green color
RESET = '\033[0m'    # Reset color to default

def generate_totp(secret, num_otp=5, algorithm='sha1', digits=6, interval=30):
    totp = pyotp.TOTP(secret, digits=digits, digest=algorithm, interval=interval)
    totp_list = []
    current_time = int(time.time())
    
    for i in range(-num_otp//2, num_otp//2 + 1):
        generated_time = current_time + (i * interval)
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(generated_time))
        totp_code = totp.at(generated_time)
        
        if i == 0:
            # Display the current OTP in green
            formatted_line = f"{GREEN}Time: {formatted_time}, TOTP code: {totp_code}{RESET}"
        else:
            formatted_line = f"Time: {formatted_time}, TOTP code: {totp_code}"
        
        totp_list.append(formatted_line)
    
    return totp_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate TOTP codes with skew")
    parser.add_argument("secret", help="Your secret key")
    parser.add_argument("--num-otp", type=int, default=5, help="Number of OTPs to display")
    
    args = parser.parse_args()

    totp_list = generate_totp(args.secret, args.num_otp)
    
    for line in totp_list:
        print(line)
