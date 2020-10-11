import sys, os, webbrowser
from optparse import OptionParser
from urllib.parse import urlparse
import gevent
from locust import HttpUser, task, constant
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging

setup_logging("DEBUG", None)

def locust_run(c, r, t, base, path, webui):
    class User(HttpUser):
        wait_time = constant(1)
        host = base

        @task
        def my_task(self):
            self.client.get(path)

    env = Environment(user_classes=[User])
    env.create_local_runner()
    if webui:
        env.create_web_ui("127.0.0.1", 8089)
        webbrowser.open('http://127.0.0.1:8089')
    gevent.spawn(stats_printer(env.stats))
    gevent.spawn(stats_history, env.runner)
    env.runner.start(c, spawn_rate=c)
    gevent.spawn_later(t, lambda: env.runner.quit())
    env.runner.greenlet.join()
    if webui:
        env.web_ui.stop()

if __name__ == "__main__":
    parser = OptionParser("\nEste script basado en locust, permite hacer benchmarking de la PI.API.", version = "0.1")
    parser.add_option("--con", "-c", dest = "c", default = 10,
                    help = "Conexiones concurrentes. Por defecto: 10")
    parser.add_option("--req", "-r", dest = "r", default = 100,
                    help = "Cantidad de peticiones. Por defecto: 100")
    parser.add_option("--tim", "-t", dest = "t", default = False,
                    help = "Tiempo total de testing. Por defecto: Cantidad/Conexiones")
    parser.add_option("--url", "-u", dest = "u", default = False,
                    help = "URL/Endpoint de la API para testear. Obligatorio.")
    parser.add_option("--webui", "-w", dest = "w", default = False,
                    help = "Para levantar interfaz gráfica")
    (options, args) = parser.parse_args()

    if not options.u:
        parser.error('Se debe indicar una URL/Endpoint para testear.')

    url = urlparse(options.u)
    base = '{}://{}'.format(url.scheme,url.netloc)
    path = '{}?{}'.format(url.path,url.query)
    print(base)
    print(path)

    if not options.t:
        t = int(int(options.r)/int(options.c))
    else:
        t = int(options.t)

    locust_run(int(options.c), int(options.r), t, base, path, options.w)