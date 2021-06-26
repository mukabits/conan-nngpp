import os
from conans import ConanFile

class NngppConan(ConanFile):
  name = "nngpp"
  version = "1.3.0"
  sha = "cc5d2641babab165d8a9943817c46d36c6dc17c2"
  source_subfolder = "source"
  license = "MIT"
  url = "https://github.com/cwzx/nngpp"
  description = "C++ wrapper around the nanomsg NNG API"
  requires = "nng/1.3.2"

  def source(self):
    self.run("git clone https://github.com/cwzx/nngpp.git " + self.source_subfolder)
    self.run("cd %s && git checkout %s" % (self.source_subfolder, self.sha))

  def package(self):
    self.copy("*.h")

  def package_info(self):
    self.cpp_info.includedirs = [os.path.join(self.source_subfolder, "include")]
