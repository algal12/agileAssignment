import socket


def get_service_name(port, protocol):
    """
    Retrieve the service name running on a given port and protocol.
    :param port: Port number
    :param protocol: Protocol type ('tcp' or 'udp')
    :return: Service name or 'Unknown Service' if not found
    """
    try:
        service_name = socket.getservbyport(port, protocol)
        return service_name
    except OSError:
        return "Unknown Service"


def find_services(ports, protocol):
    """
    Map services to open ports based on the provided ports.
    :param ports: A single port (int) or a list of ports
    :param protocol: Protocol type ('tcp' or 'udp')
    :return: Dictionary with services for the provided ports
    """
    if not ports:
        print("No ports provided for service lookup.")

    # Ensure ports is a list
    if isinstance(ports, int):
        ports = [ports]

    services = {}
    for port in ports:
        service_name = get_service_name(port, protocol)
        services[port] = service_name
    return services


def display_services(services, protocol):
    """
    Display the services running on the open ports.
    :param services: Dictionary of port-service mappings
    :param protocol: Protocol type ('tcp' or 'udp')
    """
    print(f"\n{protocol.upper()} Services on Ports:")
    for port, service in services.items():
        print(f"Port {port}: {service}")
