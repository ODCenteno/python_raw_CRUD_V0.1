
import csv
import os

'''
A Python Project to develop a CRUD(create, read, update, delete)
'''
CLIENT_TABLE = '/Users/omardaniel/Documents/Platzi/Backend/CRUD/.clients.csv'
    # Constante que indica el nombre del archivo.
    # .clients.csv para ser archivo oculto.
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []                        

# Función que abre el archivo que contiene la información de clientes
def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode = 'r') as f:     # Utilizamos context manager with. r = read
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)    # agregamos datos requeridos

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = (f'{CLIENT_TABLE}.tmp')
    with open(tmp_table_name, mode = 'w') as f:
        writer = csv.DictWriter(f, fieldnames = CLIENT_SCHEMA)

        writer.writerows(clients)
    
    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)

# Función que añade un nuevo cliente a la variable clients
def create_client(client):
    global clients              # La función global aumenta el alcance de la función y permite 
                                # utilizar     la variable clients
    if client not in clients:   # Revisamos si el cliente está en la lista.
        clients.append(client)  # Función append para agregar el dict con los datos del cliente
    else:
        print("\nClient already is in the client's list\n")


# Función que imprime la lista de clientes
def list_clients():
    global clients

    print(f"\n >> Client | 'Id' |    'Name'    |   'company'   |      'email'      |     'position'     |")
    print('-' * 90)

    for idx, client in enumerate(clients):  # Función enumerate(): Agrega un contador
        print(f"        >> |  {idx}   |    {client['name']}    |    {client['company']}    | {client['email']} |   {client['position']}  |\n")


# Función que actualiza el nombre del cliente
def update_client(client_id, updated_client):
    global clients

    if len(clients) -1 >= client_id:
        print(f"\n\tReady to Update Client Fields:\n")

        clients[client_id] = updated_client
        # updated_client_name = input(f"\n\t> UPDATE < the client's name\n\tWhat is the new client name?: ")
        # index = clients.index(client_name)
        # clients[index] = updated_client_name
        
    else:
        print(f"\n\tXX This name is not in the client's list XX\n")


# Función que borra el nombre de un cliente en la lista
def delete_client(client_id):
    global clients

    for idx, cli in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break
    # if client in clients:
    #     clients = clients.remove(client)
        print(f'\nClient deleted succesfully!')
    else:
        print(f"\n\tXX This name is not in the client's list XX\n")


def search_client(client_name):
    # No se agrega clients como variable global pues solo se leerá no modificará.

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


# # Creación de función privada que será auxiliar para separar por comas los nombres
# def _add_comma():
#     global clients
#     clients += ','


def _print_welcome():
    print(f'\n {"*" * 50}')
    print(f'\n\t\tWELCOME TO THE ECOMMERCE')
    print(f'\n\t\tCLIENT MANAGMENT SYSTEM')
    print(f'\n {"*" * 50}')
    print(f'\n {"*" * 50}')
    print(f'\n What would you like to do today?:')
    print(f'\n\t\t [C]reate client')
    print(f'\n\t\t [U]pdate client')
    print(f'\n\t\t [D]elete client')
    print(f"\n\t\t [P]rint list")
    print(f"\n\t\t [S]earch client")


def _get_client_field(field_name):
    field = None

    while not field:  # Loop para ciclar la entrada del campo en queso no lo haya escrito el usuario.
        field = input(f'\n\tWhat is the client {field_name}?: ').strip().title()
    
    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


# def _get_client_name():
#     client_name = None

#     while not client_name:
#         client_name = input(f'\n\tWhat is the client name?: ').strip().title()

#         if client_name == 'exit':
#             client_name = None
#             break

#     if not client_name:
#         sys.exit()
#     return client_name


if __name__ == '__main__':
    print(os.getcwd())

    _initialize_clients_from_storage()

    _print_welcome()

    command = input(f'\n\tChoose an option from above C/D/U/P/S: ')
    command = command.upper().strip()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        # list_clients()
    
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        # list_clients()
        

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        # list_clients()
    
    elif command == 'P':
        list_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found == True:
            print(f'\nThe client {client_name} is in the list.')
        else:
            print(f'\nThe name {client_name} is not in the client\'s list\n')

    else:
        print('Invalid command')

    _save_clients_to_storage()