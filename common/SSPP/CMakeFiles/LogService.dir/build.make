# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ece_user/Documents/ece490-s2016/common/SSPP

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ece_user/Documents/ece490-s2016/common/SSPP

# Include any dependencies generated for this target.
include CMakeFiles/LogService.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/LogService.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/LogService.dir/flags.make

CMakeFiles/LogService.dir/src/services/log_service.cpp.o: CMakeFiles/LogService.dir/flags.make
CMakeFiles/LogService.dir/src/services/log_service.cpp.o: src/services/log_service.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ece_user/Documents/ece490-s2016/common/SSPP/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/LogService.dir/src/services/log_service.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/LogService.dir/src/services/log_service.cpp.o -c /home/ece_user/Documents/ece490-s2016/common/SSPP/src/services/log_service.cpp

CMakeFiles/LogService.dir/src/services/log_service.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/LogService.dir/src/services/log_service.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/ece_user/Documents/ece490-s2016/common/SSPP/src/services/log_service.cpp > CMakeFiles/LogService.dir/src/services/log_service.cpp.i

CMakeFiles/LogService.dir/src/services/log_service.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/LogService.dir/src/services/log_service.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/ece_user/Documents/ece490-s2016/common/SSPP/src/services/log_service.cpp -o CMakeFiles/LogService.dir/src/services/log_service.cpp.s

CMakeFiles/LogService.dir/src/services/log_service.cpp.o.requires:
.PHONY : CMakeFiles/LogService.dir/src/services/log_service.cpp.o.requires

CMakeFiles/LogService.dir/src/services/log_service.cpp.o.provides: CMakeFiles/LogService.dir/src/services/log_service.cpp.o.requires
	$(MAKE) -f CMakeFiles/LogService.dir/build.make CMakeFiles/LogService.dir/src/services/log_service.cpp.o.provides.build
.PHONY : CMakeFiles/LogService.dir/src/services/log_service.cpp.o.provides

CMakeFiles/LogService.dir/src/services/log_service.cpp.o.provides.build: CMakeFiles/LogService.dir/src/services/log_service.cpp.o

# Object files for target LogService
LogService_OBJECTS = \
"CMakeFiles/LogService.dir/src/services/log_service.cpp.o"

# External object files for target LogService
LogService_EXTERNAL_OBJECTS =

services/LogService: CMakeFiles/LogService.dir/src/services/log_service.cpp.o
services/LogService: CMakeFiles/LogService.dir/build.make
services/LogService: lib/libsspp.a
services/LogService: /home/ece_user/Documents/Klampt/Library/KrisLibrary/lib/libKrisLibrary.a
services/LogService: /usr/lib/x86_64-linux-gnu/libboost_thread.so
services/LogService: /usr/lib/x86_64-linux-gnu/libboost_system.so
services/LogService: /usr/lib/x86_64-linux-gnu/libpthread.so
services/LogService: /home/ece_user/Documents/Klampt/Library/glui-2.36/src/lib/libglui.a
services/LogService: /usr/lib/x86_64-linux-gnu/libglut.so
services/LogService: /usr/lib/x86_64-linux-gnu/libXmu.so
services/LogService: /usr/lib/x86_64-linux-gnu/libXi.so
services/LogService: /usr/lib/x86_64-linux-gnu/libGLU.so
services/LogService: /usr/lib/x86_64-linux-gnu/libGL.so
services/LogService: /usr/lib/x86_64-linux-gnu/libSM.so
services/LogService: /usr/lib/x86_64-linux-gnu/libICE.so
services/LogService: /usr/lib/x86_64-linux-gnu/libX11.so
services/LogService: /usr/lib/x86_64-linux-gnu/libXext.so
services/LogService: /usr/lib/x86_64-linux-gnu/libglpk.so
services/LogService: /usr/lib/x86_64-linux-gnu/libtinyxml.so
services/LogService: /usr/lib/libassimp.so
services/LogService: CMakeFiles/LogService.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable services/LogService"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/LogService.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/LogService.dir/build: services/LogService
.PHONY : CMakeFiles/LogService.dir/build

CMakeFiles/LogService.dir/requires: CMakeFiles/LogService.dir/src/services/log_service.cpp.o.requires
.PHONY : CMakeFiles/LogService.dir/requires

CMakeFiles/LogService.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/LogService.dir/cmake_clean.cmake
.PHONY : CMakeFiles/LogService.dir/clean

CMakeFiles/LogService.dir/depend:
	cd /home/ece_user/Documents/ece490-s2016/common/SSPP && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ece_user/Documents/ece490-s2016/common/SSPP /home/ece_user/Documents/ece490-s2016/common/SSPP /home/ece_user/Documents/ece490-s2016/common/SSPP /home/ece_user/Documents/ece490-s2016/common/SSPP /home/ece_user/Documents/ece490-s2016/common/SSPP/CMakeFiles/LogService.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/LogService.dir/depend

