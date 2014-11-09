/*
 * Copyright (C) 2014 Christian Stigen Larsen
 * Distributed under the GPL v3 or later. See COPYING.
 */

#include <string>
#include <stdio.h>
#include "fileptr.h"

FilePtr::FilePtr(const char* filename, const char* mode):
  f(fopen(filename, mode))
{
  if ( !f ) {
    std::string msg = "Could not open ";
    throw std::runtime_error((msg + filename).c_str());
  }
}

FilePtr::~FilePtr() {
  fclose(f);
}
