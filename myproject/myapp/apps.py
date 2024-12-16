import requests

BASE_URL = 'http://127.0.0.1:8000/api'
TOKEN = None

def get_token(username, password):
    """Obtiene el token de acceso usando las credenciales del usuario."""
    global TOKEN
    response = requests.post(f'{BASE_URL}/token/', json={'username': username, 'password': password})
    if response.status_code == 200:
        TOKEN = response.json().get('access')
        print("Autenticación exitosa.")
    else:
        print("Error de autenticación:", response.json())

def create_task(title, description):
    """Crea una nueva tarea en la API."""
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    response = requests.post(f'{BASE_URL}/tasks/', headers=headers, json={'title': title, 'description': description})
    if response.status_code == 201:
        print("Tarea creada:", response.json())
    else:
        print("Error al crear tarea:", response.json())

def list_tasks():
    """Lista todas las tareas desde la API."""
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.get(f'{BASE_URL}/tasks/', headers=headers)
    if response.status_code == 200:
        tasks = response.json()
        print("Tareas:")
        for task in tasks:
            status = 'Completada' if task['completed'] else 'Pendiente'
            print(f"ID: {task['id']} | Título: {task['title']} | Estado: {status}")
    else:
        print("Error al obtener tareas:", response.json())

def update_task(task_id, title, description):
    """Actualiza una tarea existente en la API."""
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    response = requests.put(f'{BASE_URL}/tasks/{task_id}/', headers=headers, json={'title': title, 'description': description})
    if response.status_code == 200:
        print("Tarea actualizada:", response.json())
    else:
        print("Error al actualizar tarea:", response.json())

def delete_task(task_id):
    """Elimina una tarea de la API."""
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.delete(f'{BASE_URL}/tasks/{task_id}/', headers=headers)
    if response.status_code == 204:
        print("Tarea eliminada.")
    else:
        print("Error al eliminar tarea:", response.json())

def menu():
    """Muestra el menú principal y maneja las opciones del usuario."""
    while True:
        print("\nMenú:")
        print("1. Iniciar sesión")
        print("2. Crear tarea")
        print("3. Listar tareas")
        print("4. Actualizar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            get_token(username, password)
        elif choice == '2':
            title = input("Ingrese el título de la tarea: ")
            description = input("Ingrese la descripción de la tarea: ")
            create_task(title, description)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            task_id = input("Ingrese el ID de la tarea a actualizar: ")
            title = input("Ingrese el nuevo título de la tarea: ")
            description = input("Ingrese la nueva descripción de la tarea: ")
            update_task(task_id, title, description)
        elif choice == '5':
            task_id = input("Ingrese el ID de la tarea a eliminar: ")
            delete_task(task_id)
        elif choice == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
