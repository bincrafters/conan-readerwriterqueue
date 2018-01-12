#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ReaderwriterqueueConan(ConanFile):
    name = "readerwriterqueue"
    version = "1.0.0"
    url = "https://github.com/bincrafters/conan-readerwriterqueue"
    description = "A fast single-producer, single-consumer lock-free queue for C++"
    
    # Indicates License type of the packaged library
    license = "https://github.com/cameron314/readerwriterqueue/blob/master/LICENSE.md"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/cameron314/readerwriterqueue"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = self.source_subfolder
        self.copy(pattern="LICENSE")
        self.copy(pattern="*h", dst="include/readerwriterqueue", src=include_folder)

    def package_id(self):
        self.info.header_only()
