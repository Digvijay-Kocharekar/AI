P_B = float(input("Enter the probability of burglary: "))

P_E = float(input("Enter the probability of earthquake: "))

P_D_given_A = float(input("Enter the probability that John calls given the alarm sounded: "))

P_S_given_A = float(input("Enter the probability that Mary calls given the alarm sounded: "))

P_A_given_notB_notE = float(input("Enter the probability of the alarm sounding given there is no burglary or earthquake: "))

P_A_notB_notE = (1 - P_B) * (1 - P_E)
P_D_and_S_given_A_notB_notE = P_D_given_A * P_S_given_A
P_D_and_S = P_D_and_S_given_A_notB_notE * P_A_notB_notE * P_A_given_notB_notE

print("The probability that the alarm has sounded, but there is neither a burglary nor an earthquake occurred, and John and Mary both called User is:", P_D_and_S)