import uvicorn
import click
import sys

@click.command()
@click.option('--host', '-H', type=str, default='127.0.0.1')
@click.option('--port', '-P', type=int, default=5000)
def cli(host, port):

    uvicorn.run("industria.app:app", log_level="info", host=host, port=port)

    # I am apparently not smart enough to make a server and window application run at the same time. I will give up on this since this is a non-essential feature.
    # if appmode:
    #     def pcef(host, port):
    #         try:
    #             from cefpython3 import cefpython as cef

    #             sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    #             cef.Initialize()
    #             cef.CreateBrowserSync(url="http://{host}:{prot}",
    #                                 window_title="Industria")
    #             cef.MessageLoop()
    #             cef.Shutdown()
    #         except ImportError:
    #             click.echo(click.style('ERROR: You do not have `cefpython3` installed, and therefore cannot run in app mode. `cefpython3` is an optional dependency for this package that is necessary to run this package in app mode. To install, run `python3 -m pip install cefpython3==66.0`.', fg='red'))

    #     p = Process(target=pcef, args=(host, port), daemon=True)
    #     p.start()

    #     start_server(host, port)

    #     p.join()
    
    # else:
        # start_server(host, port)

if __name__ == '__main__':
    cli()