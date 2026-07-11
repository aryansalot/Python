import re 

common_pass = ['123456', 'password', '123456789', '12345678', '12345', '111111', '1234567', 'sunshine', 'qwerty', 'iloveyou', 'princess', 'admin', 'welcome', '666666', 'abc123', 'football', '123123', 'monkey', '654321', '!@#$%^&*', 'charlie', 'aa123456', 'donald', 'password123', 'qwerty123', '1q2w3e4r', '123qwe', 'zxcvbnm', '1qaz2wsx', 'qazwsx', 'qwertyuiop', 'asdfghjkl', 'zxcvbn', 'qwerty1', '1234', '123456a', '1234567890', '123456789a', '123456789q', '123456789z', '123456789x', '123456789c', '123456789v', '123456789b', '123456789n', '123456789m', '123456789l', '123456789k', '123456789j', '123456789h', '123456789g', '123456789f', '123456789d', '123456789s', '123456789a1', 'password1', 'password2']

def check_password_strength(password):
    
    score = 0
    feedback = []
    
    if len(password) >= 10:
        score += 1
    else:
        feedback.append("Password length must at least 10 character")
        
    if re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("Add at least one lowercase character in password")
        
    if re.search(r"[A-Z]",password):
        score += 1
    else:
        feedback.append("Add at least one uppercase character in password")
    
    if re.search(r"[!@#$%^&*()<>,.?/;:]",password):
        score += 1
    else:
        feedback.append("Add at least one Special character in password")
        
    if re.search(r"[0-9]",password):
        score += 1
    else:
        feedback.append("Add at least one number in passwrord")
        
    if password not in common_pass:
        score += 1
    else:
        feedback.append("Password is too common, try to use uncommon password")
    
    if score <= 4: 
         strength = "Weak"
    elif score <= 7:
         strength = "Moderete"
    else:
         strength = "Strong"

    return score,strength,feedback

def main():
    
    password = input("Enter Password: ")
    score,strength,feedback = check_password_strength(password)
    
    print("------------------ Result------------------")
    print(f"Scpre: {score}/10")
    print(f"Strength: {strength}")
    
    if feedback:
        print("Suggestion to Improve")
        for tip in feedback:
            print(f" -- {tip}")
    else:
        print(f"{password} is meet all criteria")

if __name__ == "__main__":
    main()