# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
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
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build

# Include any dependencies generated for this target.
include CMakeFiles/example_wirelessHandle.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/example_wirelessHandle.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/example_wirelessHandle.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/example_wirelessHandle.dir/flags.make

CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o: CMakeFiles/example_wirelessHandle.dir/flags.make
CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o: ../examples/example_wirelessHandle.cpp
CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o: CMakeFiles/example_wirelessHandle.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o -MF CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o.d -o CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o -c /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/examples/example_wirelessHandle.cpp

CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/examples/example_wirelessHandle.cpp > CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.i

CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/examples/example_wirelessHandle.cpp -o CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.s

# Object files for target example_wirelessHandle
example_wirelessHandle_OBJECTS = \
"CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o"

# External object files for target example_wirelessHandle
example_wirelessHandle_EXTERNAL_OBJECTS =

example_wirelessHandle: CMakeFiles/example_wirelessHandle.dir/examples/example_wirelessHandle.cpp.o
example_wirelessHandle: CMakeFiles/example_wirelessHandle.dir/build.make
example_wirelessHandle: CMakeFiles/example_wirelessHandle.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable example_wirelessHandle"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_wirelessHandle.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/example_wirelessHandle.dir/build: example_wirelessHandle
.PHONY : CMakeFiles/example_wirelessHandle.dir/build

CMakeFiles/example_wirelessHandle.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/example_wirelessHandle.dir/cmake_clean.cmake
.PHONY : CMakeFiles/example_wirelessHandle.dir/clean

CMakeFiles/example_wirelessHandle.dir/depend:
	cd /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build /home/jessica/ros2_ws/src/unitree_ros2_to_real/unitree_legged_sdk/build/CMakeFiles/example_wirelessHandle.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/example_wirelessHandle.dir/depend

