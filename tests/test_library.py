'''

test_library.py: testing to ensure correct formatting, varibles, and API
                 web output included for metadata in library containers

Copyright (c) 2018, Vanessa Sochat
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

from containershare.container import get_library
from containershare.utils import read_json 
from containershare.validator import ( LibraryValidator,
                                       RuntimeValidator )

import requests
import tempfile
 
import os
import re
import sys
from glob import glob

from unittest import TestCase

VERSION = sys.version_info[0]
here = os.getcwd()

print("*** PYTHON VERSION %s BASE TESTING START ***" %(VERSION))

class TestSubmission(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.LibValidator = LibraryValidator()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_library(self):
        library = get_library()
        self.assertTrue(isinstance(library,list))
        self.library_base = "%s/docs/_library" %(here) 
        self.entries = self.get_changed_files()
        self.added = [x for x in self.entries if '_library' in x] 
        print('Found %s changed or modified files.' %len(self.added))
        for entry in self.added:
            if os.path.exists(entry):
                print("TESTING %s" % entry)
                self.assertTrue(self.LibValidator.validate(entry))

                # Github repository serves Github pages, has metadata/LICENSE
                url = self.LibValidator.metadata['github']
                print('Checking Github repository %s' % url)
                result = self.RuntimeValidator.validate(url)
                print(result)
                print(url)        
                self.assertTrue(result)

                # Docker Hub url is valid, as is web
                url = self.LibValidator.metadata['docker']
                print('Checking Docker Hub url %s' % url)
                result = self.RuntimeValidator.validate_url(url)
                print(result)
                print(url)        
                self.assertTrue(result)

                # Github pages found via GIthub must == metadata
                found = self.LibValidator.metadata['web']
                ghpages = self.RuntimeValidator.github_pages
                if found != ghpages:                    
                    print('%s found in metadata != %s' %(found, ghpages))
                self.assertTrue(found == ghpages)


    def get_changed_files(self):
        '''use the Github compare url (provided by circle) to find 
        changed files between commits'''

        # Fallback, return all files in experiment base
        containers = glob("%s/*" %self.library_base)

        compare_url = os.environ.get("CIRCLE_COMPARE_URL")
        if compare_url is not None:
            print('Detected running in Circle CI')
            compare_url = "%s.patch" % compare_url
            print("Compare URL: %s" %compare_url)
            response = requests.get(compare_url) 
            if response.status_code == 200:
                containers = set(re.findall(' docs/_library/.+[.]md',response.text))
                containers = [x.strip() for x in containers]        
        else:
            print("Not running in Circle Ci")

        return containers


if __name__ == '__main__':
    unittest.main()
