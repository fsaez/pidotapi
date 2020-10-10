import sys, os
from optparse import OptionParser
from locust import HttpUser, between, task

if __name__ == "__main__":
    parser = OptionParser("\nEste script basado en locust, permite hacer benchmarking de la PI.API.", version = "0.1")
    parser.add_option("--con", "-c", dest = "c", default = False,
                    help = "Archivo CSV con usuarios para agregar")
    parser.add_option("--delete", "-d", dest = "d", default = False,
                    help = "Eliminar usuario [Excepto de Google]")
    parser.add_option("--gy", "-y", dest = "gy", action="store_true", default = False,
                    help = "Usar esta opción para usuarios ya creados en Google, para ser considerados en la BD.")
    parser.add_option("--gc", "-x", dest = "gc", action="store_true", default = False,
                    help = "Usar esta opción para cambiar contraseña en Google (Desactivado por defecto).")
    (options, args) = parser.parse_args()

    if (options.c):