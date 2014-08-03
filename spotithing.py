#!/usr/bin/env python3
import spotify, random, getpass, jinja2, time, sys

trackshowtemplate = jinja2.Template("""{% for artist in t.artists %}{{artist.name}} {% endfor %}- {{ t.name }} - {{ t.album.name }}""")
config = spotify.Config()
config.user_agent = 'Michify'
config.load_application_key_file()
session = spotify.Session(config)
session.preferred_bitrate(spotify.Bitrate.BITRATE_96k)
if session.remembered_user_name is None:
    session.login(input('Username: '), getpass.getpass(), remember_me=True)
else:
    session.relogin()
eventloop = spotify.EventLoop(session)
eventloop.start()
sound = spotify.AlsaSink(session)
strd = session.get_starred()
session.process_events()
session.process_events()
session.process_events()
def playsth():
    t = random.choice(strd.tracks)
    session.player.load(t)
    session.player.play()
    return t
def playanwa():
    try:
        input(trackshowtemplate.render(t = playsth()))
    except IndexError:
        playanwa()

if __name__ == '__main__':
    print("I will now do backend magic, wait a minute")
    print("%s [" % random.choice(["Charging low orbit ion cannon","Trying to catch Pikachu","Starting a flame war on Reddit","Saving the world (to a file)"]),end='')
    while session.connection.state is not spotify.ConnectionState.LOGGED_IN:
        print('.', end='')
        session.process_events()
        sys.stdout.flush()
        time.sleep(0.1)
    print('|', end='')
    strd.load()
    while not strd.is_loaded:
        print('.', end='')
        session.process_events()
        sys.stdout.flush()
        time.sleep(0.1)
    print('|', end='')
    strd.set_in_ram(True)
    while not strd.is_in_ram:
        print('.', end='')
        session.process_events()
        sys.stdout.flush()
        time.sleep(0.1)
    print(']')
    while True:
        playanwa()
