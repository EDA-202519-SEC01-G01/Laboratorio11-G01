"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
"""


from DataStructures.List import single_linked_list as lt
from DataStructures.Map import map_linear_probing as m
from DataStructures.Graph import digraph as G
from DataStructures.Graph import dijkstra_structure as dijkstra

import csv
import time
import os

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/singapur_bus_routes/'




def init():
    """
    Llama la función de inicialización del modelo.
    """
    analyzer = new_analyzer()
    return analyzer


def new_analyzer():
    analyzer = {
        'stops': None,
        'connections': None,
        'components': None,
        'paths': None
    }

    analyzer['stops'] = m.new_map(
        num_elements=14000, load_factor=0.7, prime=109345121)

    analyzer['connections'] = G.new_graph(order=14000)

    return analyzer




def load_services(analyzer, servicesfile):
    """
    Carga los datos del archivo CSV y crea conexiones entre estaciones adyacentes
    del mismo servicio y sentido.
    """
    servicesfile = data_dir + servicesfile
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"), delimiter=",")
    lastservice = None

    for service in input_file:
        if lastservice is not None:
            sameservice = lastservice['ServiceNo'] == service['ServiceNo']
            samedirection = lastservice['Direction'] == service['Direction']
            samebusStop = lastservice['BusStopCode'] == service['BusStopCode']

            if sameservice and samedirection and not samebusStop:
                print(f"[IF OK] Servicio {service['ServiceNo']} | {lastservice['BusStopCode']} -> {service['BusStopCode']}")
                add_stop_connection(analyzer, lastservice, service)
        lastservice = service

    return analyzer





def set_station(analyzer, station):
    """
    Establece la estación base y crea estructura Dijkstra
    """
    try:
        station = str(station)
        vertex = G.get_vertex(analyzer['connections'], station)
        if vertex is not None:
            analyzer['paths'] = dijkstra.new_dijsktra_structure(station, G.order(analyzer['connections']))
            return True
        else:
            return False
    except Exception as exp:
        return exp


def total_stops(analyzer):
    """
    Total de paradas de autobús
    """
    return G.order(analyzer['connections'])


def total_connections(analyzer):
    """
    Total de enlaces entre paradas
    """
    return G.size(analyzer['connections'])




def get_time():
    """
    Tiempo de procesamiento actual en milisegundos
    """
    return float(time.perf_counter() * 1000)


def delta_time(end, start):
    """
    Diferencia de tiempo entre dos marcas
    """
    return float(end - start)




def add_stop_connection(analyzer, lastservice, service):
    """
    Agrega conexiones entre estaciones adyacentes del mismo bus.
    """
    try:
        origin = format_vertex(lastservice)
        destination = format_vertex(service)
        clean_service_distance(lastservice, service)
        distance = abs(float(service['Distance']) - float(lastservice['Distance']))
        add_stop(analyzer, origin)
        add_stop(analyzer, destination)
        add_connection(analyzer, origin, destination, distance)
        add_route_stop(analyzer, service)
        add_route_stop(analyzer, lastservice)
        return analyzer
    except Exception as exp:
        return exp



def add_stop(analyzer, stopid):
    """
    Adiciona un vértice al grafo
    """
    G.insert_vertex(analyzer['connections'], stopid, stopid)
    return analyzer


def add_route_stop(analyzer, service):
    """
    Agrega una ruta a la lista de rutas que pasan por una estación
    """
    lstroutes = m.get(analyzer['stops'], service['BusStopCode'])
    if lstroutes is None:
        lstroutes = lt.new_list()
        lt.add_last(lstroutes, service['ServiceNo'])
        m.put(analyzer['stops'], service['BusStopCode'], lstroutes)
    else:
        lstroutes = lstroutes['value']
        if not lt.is_present(lstroutes, service['ServiceNo']):
            lt.add_last(lstroutes, service['ServiceNo'])
    return analyzer


def add_connection(analyzer, origin, destination, distance):
    if G.get_vertex(analyzer['connections'], origin) is not None and \
       G.get_vertex(analyzer['connections'], destination) is not None:
        print(f"[ADD_CONNECTION] {origin} -> {destination} con peso {distance}")
        G.add_edge(analyzer['connections'], origin, destination, distance)
    else:
        print(f"[ERROR] Alguno de los vértices no existe: {origin}, {destination}")






def clean_service_distance(lastservice, service):
    """
    Si no hay valor de distancia, se reemplaza con 0
    """
    if service['Distance'] == '':
        service['Distance'] = 0
    if lastservice['Distance'] == '':
        lastservice['Distance'] = 0


def format_vertex(service):
    """
    Nombre del vértice = código estación + '-' + número de ruta
    """
    return service['BusStopCode'] + '-' + service['ServiceNo']

