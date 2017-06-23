#!/usr/bin/env python
from os import path
from conans import ConanFile


class CatchConan(ConanFile):
    name = "Catch"
    version = "1.9.5"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"
    author = "philsquared"
    generators = "cmake"
    exports_sources = "include/*"
    url = "https://github.com/philsquared/Catch"
    license = "BSL-1.0"

    def build(self):
        pass

    def package(self):
        self.copy(pattern="*", src="include", dst="include")
