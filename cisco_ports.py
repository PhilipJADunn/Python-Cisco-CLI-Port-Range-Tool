#Cisco CLI port range tool

changes = True

nat = 'ip nat inside source static'
interface = 'interface Dialer1'

while changes:
    protocol = input('What protocol are you opening ports for (udp/tcp): ')
    ip = input('What is the internal IP address that traffic will be routed to: ')
    lowerRange = int(input('Please enter your starting port: '))
    upperRange = int(input('Please enter your final port: '))

    for i in range (lowerRange, upperRange+1):
        print(nat, protocol, ip, i, interface, i)

    again = input('\nDo you wish to run the programme again? y/n: ')
    if again.startswith('n'):
        changes = False

#Made by Philip Dunn
