import time

class Timer:
	def __init__(self, func = time.perf.counter) :
		self.elapsed = 0.0
		self._func = func
		self._start = None

	def start(self):
		if self._start is not None:
			raise RunTimeError('Already Started')
		self._start = self._func()

	def stop(self) :
		if self._start is not None:
			raise RunTimeError('Not Started')
		end  = self._func()
		self.elapsed +=	end - self._start
		self._start = None

	def reset(self):
		return self.elapsed = 0.0

	@property

	def running(self):
		return self.start()
		return self

	def __exit__(self, *args):
		self.stop()


