# Impoting termcolor for using Printing coloured sentences


from termcolor import colored

# Elements declaration

elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus','Sulphur', 'Chlorine', 'Ar6gon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
atomic_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117','118']
property = ['Nonmetal', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Nonmetal', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Post-Transition Metal', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Metalloid', 'Metalloid', 'Nonmetal', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Metalloid', 'Metalloid', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Lanthanide', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Metalloid', 'Halogen', 'Noble Gas', 'Alkali Metal', 'Alkaline Earth Metal', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Actinide', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Post-Transition Metal', 'Halogen', 'Noble Gas']
atomic_mass=[1.0079,4.0026,6.941,9.0122,10.811,12.0107,14.0067,15.9994,18.9984,20.1797,22.9897,24.305,26.9815,28.0855,30.9738,32.065,35.453,39.948,39.0983,40.078,44.9559,47.867,50.9415,51.9961,54.938,55.845,58.9332,58.6934,63.546,65.39,69.723,72.64,74.9216,78.96,79.904,83.8,85.4678,87.62,88.9059,91.224,92.9064,95.94,98,101.07,102.9055,106.42,107.8682,112.411,114.818,118.71,121.76,127.6,126.9045,131.293,132.9055,137.327,138.9055,140.116,140.9077,144.24,145,150.36,151.964,157.25,158.9253,162.5,164.9303,167.259,168.9342,173.04,174.967,178.49,180.9479,183.84,186.207,190.23,196.9665,192.217,195.078,200.59,204.3833,207.2,208.9804,209,210,222,223,226,227,232.0381,231.0359,238.0289,237,244,243,247,247,251,252,257,258,259,262,261,262,266,264,277,268,261.9,271.8,285,286,289,288,293,260.9,294]
discovery_year=[1776,1895,1817,1797,1808,'Ancient',1772,1774,1886,1898,1807,1755,1825,1824,1669,'Ancient',1774,1894,1807,1808,1879,1791,1830,1797,1774,'Ancient',1735,1751,'Ancient','Ancient',1875,1886,'Ancient',1817,1826,1898,1861,1790,1794,1789,1801,1781,1937,1844,1803,1803,'Ancient',1817,1863,'Ancient','Ancient',1783,1811,1898,1860,1808,1839,1803,1885,1885,1945,1879,1901,1880,1843,1886,1867,1842,1879,1878,1907,1923,1802,1783,1925,1803,'Ancient',1803,1735,'Ancient',1861,'Ancient','Ancient',1898,1940,1900,1939,1898,1899,1829,1913,1789,1940,1940,1944,1944,1949,1950,1952,1952,1955,1958,1961,1964,1967,1974,1981,1984,1982,1994,1994,1996,2003,1998,2010,2000,2010,2006]

# Function For choosing search by Element_Name Or search by Atomic_Number
def periodic_table():
    choice = input('''\n\tFor Searching Elements By Name Press 1\n\tFor Searching Elements By Atomic_Number Press 2 \n\t\t:''')
    if choice == '1':
        return By_name()

    elif choice == '2':
        return By_Atomic_Number()

    else:
        print(colored('PLEASE!!! Press Right Key','red',attrs=['bold','underline']))
        return periodic_table()

# Function for searching by Atomic name
def By_name():
    print("Enter the element name starting with First Capital letter")
    search = str(input('Enter Element Name: '))
    if search in elements:
        index = elements.index(search)
        ele = elements[index]
        sym = symbols[index]
        atom = atomic_number[index]
        prop = property[index]
        mass = atomic_mass[index]
        year = discovery_year[index]
        print(colored('''\t\tSymbol: {0}\n\t\tAtomic Number: {1}\n\t\tAtomic Mass:{4}\n\t\tElement: {2}\n\t\tProperty: {3}\n\t\tDiscovery Year: {5}'''.format(sym, atom, ele, prop,mass,year),'green',attrs=['bold']))
    else:
        print(colored('Element not Found, Check the name whether it\'s first letter is capital or not and Try again','red',attrs=['bold','underline']))
    repeat()
# Function for searching by Atomic number
def By_Atomic_Number():
    search = str(input('Enter Atomic_Number: '))
    if search in atomic_number:
        index = atomic_number.index(search)
        ele = elements[index]
        sym = symbols[index]
        atom = atomic_number[index]
        prop = property[index]
        mass = atomic_mass[index]
        year = discovery_year[index]
        print(colored('''\t\tSymbol: {0}\n\t\tAtomic Number: {1}\n\t\tAtomic Mass:{4}\n\t\tElement: {2}\n\t\tProperty: {3}\n\t\tDiscovery Year: {5}'''.format(sym, atom, ele, prop,mass,year),'green',attrs=['bold']))
    else:
        print(colored('Element not Found,PLEASE!!! Check the Atomic_Number whether it is between 1-118','red',attrs=['bold','underline']))
    repeat()

# Function for Repeatitoion
def repeat():
    again = input('Wants to search Again: \nIf yes press 1\nIf no press 2\n\t\t:')
    if again == '1':
        return periodic_table()
    elif again == '2':
        print(colored('THANK YOU!!!', 'yellow', attrs=['bold']))
    else:
        print(colored('PLEASE!!! press right key', 'red', attrs=['bold', 'underline']))
        return repeat()
periodic_table()
