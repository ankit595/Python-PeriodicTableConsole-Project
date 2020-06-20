# Elements declaration

from termcolor import colored

elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulphur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
atomic_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117','118']
property = ['Nonmetal', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Nonmetal', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Post-Transition Metal', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Metalloid', 'Metalloid', 'Nonmetal', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Metalloid', 'Metalloid', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Metalloid', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Halogen', 'Noble Gas']


# Function For choosing search by Element_Name Or search by Atomic_Number
def periodic_table():
    choice = int(input('''\tFor Searching Elements By Name Press 1\n\tFor Searching Elements By Atomic_Number Press 2 \n\t\t:'''))
    if choice == 1:
        return By_name()

    elif choice == 2:
        return By_Atomic_Number()

    else:
        print(colored('PLEASE!!! Press Right Key','red',attrs=['bold','underline']))
        return periodic_table()

# Function
def By_name():
    print("Enter the element name starting with First Capital letter")
    search = str(input('Enter Element Name: '))
    if search in elements:
        index = elements.index(search)
        ele = elements[index]
        sym = symbols[index]
        atom = atomic_number[index]
        prop = property[index]
        print(colored('''\t\tSymbol: {0}\n\t\tAtomic Number: {1}\n\t\tElement: {2}\n\t\tProperty: {3}\n'''.format(sym, atom, ele, prop),'green',attrs=['bold']))
    else:
        print(colored('Element not Found, Check the name whether it\'s first letter is capital or not and Try again','red',attrs=['bold']))
    again = int(input('Wants to search Again: \nIf yes press 1\nIf no press 2\n\t\t:'))
    if again == 1:
        return periodic_table()
    elif again == 2:
        print(colored('THANK YOU!!!','yellow',attrs=['bold']))
    else:
        print(colored('PLEASE!!! press right key','red',attrs=['bold']))
        return periodic_table()

def By_Atomic_Number():
    search = str(input('Enter Atomic_Number: '))
    if search in atomic_number:
        index = atomic_number.index(search)
        ele = elements[index]
        sym = symbols[index]
        atom = atomic_number[index]
        prop = property[index]
        print(colored('''\t\tSymbol: {0}\n\t\tAtomic Number: {1}\n\t\tElement: {2}\n\t\tProperty: {3}\n'''.format(sym, atom, ele, prop),'green',attrs=['bold']))
    else:
        print(colored('Element not Found,PLEASE!!! Check the Atomic_Number whether it is between 1-118','red',attrs=['bold']))
    again = int(input('Wants to search Again: \nIf yes press 1\nIf no press 2\n\t\t:'))
    if again == 1:
        return periodic_table()
    elif again == 2:
        print(colored('THANK YOU!!!', 'yellow',attrs=['bold']))
    else:
        print(colored('PLEASE!!! press right key', 'red', attrs=['bold']))
        return periodic_table()

periodic_table()
