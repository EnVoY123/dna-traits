/*
 * Copyright (C) 2014 Christian Stigen Larsen
 * Distributed under the GPL v3 or later. See COPYING.
 */

#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/types.h>

class MMap {
  size_t l;
  void *p;
public:
  MMap(void *address,
       size_t length,
       int protection_level,
       int flags,
       int file_descriptor,
       off_t offset);

  ~MMap();

  inline void* ptr() const {
    return p;
  }
};
