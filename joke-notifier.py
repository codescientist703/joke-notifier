from win10toast import ToastNotifier
import pyjokes
import time

toast = ToastNotifier()
while True:
	joke = pyjokes.get_joke(category='all')
	toast.show_toast('Joke time !!', joke, icon_path=None, duration=3)
	time.sleep(6)
