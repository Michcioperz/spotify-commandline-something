#!/usr/bin/env python3
import spotify, random, getpass, jinja2, time

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

if __name__ == '__main__':
    time.sleep(10)
    while True:
       input(trackshowtemplate.render(t = playsth()))
